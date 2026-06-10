#!/usr/bin/env python3
"""
实现逻辑：
1. 以当前脚本所在 Skill 目录为根目录，默认把登录态、浏览器 profile 保存到 skill_root/data。
2. 普通模式打开有头浏览器，用户自行完成扫码、短信验证码或账号登录后按 Enter 保存 session。
3. 二维码模式截图登录页二维码，用户扫码后脚本轮询登录状态并自动保存 session；脚本不读取密码、不绕过验证。
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError, sync_playwright

from account_paths import SKILL_ROOT, build_account_paths, display_path


DEFAULT_LOGIN_URL = "https://mp.toutiao.com/"
VERIFICATION_PATTERNS = ["验证码", "滑块", "安全验证", "环境异常", "操作频繁", "登录已失效"]
LOGIN_SUCCESS_PATTERNS = ["发布", "创作", "作品管理", "头条号发文规范", "首页", "消息"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Login to Toutiao Creator and save Playwright storage_state.")
    parser.add_argument("--login-url", default=DEFAULT_LOGIN_URL)
    parser.add_argument("--account", default="default", help="Account alias used under data/accounts/{account}.")
    parser.add_argument("--data-dir", default="")
    parser.add_argument("--state-path", default="")
    parser.add_argument("--user-data-dir", default="")
    parser.add_argument("--browser-channel", default="chrome")
    parser.add_argument("--timeout-ms", type=int, default=0)
    parser.add_argument("--qr", action="store_true", help="Save a login QR screenshot and wait until the user scans it.")
    parser.add_argument("--qr-timeout", type=int, default=180, help="Seconds to wait for QR login.")
    parser.add_argument("--headless", action="store_true", help="Run browser without a visible window. Useful on servers.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    account_paths = build_account_paths(args.data_dir, args.account)
    state_path = Path(args.state_path).expanduser() if args.state_path else account_paths.state_path
    user_data_dir = Path(args.user_data_dir).expanduser() if args.user_data_dir else account_paths.browser_profile_dir
    state_path.parent.mkdir(parents=True, exist_ok=True)
    user_data_dir.mkdir(parents=True, exist_ok=True)
    login_dir = account_paths.account_dir / "login"
    login_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as playwright:
        context = playwright.chromium.launch_persistent_context(
            user_data_dir=str(user_data_dir),
            channel=args.browser_channel or None,
            headless=args.headless,
            viewport={"width": 1440, "height": 900},
            args=["--disable-blink-features=AutomationControlled"],
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(args.login_url, wait_until="domcontentloaded", timeout=60000)
        print(f"已打开头条号登录页：{args.login_url}", flush=True)
        print(f"Skill 根目录：{SKILL_ROOT}", flush=True)
        print(f"账号别名：{account_paths.account}", flush=True)
        print(f"账号数据目录：{account_paths.account_dir}", flush=True)
        if args.qr:
            qr_path = save_login_qr(page, login_dir)
            print(f"二维码截图：{display_path(qr_path)}", flush=True)
            print(f"请扫码登录，最多等待 {args.qr_timeout} 秒。", flush=True)
            wait_for_login(page, args.qr_timeout, login_dir)
        else:
            print("请在浏览器中自行完成登录。完成后回到终端按 Enter 保存 session。", flush=True)
            if args.timeout_ms > 0:
                page.wait_for_timeout(args.timeout_ms)
            else:
                input()
        context.storage_state(path=str(state_path))
        context.close()

    result = {
        "success": True,
        "platform": "toutiao",
        "account": account_paths.account,
        "state_path": display_path(state_path),
        "user_data_dir": display_path(user_data_dir),
        "login_dir": display_path(login_dir),
        "message": "头条号登录态已保存。请妥善保管 data 目录，不要公开分享。",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2), flush=True)


def save_login_qr(page, login_dir: Path) -> Path:
    page.wait_for_timeout(4000)
    qr_path = login_dir / "login-qr.png"
    candidates = [
        "img[src*='qr']",
        "canvas",
        "[class*='qr'] img",
        "[class*='qrcode'] img",
        "[class*='scan'] img",
        "[class*='login'] img",
    ]
    for selector in candidates:
        try:
            locator = page.locator(selector).first
            locator.wait_for(state="visible", timeout=2500)
            locator.screenshot(path=str(qr_path), timeout=5000)
            return qr_path
        except Exception:
            continue
    page.screenshot(path=str(qr_path), full_page=True, timeout=8000)
    return qr_path


def wait_for_login(page, timeout_seconds: int, login_dir: Path) -> None:
    deadline = time.time() + max(timeout_seconds, 1)
    last_screenshot = login_dir / "login-waiting.png"
    while time.time() < deadline:
        detect_verification(page)
        if is_logged_in(page):
            return
        try:
            page.screenshot(path=str(last_screenshot), full_page=True, timeout=5000)
        except Exception:
            pass
        page.wait_for_timeout(2000)
    raise RuntimeError(f"等待扫码登录超时，请重新运行。最后截图：{display_path(last_screenshot)}")


def is_logged_in(page) -> bool:
    text = safe_body_text(page)
    if any(pattern in text for pattern in LOGIN_SUCCESS_PATTERNS) and "扫码登录" not in text:
        return True
    url = page.url or ""
    if "profile_v4" in url and "login" not in url and "passport" not in url and "sso" not in url:
        return True
    return False


def detect_verification(page) -> None:
    text = safe_body_text(page)
    for pattern in VERIFICATION_PATTERNS:
        if pattern in text:
            raise RuntimeError(f"出现登录、验证或风控提示：{pattern}")


def safe_body_text(page) -> str:
    try:
        return page.locator("body").inner_text(timeout=3000)
    except (PlaywrightTimeoutError, Exception):
        return ""


if __name__ == "__main__":
    main()
