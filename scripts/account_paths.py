"""
实现逻辑：
1. 统一头条号 Skill 的多账号数据路径，所有默认路径都跟随 Skill 安装目录。
2. 使用 account 别名隔离登录态、浏览器 profile、发布输入、作品数据和运行诊断。
3. 兼容早期单账号 data/states/toutiao.json，方便用户平滑迁移。
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class AccountPaths:
    account: str
    data_dir: Path
    account_dir: Path
    state_path: Path
    legacy_state_path: Path
    browser_profile_dir: Path
    inputs_dir: Path
    assets_dir: Path
    runs_dir: Path
    works_dir: Path


def build_account_paths(data_dir_value: str = "", account_value: str = "default") -> AccountPaths:
    data_dir = resolve_data_dir(data_dir_value)
    account = normalize_account(account_value)
    account_dir = data_dir / "accounts" / account
    return AccountPaths(
        account=account,
        data_dir=data_dir,
        account_dir=account_dir,
        state_path=account_dir / "states" / "toutiao.json",
        legacy_state_path=data_dir / "states" / "toutiao.json",
        browser_profile_dir=account_dir / "browser-profile",
        inputs_dir=account_dir / "inputs",
        assets_dir=account_dir / "assets",
        runs_dir=account_dir / "runs",
        works_dir=account_dir / "works",
    )


def resolve_data_dir(value: str) -> Path:
    if value:
        return Path(value).expanduser().resolve()
    return SKILL_ROOT / "data"


def normalize_account(value: str) -> str:
    text = str(value or "default").strip()
    text = re.sub(r"[^a-zA-Z0-9._-]+", "-", text).strip(".-_")
    return text or "default"


def default_read_state_path(paths: AccountPaths) -> Path:
    if paths.state_path.exists():
        return paths.state_path
    return paths.legacy_state_path


def display_path(path: Path | str) -> str:
    resolved = Path(path).expanduser().resolve()
    try:
        return str(resolved.relative_to(SKILL_ROOT))
    except ValueError:
        return str(resolved)
