#!/usr/bin/env python3
"""
实现逻辑：
1. 以当前脚本所在 Skill 目录为根目录，读取多账号登录态并为每次视频发布创建独立 runs 诊断目录。
2. 读取视频发布 JSON 和 config/selectors.json，按用户提供的稳定 selector 上传视频、填写标题、上传封面并处理发布选项。
3. 自动发布时只走平台正常上传与确认链路；遇到验证码、风控、上传失败或发布失败时退出并保留日志、截图和 result.json。
"""

from __future__ import annotations

import argparse
import json
import time
from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright

from account_paths import build_account_paths, default_read_state_path, display_path
from publish import (
    click_first_enabled,
    click_selector,
    detect_verification,
    load_selectors,
    locator_from_selector,
    read_json,
    resolve_path,
    safe_body_text,
    selector_value,
    take_screenshot,
    write_log,
    write_result,
)


TOUTIAO_HOME_URL = "https://mp.toutiao.com/profile_v4/"
FAILURE_PATTERNS = ["上传失败", "发布失败", "保存失败", "请填写", "请上传", "审核不通过", "操作失败"]
SUCCESS_PATTERNS = ["发布成功", "发表成功", "发布完成", "已发布", "作品管理"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Publish a Toutiao video with Playwright storage_state.")
    parser.add_argument("--input", required=True, help="Path to video publish JSON. Relative paths are resolved from skill root.")
    parser.add_argument("--account", default="default", help="Account alias used under data/accounts/{account}.")
    parser.add_argument("--data-dir", default="")
    parser.add_argument("--state-path", default="")
    parser.add_argument("--run-dir", default="")
    parser.add_argument("--headed", action="store_true", help="Run with a visible browser.")
    parser.add_argument("--browser-channel", default="")
    parser.add_argument("--upload-timeout", type=int, default=900, help="Seconds to wait for video upload/processing.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    account_paths = build_account_paths(args.data_dir, args.account)
    input_path = resolve_path(args.input, account_paths)
    payload = read_json(input_path)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    state_path = Path(args.state_path).expanduser() if args.state_path else default_read_state_path(account_paths)
    run_dir = Path(args.run_dir).expanduser() if args.run_dir else account_paths.runs_dir / f"toutiao-video-{timestamp}"
    run_dir.mkdir(parents=True, exist_ok=True)

    log_file = run_dir / "worker.log"
    with log_file.open("w", encoding="utf-8") as log:
        try:
            result = run_publish(args, payload, state_path, run_dir, account_paths, log)
        except Exception as exc:
            result = {
                "success": False,
                "published": False,
                "platform": "toutiao",
                "type": "video",
                "error_message": str(exc),
                "run_dir": display_path(run_dir),
            }
            write_log(log, f"failed: {exc}")
        write_result(run_dir / "result.json", result)

    print(json.dumps(result, ensure_ascii=False, indent=2), flush=True)
    if not result.get("success"):
        raise SystemExit(1)


def run_publish(args: argparse.Namespace, payload: dict, state_path: Path, run_dir: Path, account_paths, log) -> dict:
    selectors = load_selectors()
    validate_payload(payload, state_path, account_paths)
    title = str(payload["title"]).strip()[:30]
    description = str(payload.get("description", "")).strip()
    publish_mode = str(payload.get("publish_mode", "auto")).strip().lower()
    if publish_mode not in {"auto", "draft"}:
        raise ValueError("publish_mode 只能是 auto 或 draft")

    video_path = resolve_path(str(payload["video"]), account_paths)
    cover_path = resolve_path(str(payload["cover_image"]), account_paths) if payload.get("cover_image") else None
    options = build_options(payload)
    write_log(
        log,
        "platform=toutiao type=video "
        f"account={account_paths.account} mode={publish_mode} "
        f"video={display_path(video_path)} cover={display_path(cover_path) if cover_path else ''}",
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
            open_video_publish(page, selectors, log)
            upload_video(page, video_path, selectors, args.upload_timeout, log)
            fill_title(page, title, selectors, log)
            fill_description(page, description, selectors, log)
            upload_cover(page, cover_path, selectors, log)
            handle_options(page, selectors, options, log)
            take_screenshot(page, run_dir / "before_publish.png")

            published = False
            if publish_mode == "auto":
                click_publish(page, selectors, log)
                page.wait_for_timeout(2500)
                take_screenshot(page, run_dir / "after_publish_click.png")
                confirm_publish_if_needed(page, selectors, log)
                wait_publish_result(page, title, log)
                published = True
            else:
                write_log(log, "draft mode: skipped publish click")

            return {
                "success": True,
                "published": published,
                "platform": "toutiao",
                "type": "video",
                "account": account_paths.account,
                "platform_url": page.url,
                "message": "已自动发布到头条号视频" if published else "已打开并填充视频内容，未点击发布",
                "run_dir": display_path(run_dir),
            }
        except Exception:
            if page is not None:
                take_screenshot(page, run_dir / "failure.png")
            raise
        finally:
            browser.close()


def validate_payload(payload: dict, state_path: Path, account_paths) -> None:
    if not state_path.exists():
        raise ValueError(f"登录态不存在：{state_path}。请先运行 scripts/login.py")
    if not str(payload.get("title", "")).strip():
        raise ValueError("输入 JSON 缺少 title")
    if not str(payload.get("video", "")).strip():
        raise ValueError("输入 JSON 缺少 video")
    video_path = resolve_path(str(payload["video"]), account_paths)
    if not video_path.exists() or not video_path.is_file():
        raise ValueError(f"视频文件不存在：{video_path}")
    if payload.get("cover_image"):
        cover_path = resolve_path(str(payload["cover_image"]), account_paths)
        if not cover_path.exists() or not cover_path.is_file():
            raise ValueError(f"封面文件不存在：{cover_path}")
    options = payload.get("options") or {}
    if not isinstance(options, dict):
        raise ValueError("options 必须是对象")


def build_options(payload: dict) -> dict:
    options = payload.get("options") or {}
    return {
        "ad_revenue": bool(options.get("ad_revenue", True)),
        "video_to_article": bool(options.get("video_to_article", False)),
        "personal_opinion": bool(options.get("personal_opinion", True)),
    }


def open_video_publish(page, selectors: dict, log) -> None:
    page.goto(selectors.get("home_url") or TOUTIAO_HOME_URL, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(4000)
    detect_verification(page)
    if click_selector(page, selector_value(selectors, "video_publish.entry"), log, "video entry", timeout=10000):
        page.wait_for_timeout(4000)
        detect_verification(page)
        return
    if click_first_enabled([
        page.get_by_text("视频", exact=True).last,
        page.locator("a").filter(has_text="视频").last,
    ], log, "video entry fallback", timeout=5000):
        page.wait_for_timeout(4000)
        detect_verification(page)
        return
    raise RuntimeError("未找到头条号视频发布入口")


def upload_video(page, video_path: Path, selectors: dict, upload_timeout: int, log) -> None:
    upload_selector = selector_value(selectors, "video_publish.upload_trigger")
    if upload_selector:
        upload_trigger = locator_from_selector(page, upload_selector)
    else:
        upload_trigger = page.locator(".upload-video-trigger").first
    try:
        with page.expect_file_chooser(timeout=8000) as chooser_info:
            upload_trigger.click(timeout=8000)
        chooser_info.value.set_files(str(video_path))
        write_log(log, f"selected video by file chooser: {display_path(video_path)}")
    except Exception as exc:
        write_log(log, f"video file chooser failed: {exc}")
        file_input = page.locator("input[type='file']").first
        file_input.set_input_files(str(video_path), timeout=15000)
        write_log(log, f"selected video by input: {display_path(video_path)}")
    wait_video_upload_ready(page, selectors, upload_timeout, log)


def wait_video_upload_ready(page, selectors: dict, timeout_seconds: int, log) -> None:
    deadline = time.time() + max(timeout_seconds, 30)
    title_selector = selector_value(selectors, "video_publish.title")
    while time.time() < deadline:
        detect_verification(page)
        text = safe_body_text(page)
        for pattern in FAILURE_PATTERNS:
            if pattern in text:
                raise RuntimeError(f"头条号视频上传失败：{pattern}")
        if title_selector:
            try:
                page.locator(title_selector).first.wait_for(state="visible", timeout=3000)
                write_log(log, "video form is visible after upload")
                return
            except Exception:
                pass
        if any(pattern in text for pattern in ["上传成功", "上传完成", "转码完成", "发布"]):
            write_log(log, "video upload readiness inferred by page text")
            return
        page.wait_for_timeout(3000)
    raise RuntimeError("等待视频上传或转码完成超时")


def fill_title(page, title: str, selectors: dict, log) -> None:
    locators = [
        locator_from_selector(page, selector_value(selectors, "video_publish.title")),
        page.locator("input[placeholder*='标题']").first,
        page.locator("input").first,
    ]
    if fill_first(locators, title, log, "video title"):
        return
    raise RuntimeError("未找到视频标题输入框")


def fill_description(page, description: str, selectors: dict, log) -> None:
    if not description:
        return
    locators = [
        locator_from_selector(page, selector_value(selectors, "video_publish.description")),
        page.locator("textarea[placeholder*='简介']").first,
        page.locator("textarea[placeholder*='描述']").first,
        page.locator("textarea").first,
        page.locator("[contenteditable='true']").last,
    ]
    if fill_first(locators, description, log, "video description", required=False):
        return
    write_log(log, "video description skipped: field unavailable")


def upload_cover(page, cover_path: Path | None, selectors: dict, log) -> None:
    if not cover_path:
        write_log(log, "video cover skipped: cover_image not provided")
        return
    cover = locator_from_selector(page, selector_value(selectors, "video_publish.cover"))
    if cover is None:
        cover = page.locator(".form-item-poster").first
    try:
        with page.expect_file_chooser(timeout=8000) as chooser_info:
            cover.click(timeout=8000)
        chooser_info.value.set_files(str(cover_path))
        page.wait_for_timeout(3000)
        write_log(log, f"uploaded video cover by file chooser: {display_path(cover_path)}")
        return
    except Exception as exc:
        write_log(log, f"video cover file chooser failed: {exc}")
    try:
        cover.click(timeout=5000)
        page.wait_for_timeout(1000)
        file_input = page.locator("input[type='file'][accept*='image']").first
        file_input.set_input_files(str(cover_path), timeout=15000)
        page.wait_for_timeout(3000)
        write_log(log, f"uploaded video cover by input: {display_path(cover_path)}")
    except Exception as exc:
        write_log(log, f"video cover upload skipped/failed: {exc}")


def handle_options(page, selectors: dict, options: dict, log) -> None:
    if options.get("video_to_article"):
        click_selector(page, selector_value(selectors, "video_publish.video_to_article"), log, "视频生成图文", timeout=3000)
    else:
        write_log(log, "skip video option: video_to_article")
    if options.get("personal_opinion"):
        if click_selector(page, selector_value(selectors, "video_publish.work_declaration"), log, "作品声明", timeout=3000):
            page.wait_for_timeout(1000)
            click_personal_opinion(page, log)
    if options.get("ad_revenue"):
        enable_ad_revenue(page, log)


def click_personal_opinion(page, log) -> None:
    locators = [
        page.get_by_text("个人观点，仅供参考", exact=True).last,
        page.locator("label").filter(has_text="个人观点").last,
    ]
    click_first_enabled(locators, log, "video personal opinion", timeout=3000)


def enable_ad_revenue(page, log) -> None:
    blocks = page.locator(".video-form-item, .form-item, .edit-input").filter(has_text="投放广告")
    for index in range(min(blocks.count(), 5)):
        block = blocks.nth(index)
        try:
            block.scroll_into_view_if_needed(timeout=2000)
            radio = block.locator("label").filter(has_text="投放广告").first
            if radio.count() > 0:
                radio.click(timeout=3000)
                write_log(log, "selected video option: 投放广告赚收益")
                return
        except Exception:
            continue
    write_log(log, "video ad revenue option unavailable")


def click_publish(page, selectors: dict, log) -> None:
    locators = [
        locator_from_selector(page, selector_value(selectors, "video_publish.publish")),
        page.get_by_role("button", name="发布").last,
        page.locator("button").filter(has_text="发布").last,
    ]
    if click_first_enabled(locators, log, "video publish button", timeout=8000):
        return
    raise RuntimeError("未找到头条号视频发布按钮")


def confirm_publish_if_needed(page, selectors: dict, log) -> None:
    locators = [
        locator_from_selector(page, selector_value(selectors, "modal.confirm")),
        page.locator(".byte-modal-wrapper .byte-modal-footer button.byte-btn-primary").last,
        page.get_by_text("确认发布", exact=True).last,
        page.get_by_text("确定", exact=True).last,
    ]
    click_first_enabled(locators, log, "video confirm button", timeout=5000)


def wait_publish_result(page, title: str, log) -> None:
    deadline = time.time() + 60
    normalized_title = "".join(title.split())
    while time.time() < deadline:
        detect_verification(page)
        text = safe_body_text(page)
        compact_text = "".join(text.split())
        if any(pattern in text for pattern in SUCCESS_PATTERNS):
            write_log(log, "video publish success detected")
            return
        if normalized_title and normalized_title in compact_text and "作品管理" in text:
            write_log(log, f"video publish success inferred by title: {title}")
            return
        for pattern in FAILURE_PATTERNS:
            if pattern in text:
                raise RuntimeError(f"头条号视频发布失败：{pattern}")
        if page.url and any(part in page.url for part in ["/publish/success", "/manage", "content/manage"]):
            write_log(log, f"video publish success inferred by url: {page.url}")
            return
        page.wait_for_timeout(2000)
    raise RuntimeError("等待视频发布结果超时")


def fill_first(locators, value: str, log, label: str, required: bool = True) -> bool:
    for locator in locators:
        if locator is None:
            continue
        try:
            locator.wait_for(state="visible", timeout=5000)
            locator.scroll_into_view_if_needed(timeout=3000)
            locator.click(timeout=3000)
            try:
                locator.fill(value, timeout=8000)
            except Exception:
                locator.evaluate(
                    """
                    (element, value) => {
                      element.focus();
                      if ('value' in element) {
                        element.value = value;
                      } else {
                        element.textContent = value;
                      }
                      element.dispatchEvent(new InputEvent('input', {
                        bubbles: true,
                        inputType: 'insertText',
                        data: value
                      }));
                      element.dispatchEvent(new Event('change', { bubbles: true }));
                    }
                    """,
                    value,
                )
            write_log(log, f"filled {label}")
            return True
        except Exception as exc:
            write_log(log, f"fill {label} candidate failed: {exc}")
            continue
    if required:
        write_log(log, f"fill {label} failed")
    return False


if __name__ == "__main__":
    main()
