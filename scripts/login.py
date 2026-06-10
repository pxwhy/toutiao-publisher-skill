#!/usr/bin/env python3
"""
实现逻辑：
1. 以当前脚本所在 Skill 目录为根目录，默认把登录态、浏览器 profile 保存到 skill_root/data。
2. 打开头条号官方登录页，用户在有头浏览器中自行完成扫码、短信验证码或账号登录。
3. 用户确认登录完成后保存 Playwright storage_state；脚本不读取密码、不绕过验证。
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from playwright.sync_api import sync_playwright

from account_paths import SKILL_ROOT, build_account_paths, display_path


DEFAULT_LOGIN_URL = "https://mp.toutiao.com/"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Login to Toutiao Creator and save Playwright storage_state.")
    parser.add_argument("--login-url", default=DEFAULT_LOGIN_URL)
    parser.add_argument("--account", default="default", help="Account alias used under data/accounts/{account}.")
    parser.add_argument("--data-dir", default="")
    parser.add_argument("--state-path", default="")
    parser.add_argument("--user-data-dir", default="")
    parser.add_argument("--browser-channel", default="chrome")
    parser.add_argument("--timeout-ms", type=int, default=0)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    account_paths = build_account_paths(args.data_dir, args.account)
    state_path = Path(args.state_path).expanduser() if args.state_path else account_paths.state_path
    user_data_dir = Path(args.user_data_dir).expanduser() if args.user_data_dir else account_paths.browser_profile_dir
    state_path.parent.mkdir(parents=True, exist_ok=True)
    user_data_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as playwright:
        context = playwright.chromium.launch_persistent_context(
            user_data_dir=str(user_data_dir),
            channel=args.browser_channel or None,
            headless=False,
            viewport={"width": 1440, "height": 900},
            args=["--disable-blink-features=AutomationControlled"],
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(args.login_url, wait_until="domcontentloaded", timeout=60000)
        print(f"已打开头条号登录页：{args.login_url}", flush=True)
        print(f"Skill 根目录：{SKILL_ROOT}", flush=True)
        print(f"账号别名：{account_paths.account}", flush=True)
        print(f"账号数据目录：{account_paths.account_dir}", flush=True)
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
        "message": "头条号登录态已保存。请妥善保管 data 目录，不要公开分享。",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2), flush=True)

if __name__ == "__main__":
    main()
