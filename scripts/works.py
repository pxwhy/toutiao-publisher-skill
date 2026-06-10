#!/usr/bin/env python3
"""
实现逻辑：
1. 以当前 Skill 安装目录为根目录，默认读取 data/states/toutiao.json 并输出 data/works/latest.json。
2. 使用 Playwright 打开头条号作品管理页，滚动和翻页提取标题、链接、状态、基础指标与原始文本。
3. 可选同步部分作品正文；遇到登录失效、验证码或风控提示时失败退出，不实现绕过逻辑。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from datetime import UTC, datetime
from pathlib import Path

from playwright.sync_api import sync_playwright

from account_paths import SKILL_ROOT, build_account_paths, default_read_state_path, display_path

DEFAULT_WORK_URLS = [
    "https://mp.toutiao.com/profile_v4/manage/content/all",
    "https://mp.toutiao.com/profile_v4/content/manage",
    "https://mp.toutiao.com/",
]
NAVIGATION_TITLES = {
    "全部",
    "文章",
    "作品管理",
    "收益数据",
    "功能实验室",
    "西瓜视频",
    "微头条",
    "问答",
    "草稿箱",
    "状态",
    "创作权益",
}
VERIFICATION_PATTERNS = ["验证码", "滑块", "安全验证", "环境异常", "操作频繁", "登录已失效"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch Toutiao account works with Playwright storage_state.")
    parser.add_argument("--account", default="default", help="Account alias used under data/accounts/{account}.")
    parser.add_argument("--data-dir", default="")
    parser.add_argument("--state-path", default="")
    parser.add_argument("--result-file", default="")
    parser.add_argument("--max-items", type=int, default=200)
    parser.add_argument("--sync-content-count", type=int, default=20)
    parser.add_argument("--headed", action="store_true")
    parser.add_argument("--browser-channel", default="")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    account_paths = build_account_paths(args.data_dir, args.account)
    state_path = Path(args.state_path).expanduser() if args.state_path else default_read_state_path(account_paths)
    result_file = Path(args.result_file).expanduser() if args.result_file else account_paths.works_dir / "latest.json"
    result_file.parent.mkdir(parents=True, exist_ok=True)

    try:
            result = run_fetch(args, state_path, result_file, account_paths.account)
    except Exception as exc:
        result = {
            "success": False,
            "platform": "toutiao",
            "account": account_paths.account,
            "error_message": str(exc),
            "result_file": display_path(result_file),
        }
    write_result(result_file, result)
    print(json.dumps(result, ensure_ascii=False, indent=2), flush=True)
    if not result.get("success"):
        raise SystemExit(1)


def run_fetch(args: argparse.Namespace, state_path: Path, result_file: Path, account: str) -> dict:
    if not state_path.exists():
        raise ValueError(f"登录态不存在：{state_path}。请先运行 scripts/login.py")

    with sync_playwright() as playwright:
        launch_options = {
            "headless": not args.headed,
            "args": ["--disable-blink-features=AutomationControlled"],
        }
        if args.browser_channel:
            launch_options["channel"] = args.browser_channel
        browser = playwright.chromium.launch(**launch_options)
        context = browser.new_context(storage_state=str(state_path), viewport={"width": 1440, "height": 900})
        try:
            page = context.new_page()
            works = open_and_extract_all_works(page, args.max_items)
            fill_work_contents(context, works, args.sync_content_count)
            return {
                "success": True,
                "platform": "toutiao",
                "account": account,
                "works": works,
                "total_count": len(works),
                "message": f"已获取 {len(works)} 条头条号作品",
                "synced_at": datetime.now(UTC).isoformat(),
                "result_file": display_path(result_file),
            }
        finally:
            context.close()
            browser.close()


def open_and_extract_all_works(page, max_items: int) -> list[dict]:
    last_error = ""
    for url in DEFAULT_WORK_URLS:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            page.wait_for_timeout(3500)
            detect_verification(page)
            click_content_manage_if_needed(page)
            works = collect_works_with_scroll_and_pages(page, max_items)
            if works:
                return works
        except Exception as exc:
            last_error = str(exc)
    if last_error:
        raise RuntimeError(f"未能从头条号作品管理页提取作品：{last_error}")
    raise RuntimeError("未能从头条号作品管理页提取作品")


def click_content_manage_if_needed(page) -> None:
    for text in ["内容管理", "作品管理", "全部作品"]:
        try:
            page.get_by_text(text, exact=True).first.click(timeout=3000)
            page.wait_for_timeout(2500)
            return
        except Exception:
            continue


def collect_works_with_scroll_and_pages(page, max_items: int) -> list[dict]:
    collected: list[dict] = []
    seen = set()
    for _page_index in range(20):
        for _scroll_index in range(8):
            merge_works(collected, seen, extract_works(page), max_items)
            if len(collected) >= max_items:
                return collected
            page.mouse.wheel(0, 1400)
            page.wait_for_timeout(1200)
        if not click_next_page(page):
            break
        page.wait_for_timeout(3000)
    return collected


def merge_works(collected: list[dict], seen: set, works: list[dict], max_items: int) -> None:
    for work in works:
        key = work.get("platform_work_id") or work.get("url") or work.get("title")
        if not key or key in seen:
            continue
        seen.add(key)
        collected.append(work)
        if len(collected) >= max_items:
            return


def click_next_page(page) -> bool:
    candidates = [
        page.get_by_text("下一页", exact=False).last,
        page.locator("button").filter(has_text="下一页").last,
        page.locator(".byte-pagination-next").last,
        page.locator("[aria-label*='下一页']").last,
    ]
    for locator in candidates:
        try:
            locator.wait_for(state="visible", timeout=2000)
            class_name = locator.get_attribute("class", timeout=1000) or ""
            if "disabled" in class_name:
                continue
            if locator.is_enabled(timeout=1000):
                locator.click(timeout=3000)
                return True
        except Exception:
            continue
    return False


def extract_works(page) -> list[dict]:
    works = page.evaluate(
        """
        () => {
          const normalize = (text) => (text || '').replace(/\\s+/g, ' ').trim();
          const metricValue = (text, labels) => {
            for (const label of labels) {
              const pattern = new RegExp(label + '\\\\s*[:：]?\\\\s*([0-9,.万kK+-]+)');
              const match = text.match(pattern);
              if (match) return match[1];
            }
            return '';
          };
          const titleFromNode = (node, link) => {
            const titleNode = node.querySelector('[class*=title], [class*=Title], h3, h4');
            const title = normalize(titleNode?.innerText || titleNode?.textContent);
            if (title) return title;
            return normalize(link?.innerText || link?.textContent).slice(0, 120);
          };
          const statusFromText = (text) => {
            const statuses = ['已发布', '审核中', '未通过', '仅我可见', '草稿', '推荐中'];
            return statuses.find((item) => text.includes(item)) || '';
          };
          const ignoredTitles = new Set(['全部', '文章', '作品管理', '收益数据', '功能实验室', '西瓜视频', '微头条', '问答', '草稿箱', '状态', '创作权益']);
          const items = [];
          const seen = new Set();
          const containers = Array.from(document.querySelectorAll(
            '.byte-table-row, [class*=article], [class*=Article], [class*=content], [class*=Content], [class*=work], [class*=Work], li'
          ));
          for (const node of containers) {
            const text = normalize(node.innerText || node.textContent);
            if (!text || text.length < 4) continue;
            const link = Array.from(node.querySelectorAll('a[href]')).find((item) => {
              const href = item.href || '';
              return href.includes('toutiao.com') || href.includes('mp.toutiao.com');
            });
            const title = titleFromNode(node, link);
            const url = link?.href || '';
            if (!title || ignoredTitles.has(title) || !url || !/^https?:\\/\\//.test(url)) continue;
            const metrics = {
              views: metricValue(text, ['阅读', '展现', '播放']),
              likes: metricValue(text, ['点赞', '赞']),
              comments: metricValue(text, ['评论']),
              favorites: metricValue(text, ['收藏']),
              shares: metricValue(text, ['分享']),
              revenue: metricValue(text, ['收益'])
            };
            const status = statusFromText(text);
            const key = workIdFromUrl(url) || url || title;
            if (seen.has(key)) continue;
            seen.add(key);
            items.push({
              platform_work_id: key,
              title,
              url,
              status,
              metrics,
              raw: { text }
            });
          }
          return items;

          function workIdFromUrl(url) {
            if (!url) return '';
            const matches = url.match(/\\d{8,}/g);
            if (matches && matches.length) return matches[matches.length - 1];
            try {
              const parsed = new URL(url);
              const parts = parsed.pathname.split('/').filter(Boolean);
              return parts[parts.length - 1] || url;
            } catch {
              return url;
            }
          }
        }
        """
    )
    return dedupe_works(works)


def dedupe_works(works: list[dict]) -> list[dict]:
    cleaned = []
    seen = set()
    for item in works:
        title = (item.get("title") or "").strip()
        url = (item.get("url") or "").strip()
        platform_work_id = (item.get("platform_work_id") or work_id_from_url(url) or title).strip()
        item["metrics"] = normalize_metrics(item.get("metrics") or {})
        if not is_valid_work(title=title, url=url):
            continue
        key = platform_work_id or url or title
        if key in seen:
            continue
        seen.add(key)
        item["platform_work_id"] = platform_work_id
        item["title"] = title
        item["content"] = (item.get("content") or "").strip()
        item["url"] = url
        cleaned.append(item)
    return cleaned


def fill_work_contents(context, works: list[dict], max_count: int) -> None:
    if max_count <= 0:
        return
    detail_page = context.new_page()
    try:
        synced = 0
        for work in works:
            if synced >= max_count:
                break
            url = work.get("url") or ""
            if not url or work.get("content"):
                continue
            try:
                detail_page.goto(url, wait_until="domcontentloaded", timeout=45000)
                detail_page.wait_for_timeout(2500)
                content = extract_work_content(detail_page, work.get("title") or "")
                if content:
                    work["content"] = content
                    synced += 1
            except Exception:
                continue
    finally:
        detail_page.close()


def extract_work_content(page, title: str) -> str:
    content = page.evaluate(
        """
        (title) => {
          const normalize = (text) => (text || '').replace(/\\u00a0/g, ' ').replace(/[ \\t]+/g, ' ').replace(/\\n{3,}/g, '\\n\\n').trim();
          const selectors = ['article', '[class*=article-content]', '[class*=ArticleContent]', '[class*=content-detail]', '[class*=ContentDetail]', '[class*=detail-content]', '[class*=syl-page-article]', '[class*=ProseMirror]', 'main'];
          const candidates = [];
          for (const selector of selectors) {
            for (const node of Array.from(document.querySelectorAll(selector))) {
              const text = normalize(node.innerText || node.textContent);
              if (text.length >= 20) candidates.push(text);
            }
          }
          if (!candidates.length) {
            const paragraphs = Array.from(document.querySelectorAll('p')).map((node) => normalize(node.innerText || node.textContent)).filter(Boolean);
            if (paragraphs.length) candidates.push(paragraphs.join('\\n'));
          }
          candidates.sort((a, b) => b.length - a.length);
          const best = candidates[0] || '';
          return best.startsWith(title) ? best.slice(title.length).trim() : best;
        }
        """,
        title,
    )
    return content[:20000]


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


def is_valid_work(title: str, url: str) -> bool:
    if not title or title in NAVIGATION_TITLES:
        return False
    return url.startswith(("http://", "https://"))


def normalize_metrics(metrics: dict) -> dict:
    return {key: parse_number(value) for key, value in metrics.items() if value not in {"", None}}


def parse_number(value) -> int | float | str:
    text = str(value).replace(",", "").strip()
    if not text:
        return ""
    multiplier = 1
    if text.lower().endswith("k"):
        multiplier = 1000
        text = text[:-1]
    if text.endswith("万"):
        multiplier = 10000
        text = text[:-1]
    try:
        number = float(text)
    except ValueError:
        return value
    value = number * multiplier
    return int(value) if value.is_integer() else value


def work_id_from_url(url: str) -> str:
    if not url:
        return ""
    matches = re.findall(r"\\d{8,}", url)
    if matches:
        return matches[-1]
    return url.rstrip("/").split("/")[-1]


def write_result(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("用户中断", file=sys.stderr)
        raise SystemExit(130)
