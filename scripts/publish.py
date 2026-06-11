#!/usr/bin/env python3
"""
实现逻辑：
1. 以当前脚本所在 Skill 目录为根目录，默认读取 skill_root/data/states/toutiao.json 并写入 skill_root/data/runs。
2. 读取用户发布 JSON 和 config/selectors.json，按 content_blocks 顺序填充正文段落、小标题和图片，并单独上传封面图。
3. 自动发布时处理“预览并发布”“确认发布”“作品同步授权”等正常平台链路；文章发布选项按稳定 selector 和当前状态设置，遇到验证码、风控或失败提示立即退出并保留诊断。
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from playwright.sync_api import Error, TimeoutError as PlaywrightTimeoutError, sync_playwright

from account_paths import SKILL_ROOT, build_account_paths, default_read_state_path, display_path


TOUTIAO_PUBLISH_URL = "https://mp.toutiao.com/profile_v4/graphic/publish"
SELECTORS_PATH = SKILL_ROOT / "config" / "selectors.json"
VERIFICATION_PATTERNS = ["验证码", "滑块", "安全验证", "环境异常", "操作频繁", "登录已失效"]
FAILURE_PATTERNS = ["发布失败", "保存失败", "请填写", "请上传", "审核不通过", "操作失败"]
SUCCESS_PATTERNS = ["发布成功", "发表成功", "发布完成", "已发布", "作品管理"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Publish a Toutiao article with Playwright storage_state.")
    parser.add_argument("--input", required=True, help="Path to publish JSON. Relative paths are resolved from skill root.")
    parser.add_argument("--account", default="default", help="Account alias used under data/accounts/{account}.")
    parser.add_argument("--data-dir", default="")
    parser.add_argument("--state-path", default="")
    parser.add_argument("--run-dir", default="")
    parser.add_argument("--headed", action="store_true", help="Run with a visible browser.")
    parser.add_argument("--browser-channel", default="")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    account_paths = build_account_paths(args.data_dir, args.account)
    input_path = resolve_path(args.input, account_paths)
    payload = read_json(input_path)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    state_path = Path(args.state_path).expanduser() if args.state_path else default_read_state_path(account_paths)
    run_dir = Path(args.run_dir).expanduser() if args.run_dir else account_paths.runs_dir / f"toutiao-{timestamp}"
    run_dir.mkdir(parents=True, exist_ok=True)

    log_file = run_dir / "worker.log"
    with log_file.open("w", encoding="utf-8") as log:
        try:
            result = run_publish(args, payload, state_path, run_dir, account_paths.account, log)
        except Exception as exc:
            result = {
                "success": False,
                "published": False,
                "platform": "toutiao",
                "error_message": str(exc),
                "run_dir": display_path(run_dir),
            }
            write_log(log, f"failed: {exc}")
        write_result(run_dir / "result.json", result)

    print(json.dumps(result, ensure_ascii=False, indent=2), flush=True)
    if not result.get("success"):
        raise SystemExit(1)


def run_publish(args: argparse.Namespace, payload: dict, state_path: Path, run_dir: Path, account: str, log) -> dict:
    selectors = load_selectors()
    validate_payload(payload, state_path)
    title = str(payload["title"]).strip()[:80]
    publish_options = build_publish_options(payload)
    publish_mode = str(payload.get("publish_mode", "auto")).strip().lower()
    if publish_mode not in {"auto", "draft"}:
        raise ValueError("publish_mode 只能是 auto 或 draft")

    content_blocks = prepare_content_blocks(payload["content_blocks"], run_dir / "content-images", account)
    cover_image_paths = prepare_images(cover_image_values(payload), run_dir / "cover-images", account)
    write_log(
        log,
        "platform=toutiao "
        f"account={account} mode={publish_mode} "
        f"content_blocks={len(content_blocks)} cover_images={len(cover_image_paths)} "
        f"skill_root={SKILL_ROOT}",
    )

    page = None
    with sync_playwright() as playwright:
        launch_options = {
            "headless": not args.headed,
            "args": ["--disable-blink-features=AutomationControlled"],
        }
        if args.browser_channel:
            launch_options["channel"] = args.browser_channel
        browser = playwright.chromium.launch(**launch_options)
        try:
            context = browser.new_context(
                storage_state=str(state_path),
                viewport={"width": 1440, "height": 900},
            )
            page = context.new_page()
            page.goto(selectors.get("publish_url") or TOUTIAO_PUBLISH_URL, wait_until="domcontentloaded", timeout=60000)
            page.wait_for_timeout(4000)
            detect_verification(page)
            fill_title(page, title, selectors)
            fill_content_blocks(page, content_blocks, selectors, log)
            handle_cover(page, cover_image_paths, selectors, log, publish_options.get("cover_mode", ""))
            upload_cover_image(page, cover_image_paths, selectors, log)
            handle_publish_options(page, selectors, publish_options, log)
            take_screenshot(page, run_dir / "before_publish.png")

            published = False
            if publish_mode == "auto":
                publish_to_toutiao(page, run_dir, title, selectors, publish_options, log)
                published = True
            else:
                write_log(log, "draft mode: skipped publish click")

            return {
                "success": True,
                "published": published,
                "platform": "toutiao",
                "account": account,
                "platform_url": page.url,
                "message": "已自动发布到头条号" if published else "已打开并填充内容，未点击发布",
                "run_dir": display_path(run_dir),
            }
        except Exception:
            if page is not None:
                take_screenshot(page, run_dir / "failure.png")
            raise
        finally:
            browser.close()


def validate_payload(payload: dict, state_path: Path) -> None:
    if not state_path.exists():
        raise ValueError(f"登录态不存在：{state_path}。请先运行 scripts/login.py")
    if not str(payload.get("title", "")).strip():
        raise ValueError("输入 JSON 缺少 title")
    if not isinstance(payload.get("content_blocks"), list) or not payload.get("content_blocks"):
        raise ValueError("输入 JSON 缺少 content_blocks")
    if not str(payload.get("cover_image", "")).strip():
        raise ValueError("输入 JSON 缺少 cover_image")
    options = payload.get("options") or {}
    if not isinstance(options, dict):
        raise ValueError("options 必须是对象")


def build_publish_options(payload: dict) -> dict:
    options = payload.get("options") or {}
    source_declarations = options.get("source_declarations", options.get("source_declaration"))
    if source_declarations is None and options.get("personal_opinion", True):
        source_declarations = ["personal_opinion"]
    elif source_declarations is None:
        source_declarations = []
    if isinstance(source_declarations, str):
        source_declarations = [source_declarations]
    return {
        "ad_revenue": bool(options.get("ad_revenue", True)),
        "first_publish": bool(options.get("first_publish", False)),
        "source_declarations": normalize_string_list(source_declarations),
        "sync_weitoutiao": bool(options.get("sync_weitoutiao", False)),
        "cover_mode": str(options.get("cover_mode", "")).strip().lower(),
    }


def normalize_string_list(value) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        items = [value]
    elif isinstance(value, list):
        items = value
    else:
        raise ValueError("列表字段必须是字符串或字符串数组")
    normalized = []
    for item in items:
        text = str(item).strip()
        if text:
            normalized.append(text)
    return normalized


def cover_image_values(payload: dict) -> list[str]:
    value = payload.get("cover_image")
    return image_values([value])


def image_values(images: list) -> list[str]:
    values: list[str] = []
    for image in images:
        if isinstance(image, str):
            values.append(image)
            continue
        if isinstance(image, dict):
            value = image.get("path") or image.get("url") or image.get("src") or ""
            if value:
                values.append(str(value))
    return values


def prepare_content_blocks(blocks: list[dict], image_dir: Path, account: str) -> list[dict]:
    image_dir.mkdir(parents=True, exist_ok=True)
    prepared: list[dict] = []
    image_index = 1
    for index, block in enumerate(blocks, start=1):
        if not isinstance(block, dict):
            raise ValueError(f"content_blocks 第 {index} 项必须是对象")
        block_type = str(block.get("type", "")).strip().lower()
        if block_type in {"paragraph", "heading"}:
            text = str(block.get("text", "")).strip()
            if text:
                prepared.append({"type": block_type, "text": text})
            continue
        if block_type == "image":
            image_value = image_values([block.get("src") or block.get("path") or block.get("url") or block])
            if not image_value:
                raise ValueError(f"content_blocks 第 {index} 个图片块缺少 src/path/url")
            paths = prepare_images(image_value[:1], image_dir / f"block_{image_index}", account)
            if not paths:
                raise ValueError(f"content_blocks 第 {index} 个图片块下载或复制失败")
            prepared.append({
                "type": "image",
                "path": paths[0],
                "caption": str(block.get("caption", "")).strip(),
            })
            image_index += 1
            continue
        raise ValueError(f"content_blocks 第 {index} 项 type 不支持：{block_type}")
    if not any(block["type"] in {"paragraph", "heading"} for block in prepared):
        raise ValueError("content_blocks 至少需要一个 paragraph 或 heading")
    return prepared


def fill_title(page, title: str, selectors: dict) -> None:
    selectors = [
        selector_value(selectors, "article_publish.title"),
        "textarea[placeholder*='标题']",
        "input[placeholder*='标题']",
        "textarea",
        "xpath=//*[@id='root']/div/div[1]/div/div[1]/div[3]/div/div/div[2]/div/div/div/textarea",
    ]
    fill_first_match(page, selectors, title, "未找到头条号标题输入框")


def editor_locator(page, selectors: dict):
    selectors = [
        "[contenteditable='true']",
        "div.ProseMirror",
        selector_value(selectors, "article_publish.content"),
        "xpath=//*[@id='root']/div/div[1]/div/div[1]/div[4]/div/div[1]",
    ]
    for selector in selectors:
        if not selector:
            continue
        try:
            locator = page.locator(selector).first
            locator.wait_for(state="visible", timeout=8000)
            return locator
        except Exception:
            continue
    raise RuntimeError("未找到头条号正文编辑区")


def fill_content_blocks(page, blocks: list[dict], selectors: dict, log) -> None:
    editor = editor_locator(page, selectors)
    editor.click(timeout=3000)
    for block in blocks:
        block_type = block["type"]
        if block_type == "heading":
            insert_editor_text(page, editor, f"{block['text']}\n\n")
            write_log(log, f"inserted heading: {block['text'][:30]}")
            continue
        if block_type == "paragraph":
            insert_editor_text(page, editor, f"{block['text']}\n\n")
            continue
        if block_type == "image":
            insert_single_content_image(page, block["path"], log)
            if block.get("caption"):
                insert_editor_text(page, editor, f"{block['caption']}\n\n")
            continue
    write_log(log, f"inserted content blocks: {len(blocks)}")


def insert_editor_text(page, editor, text: str) -> None:
    dismiss_editor_overlay(page)
    editor.click(timeout=3000)
    page.keyboard.press("End")
    try:
        page.keyboard.insert_text(text)
    except Exception:
        editor.evaluate(
            """
            (element, value) => {
              element.focus();
              document.execCommand('insertText', false, value);
              element.dispatchEvent(new InputEvent('input', {
                bubbles: true,
                inputType: 'insertText',
                data: value
              }));
            }
            """,
            text,
        )


def fill_first_match(page, selectors: list[str], value: str, error_message: str) -> None:
    for selector in selectors:
        if not selector:
            continue
        try:
            locator = page.locator(selector).first
            locator.wait_for(state="visible", timeout=8000)
            locator.click(timeout=3000)
            locator.fill(value, timeout=8000)
            return
        except (PlaywrightTimeoutError, Error):
            continue
        except Exception:
            continue
    raise RuntimeError(error_message)


def selected_state(locator) -> bool:
    return bool(locator.evaluate(
        """
        (element) => {
          const root = element.closest('label') || element;
          const input = root.matches('input') ? root : root.querySelector('input');
          if (input && (input.type === 'checkbox' || input.type === 'radio')) return Boolean(input.checked);
          return Boolean(
            root.getAttribute('aria-checked') === 'true' ||
            root.querySelector('[aria-checked="true"], .checked, .byte-checkbox-checked, .byte-checkbox-wrapper-checked, .byte-radio-inner.checked')
          );
        }
        """
    ))


def set_checked_selector(page, selector: str, enabled: bool, log, label: str, timeout: int = 5000) -> None:
    if not selector:
        raise RuntimeError(f"缺少 selector: {label}")
    locator = page.locator(selector).first
    locator.wait_for(state="visible", timeout=timeout)
    checked = selected_state(locator)
    try:
        is_enabled = locator.is_enabled(timeout=1000)
    except Exception:
        is_enabled = True
    if checked != enabled:
        if not is_enabled:
            if not enabled:
                write_log(log, f"skip disabled {label}: current={checked}, target={enabled}")
                return
            raise RuntimeError(f"{label} 被平台禁用，无法设置为 {enabled}")
        locator.scroll_into_view_if_needed(timeout=3000)
        locator.click(timeout=timeout)
        page.wait_for_timeout(700)
        write_log(log, f"set {label}={enabled}")
        return
    write_log(log, f"{label} already {enabled}")


def handle_cover(page, image_paths: list[Path], selectors: dict, log, cover_mode: str = "") -> None:
    normalized_mode = cover_mode if cover_mode in {"single", "triple", "none"} else ""
    if not normalized_mode:
        normalized_mode = "single" if image_paths else "none"
    selector = selector_value(selectors, f"article_publish.cover.{normalized_mode}")
    set_checked_selector(page, selector, True, log, f"cover mode {normalized_mode}")


def insert_single_content_image(page, image_path: Path, log) -> None:
    try:
        editor = page.locator("[contenteditable='true']").first
        editor.click(timeout=5000)
        page.keyboard.press("End")
    except Exception:
        pass
    try:
        page.locator(".syl-toolbar-tool.image.static").first.click(timeout=8000)
        upload_images_from_open_dialog(page, [image_path], log, "content image")
        close_drawer_if_visible(page, log)
        write_log(log, f"inserted content image: {display_path(image_path)}")
    except Exception as exc:
        close_drawer_if_visible(page, log)
        write_log(log, f"toutiao content image upload skipped/failed: {exc}")


def upload_cover_image(page, image_paths: list[Path], selectors: dict, log) -> None:
    if not image_paths:
        return
    try:
        if open_cover_drawer(page, selectors, log):
            upload_cover_from_drawer(page, image_paths[0], log)
            close_drawer_if_visible(page, log)
            write_log(log, "uploaded cover image")
            return
        raise RuntimeError("未找到可用的封面上传入口")
    except Exception as exc:
        close_drawer_if_visible(page, log)
        write_log(log, f"toutiao cover image upload skipped/failed: {exc}")


def open_cover_drawer(page, selectors: dict, log) -> bool:
    locators = [
        locator_from_selector(page, selector_value(selectors, "article_publish.cover.upload")),
        page.locator(".article-cover-images").get_by_text("替换", exact=True).last,
        page.locator(".article-cover-images").get_by_text("编辑", exact=True).last,
        page.locator(".article-cover-images-wrap").locator("div").filter(has_text="替换").last,
    ]
    for locator in locators:
        if locator is None:
            continue
        try:
            locator.wait_for(state="visible", timeout=3000)
            locator.scroll_into_view_if_needed(timeout=3000)
            locator.click(timeout=5000)
            page.locator(".byte-drawer-wrapper").last.wait_for(state="visible", timeout=8000)
            write_log(log, "opened cover drawer")
            return True
        except Exception as exc:
            write_log(log, f"cover drawer candidate failed: {exc}")
            continue
    return False


def upload_cover_from_drawer(page, image_path: Path, log) -> None:
    drawer = page.locator(".byte-drawer-wrapper").last
    upload_tab = drawer.get_by_text("上传图片", exact=True).last
    upload_tab.click(timeout=5000)
    page.wait_for_timeout(1000)
    file_input = drawer.locator("input[type='file'][accept*='image']").first
    if file_input.count() > 0:
        file_input.set_input_files(str(image_path), timeout=15000)
    else:
        with page.expect_file_chooser(timeout=8000) as chooser_info:
            drawer.get_by_text("上传图片", exact=True).last.click(timeout=5000)
        chooser_info.value.set_files(str(image_path))
    page.wait_for_timeout(4000)
    confirm_cover_drawer(page, log)
    write_log(log, f"uploaded cover from drawer: {display_path(image_path)}")


def confirm_cover_drawer(page, log) -> None:
    drawer = page.locator(".byte-drawer-wrapper").last
    locators = [
        drawer.locator("button").filter(has_text="确定").last,
        drawer.locator(".byte-btn-primary").last,
        drawer.get_by_text("确定", exact=True).last,
    ]
    if click_first_enabled(locators, log, "cover drawer confirm", timeout=3000):
        return
    thumbnails = drawer.locator("img")
    if thumbnails.count() > 0:
        thumbnails.last.click(timeout=5000)
        write_log(log, "selected cover drawer thumbnail")
        return
    raise RuntimeError("封面抽屉内未找到确认按钮或图片")


def close_drawer_if_visible(page, log) -> None:
    drawer = page.locator(".byte-drawer-wrapper").last
    try:
        if not drawer.is_visible(timeout=1000):
            return
    except Exception:
        return
    locators = [
        drawer.locator(".byte-drawer-close").last,
        drawer.locator(".byte-icon-close").last,
        drawer.locator("[class*='close']").last,
        drawer.get_by_text("×", exact=True).last,
    ]
    if click_first_enabled(locators, log, "drawer close", timeout=1500):
        wait_drawer_closed(page, log)
        return
    if click_drawer_close_by_dom(page, log):
        wait_drawer_closed(page, log)
        return
    try:
        page.keyboard.press("Escape")
        wait_drawer_closed(page, log)
        write_log(log, "closed drawer with Escape")
    except Exception:
        pass


def dismiss_editor_overlay(page) -> None:
    try:
        page.keyboard.press("Escape")
        page.wait_for_timeout(300)
    except Exception:
        pass
    try:
        clicked = page.evaluate(
            """
            () => {
              const visible = (element) => {
                const rect = element.getBoundingClientRect();
                const style = window.getComputedStyle(element);
                return rect.width > 0 && rect.height > 0 && style.display !== 'none' && style.visibility !== 'hidden';
              };
              const drawers = Array.from(document.querySelectorAll('.byte-drawer-wrapper')).filter(visible);
              const drawer = drawers[drawers.length - 1];
              if (!drawer) return false;
              const drawerRect = drawer.getBoundingClientRect();
              const nodes = Array.from(drawer.querySelectorAll('button, [role="button"], span, div, i, svg'));
              const closeNode = nodes.find((node) => {
                if (!visible(node)) return false;
                const rect = node.getBoundingClientRect();
                return rect.left >= drawerRect.right - 90 && rect.top <= drawerRect.top + 90;
              });
              if (!closeNode) return false;
              closeNode.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true, view: window }));
              return true;
            }
            """
        )
        if clicked:
            page.wait_for_timeout(700)
    except Exception:
        pass


def click_drawer_close_by_dom(page, log) -> bool:
    try:
        clicked = page.evaluate(
            """
            () => {
              const visible = (element) => {
                const rect = element.getBoundingClientRect();
                const style = window.getComputedStyle(element);
                return rect.width > 0 && rect.height > 0 && style.display !== 'none' && style.visibility !== 'hidden';
              };
              const drawers = Array.from(document.querySelectorAll('.byte-drawer-wrapper')).filter(visible);
              const drawer = drawers[drawers.length - 1];
              if (!drawer) return false;
              const candidates = Array.from(drawer.querySelectorAll('button, [role="button"], .byte-icon-close, [class*="close"], span, div'));
              const close = candidates.find((node) => {
                const text = (node.innerText || node.textContent || '').trim();
                const name = node.getAttribute('aria-label') || node.getAttribute('title') || '';
                const cls = node.className ? String(node.className) : '';
                return visible(node) && (text === '×' || name.includes('关闭') || name.toLowerCase().includes('close') || cls.includes('close'));
              });
              if (!close) return false;
              close.click();
              return true;
            }
            """
        )
        if clicked:
            write_log(log, "closed drawer by dom")
            return True
    except Exception as exc:
        write_log(log, f"drawer dom close failed: {exc}")
    return False


def wait_drawer_closed(page, log) -> None:
    try:
        page.locator(".byte-drawer-wrapper").last.wait_for(state="hidden", timeout=3000)
    except Exception:
        page.wait_for_timeout(1000)


def upload_images_from_open_dialog(page, image_paths: list[Path], log, label: str) -> None:
    page.locator("input[type='file'][accept*='image']").first.set_input_files(
        [str(path) for path in image_paths],
        timeout=15000,
    )
    try:
        page.get_by_text(f"已上传 {len(image_paths)} 张图片", exact=False).wait_for(timeout=60000)
    except Exception:
        page.wait_for_timeout(4000)
    page.locator(".byte-drawer-wrapper button").filter(has_text="确定").last.click(timeout=10000)
    page.wait_for_timeout(3000)
    close_drawer_if_visible(page, log)
    write_log(log, f"uploaded {label}: {len(image_paths)}")


def publish_to_toutiao(page, run_dir: Path, title: str, selectors: dict, publish_options: dict, log) -> None:
    print_publish_button_debug(page, log)
    click_publish_button(page, selectors, log)
    page.wait_for_timeout(2500)
    take_screenshot(page, run_dir / "after_first_publish_click.png")
    click_confirm_or_authorization(page, selectors, log)
    page.wait_for_timeout(2000)
    authorization_confirmed = click_authorization_modal_if_visible(page, selectors, log)
    if authorization_confirmed:
        page.wait_for_timeout(2000)
        write_log(log, "authorization confirmed, retry publish chain")
        click_publish_button(page, selectors, log)
        page.wait_for_timeout(2500)
        click_confirm_or_authorization(page, selectors, log)
    page.wait_for_timeout(2500)
    take_screenshot(page, run_dir / "after_confirm_publish_click.png")
    wait_publish_result(page, title, selectors, log)


def handle_publish_options(page, selectors: dict, publish_options: dict, log) -> None:
    page.wait_for_timeout(1000)
    set_ad_revenue_option(page, selectors, bool(publish_options.get("ad_revenue")), log)
    set_toutiao_first_option(page, selectors, bool(publish_options.get("first_publish")), log)
    set_sync_weitoutiao_option(page, selectors, bool(publish_options.get("sync_weitoutiao")), log)
    set_source_declarations(page, selectors, publish_options.get("source_declarations", []), log)


def set_ad_revenue_option(page, selectors: dict, enabled: bool, log) -> None:
    path = "article_publish.ad.enable_revenue" if enabled else "article_publish.ad.disable"
    set_checked_selector(page, selector_value(selectors, path), True, log, f"article ad_revenue {enabled}")


def set_toutiao_first_option(page, selectors: dict, enabled: bool, log) -> None:
    set_checked_selector(page, selector_value(selectors, "article_publish.first_publish"), enabled, log, "article first_publish")


def set_sync_weitoutiao_option(page, selectors: dict, enabled: bool, log) -> None:
    set_checked_selector(page, selector_value(selectors, "article_publish.sync_weitoutiao"), enabled, log, "article sync_weitoutiao")


def set_source_declarations(page, selectors: dict, declarations: list[str], log) -> None:
    source_keys = {
        "network": "network",
        "external": "network",
        "internal": "internal",
        "site": "internal",
        "personal_opinion": "personal_opinion",
        "opinion": "personal_opinion",
        "ai": "ai",
        "fiction": "fiction",
        "story": "fiction",
        "investment": "investment",
        "health": "health",
    }
    for declaration in declarations:
        key = source_keys.get(str(declaration).strip().lower())
        if not key:
            raise ValueError(f"不支持的文章作品声明：{declaration}")
        set_checked_selector(page, selector_value(selectors, f"article_publish.source.{key}"), True, log, f"article source {key}")


def click_publish_button(page, selectors: dict, log) -> None:
    locators = [
        locator_from_selector(page, selector_value(selectors, "article_publish.preview_and_publish")),
        page.get_by_role("button", name="预览并发布").last,
        page.locator("button").filter(has_text="预览并发布").last,
        page.locator(".publish-btn-last").last,
        page.get_by_role("button", name="发布").last,
        page.locator("button").filter(has_text="发布").last,
    ]
    if click_first_enabled(locators, log, "toutiao publish button"):
        return
    if click_visible_text(page, ["预览并发布", "确认发布", "发布"], log):
        return
    raise RuntimeError("未找到头条号发布按钮")


def click_confirm_or_authorization(page, selectors: dict, log) -> None:
    deadline = time.time() + 35
    texts = ["确认发布", "确定发布", "确定", "继续发布", "发布"]
    while time.time() < deadline:
        locators = [
            locator_from_selector(page, selector_value(selectors, "modal.confirm")),
            page.locator(".byte-modal-wrapper").filter(has_text="作品同步授权").locator("button").filter(has_text="确定").last,
            page.locator(".byte-modal-wrapper .byte-modal-footer button.byte-btn-primary").last,
            page.get_by_text("确定", exact=True).last,
        ]
        if click_first_enabled(locators, log, "toutiao modal confirm button", timeout=2000):
            return
        if click_visible_text(page, ["确定"], log, exact=True):
            return
        locators = [
            locator_from_selector(page, selector_value(selectors, "article_publish.confirm_publish")),
        ]
        locators.extend(page.get_by_role("button", name=text).last for text in texts)
        locators.extend(page.locator("button").filter(has_text=text).last for text in texts)
        locators.extend([
            page.get_by_text("确定", exact=True).last,
        ])
        if click_first_enabled(locators, log, "toutiao confirm button", timeout=2000):
            return
        if click_visible_text(page, texts, log, exact=True):
            return
        page.wait_for_timeout(1000)


def click_authorization_modal_if_visible(page, selectors: dict, log) -> bool:
    modal = page.locator(".byte-modal-wrapper").filter(has_text="作品同步授权").last
    try:
        if not modal.is_visible(timeout=2000):
            return False
    except Exception:
        return False
    locators = [
        locator_from_selector(page, selector_value(selectors, "modal.confirm")),
        modal.locator("button").filter(has_text="确定").last,
        modal.locator(".byte-modal-footer button.byte-btn-primary").last,
        modal.get_by_text("确定", exact=True).last,
    ]
    if click_first_enabled(locators, log, "toutiao authorization modal confirm", timeout=3000):
        return True
    return click_visible_text(page, ["确定"], log, exact=True)


def click_first_enabled(locators, log, label: str, timeout: int = 8000) -> bool:
    for locator in locators:
        if locator is None:
            continue
        try:
            locator.wait_for(state="visible", timeout=timeout)
            locator.scroll_into_view_if_needed(timeout=3000)
            if locator.is_enabled(timeout=1000):
                text = ""
                try:
                    text = locator.inner_text(timeout=1000)
                except Exception:
                    pass
                locator.click(timeout=5000)
                write_log(log, f"clicked {label}: {text!r}")
                page_wait(locator)
                return True
        except Exception:
            continue
    return False


def click_visible_text(page, texts: list[str], log, exact: bool = False) -> bool:
    try:
        clicked = page.evaluate(
            """
            ({ texts, exact }) => {
              const isVisible = (element) => {
                const rect = element.getBoundingClientRect();
                const style = window.getComputedStyle(element);
                return rect.width > 0 && rect.height > 0 && style.visibility !== 'hidden' && style.display !== 'none';
              };
              const candidates = Array.from(document.querySelectorAll('button, [role="button"], .byte-btn, .byte-btn-primary, div, span'));
              for (const text of texts) {
                const node = candidates.find((element) => {
                  const content = (element.innerText || element.textContent || '').trim();
                  return isVisible(element) && !element.disabled && (exact ? content === text : content.includes(text));
                });
                if (node) {
                  const clickable = node.closest('button, [role="button"], .byte-btn, .byte-btn-primary') || node;
                  clickable.scrollIntoView({ block: 'center', inline: 'center' });
                  clickable.click();
                  return text;
                }
              }
              return '';
            }
            """,
            {"texts": texts, "exact": exact},
        )
        if clicked:
            write_log(log, f"clicked visible text: {clicked}")
            page.wait_for_timeout(1500)
            return True
    except Exception as exc:
        write_log(log, f"visible text click failed: {exc}")
    return False


def page_wait(locator) -> None:
    try:
        locator.page.wait_for_timeout(1500)
    except Exception:
        pass


def wait_publish_result(page, title: str, selectors: dict, log) -> None:
    deadline = time.time() + 25
    while time.time() < deadline:
        detect_verification(page)
        text = safe_body_text(page)
        if any(pattern in text for pattern in SUCCESS_PATTERNS):
            write_log(log, "publish success detected on publish page")
            return
        for pattern in FAILURE_PATTERNS:
            if pattern in text:
                raise RuntimeError(f"头条号发布失败：{pattern}")
        if page.url and any(part in page.url for part in ["/publish/success", "/manage", "content/manage"]):
            write_log(log, f"publish success inferred by url: {page.url}")
            return
        page.wait_for_timeout(1500)
    if verify_title_in_work_management(page, title, selectors, log):
        return
    raise RuntimeError("等待发布结果超时，作品管理页未确认到标题")


def verify_title_in_work_management(page, title: str, selectors: dict, log) -> bool:
    urls = [
        "https://mp.toutiao.com/profile_v4/manage/content/all",
        "https://mp.toutiao.com/profile_v4/content/manage",
    ]
    normalized_title = normalize_text(title)
    for url in urls:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            page.wait_for_timeout(5000)
            click_selector(page, selector_value(selectors, "work_management.tabs.article"), log, "作品管理文章 tab", timeout=3000)
            page.wait_for_timeout(2500)
            if page_contains_title(page, normalized_title):
                write_log(log, f"publish success verified in work management: {title}")
                return True
            click_selector(page, selector_value(selectors, "work_management.tabs.all"), log, "作品管理全部 tab", timeout=3000)
            page.wait_for_timeout(2500)
            if page_contains_title(page, normalized_title):
                write_log(log, f"publish success verified in work management all tab: {title}")
                return True
        except Exception as exc:
            write_log(log, f"work management verification failed on {url}: {exc}")
    return False


def page_contains_title(page, normalized_title: str) -> bool:
    text = normalize_text(safe_body_text(page))
    return normalized_title in text


def normalize_text(value: str) -> str:
    return "".join(str(value).split())


def detect_verification(page) -> None:
    text = safe_body_text(page)
    for pattern in VERIFICATION_PATTERNS:
        if pattern in text:
            raise RuntimeError(f"出现登录、验证或风控提示：{pattern}")


def safe_body_text(page) -> str:
    try:
        return page.locator("body").inner_text(timeout=3000)
    except Exception:
        return ""


def print_publish_button_debug(page, log) -> None:
    try:
        buttons = page.locator("button, [role='button']")
        count = buttons.count()
        write_log(log, f"[toutiao] button candidates: {count}")
        for index in range(min(count, 30)):
            button = buttons.nth(index)
            try:
                write_log(
                    log,
                    "[toutiao] button "
                    f"#{index}: visible={button.is_visible(timeout=1000)} "
                    f"enabled={button.is_enabled(timeout=1000)} "
                    f"text={button.inner_text(timeout=1000)!r} "
                    f"class={button.get_attribute('class', timeout=1000)!r}",
                )
            except Exception:
                continue
    except Exception as exc:
        write_log(log, f"[toutiao] publish button debug failed: {exc}")


def prepare_images(images: list[str], image_dir: Path, account: str = "default") -> list[Path]:
    image_dir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    for index, image in enumerate(images[:9], start=1):
        value = str(image).strip()
        if not value:
            continue
        if value.startswith(("http://", "https://")):
            downloaded = download_image(value, image_dir / f"image_{index}")
            if downloaded:
                paths.append(downloaded)
            continue
        source = resolve_path(value, build_account_paths("", account))
        if source.exists() and source.is_file():
            copied = image_dir / f"image_{index}{source.suffix.lower() or '.jpg'}"
            shutil.copy2(source, copied)
            paths.append(copied)
    return paths


def download_image(url: str, target_without_suffix: Path) -> Path | None:
    try:
        request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(request, timeout=20) as response:
            content = response.read()
            if len(content) < 1024:
                return None
            suffix = image_suffix(response.headers.get("content-type", ""), url)
            target = target_without_suffix.with_suffix(suffix)
            target.write_bytes(content)
            return target
    except Exception:
        return None


def image_suffix(content_type: str, url: str) -> str:
    if "png" in content_type:
        return ".png"
    if "webp" in content_type:
        return ".webp"
    if "gif" in content_type:
        return ".gif"
    suffix = Path(urlparse(url).path).suffix.lower()
    if suffix in {".jpg", ".jpeg", ".png", ".webp", ".gif"}:
        return suffix
    return ".jpg"


def take_screenshot(page, path: Path) -> None:
    try:
        page.screenshot(path=str(path), full_page=True, timeout=8000)
    except Exception:
        return


def load_selectors() -> dict:
    if not SELECTORS_PATH.exists():
        return {}
    return read_json(SELECTORS_PATH)


def selector_value(selectors: dict, dotted_path: str) -> str:
    value = selectors
    for part in dotted_path.split("."):
        if not isinstance(value, dict):
            return ""
        value = value.get(part)
    return value if isinstance(value, str) else ""


def locator_from_selector(page, selector: str):
    if not selector:
        return None
    return page.locator(selector).first


def click_selector(page, selector: str, log, label: str, timeout: int = 8000) -> bool:
    if not selector:
        return False
    return click_first_enabled([page.locator(selector).first], log, label, timeout=timeout)


def resolve_path(value: str, account_paths=None) -> Path:
    path = Path(value).expanduser()
    if path.is_absolute():
        return path
    if account_paths is not None:
        account_relative = (account_paths.account_dir / path).resolve()
        if account_relative.exists():
            return account_relative
    return (SKILL_ROOT / path).resolve()


def read_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict):
        raise ValueError("输入 JSON 顶层必须是对象")
    return data


def write_result(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def write_log(log, message: str) -> None:
    print(message, file=log, flush=True)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("用户中断", file=sys.stderr)
        raise SystemExit(130)
