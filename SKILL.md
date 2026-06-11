---
name: toutiao-publisher
description: Use when a coding agent needs to log in to Toutiao Creator, save Playwright storage_state, and publish a Toutiao article or video with Playwright using a JSON input file, including cover upload, article/video filling, publish option handling, preview/confirm publish flow, diagnostics, and anti-risk boundaries. This skill must not bypass verification or publish without explicit user intent.
---

# Toutiao Publisher

## 使用时机

当用户需要 Codex、Hermes 或其他编码 Agent 帮助登录头条号、保存会话并自动发布头条号文章时使用。

这个 Skill 只处理头条号，不包含小红书逻辑。

## 数据目录

默认数据目录跟随 Skill 安装位置：

```text
{skill_root}/data/
```

例如安装在 `/Users/px/.codex/skills/toutiao-publisher` 时，默认数据会保存到：

```text
/Users/px/.codex/skills/toutiao-publisher/data/
```

单账号兼容目录：

- `data/states/toutiao.json`：登录态。
- `data/browser-profile/`：持久化浏览器 profile。
- `data/inputs/`：发布 JSON。
- `data/runs/`：每次发布的日志、截图和结果。
- `data/assets/`：配图等素材。

多账号推荐目录：

- `data/accounts/{account}/states/toutiao.json`
- `data/accounts/{account}/browser-profile/`
- `data/accounts/{account}/inputs/`
- `data/accounts/{account}/assets/`
- `data/accounts/{account}/runs/`
- `data/accounts/{account}/works/`

`{account}` 是用户自定义账号别名，只允许字母、数字、点、下划线和短横线；其他字符会被转换为短横线。

如需自定义位置，可给脚本传 `--data-dir`。

脚本内部使用绝对路径执行，但写入 `result.json` 或终端输出时，凡是位于 Skill 根目录下的路径都会显示为相对路径，例如 `data/accounts/default/runs/...`。

## 登录

```bash
python scripts/login.py --account default
```

可指定官方登录地址：

```bash
python scripts/login.py --account my-toutiao --login-url "https://mp.toutiao.com/"
```

脚本会打开有头浏览器。用户自行完成扫码、短信验证码或账号登录后，回到终端按 Enter 保存 session。

服务器二维码登录：

```bash
python scripts/login.py --account default --qr --headless
```

脚本会保存二维码截图并轮询登录状态：

```text
data/accounts/default/login/login-qr.png
```

用户用手机扫码登录后，脚本自动保存 session。可调整等待时间：

```bash
python scripts/login.py --account default --qr --headless --qr-timeout 300
```

二维码模式只截图登录页面，不读取短信验证码、不绕过验证码、滑块或风控。

## 发布

图文文章：

```bash
python scripts/publish.py --account default --input data/inputs/article.json
```

调试时可有头运行：

```bash
python scripts/publish.py --account my-toutiao --input data/accounts/my-toutiao/inputs/article.json --headed
```

发布前必须确认用户明确要求自动发布。若用户只想填充草稿，输入 JSON 使用 `"publish_mode": "draft"`。

视频：

```bash
python scripts/video.py --account default --input data/accounts/default/inputs/video.json
```

调试时可有头运行：

```bash
python scripts/video.py --account default --input data/accounts/default/inputs/video.json --headed
```

视频发布会上传 `video` 文件、可选上传 `cover_image`，再处理标题、作品声明、视频生成图文、可见范围和发布按钮。若用户只想填充草稿，输入 JSON 使用 `"publish_mode": "draft"`。

## 获取作品数据

```bash
python scripts/works.py --account default
```

默认优先读取 `data/accounts/{account}/states/toutiao.json`，兼容读取旧的 `data/states/toutiao.json`，输出到：

```text
data/accounts/{account}/works/latest.json
```

可调整最多获取数量和正文同步数量：

```bash
python scripts/works.py --account my-toutiao --max-items 200 --sync-content-count 20
```

## Selector 配置

头条号页面定位优先读取：

```text
config/selectors.json
```

如果平台页面结构变化，优先更新这个配置文件。视频发布动作采用严格 selector 模式：入口、上传、标题、封面、作品声明、可见范围和发布按钮只使用配置中的 selector，不做通用文本兜底，避免误点“存草稿”等相邻按钮。

## 输入格式

- 图文文章见 `references/input-format.md`。
- 视频见 `references/video-input-format.md`。

## 页面规则

见 `references/page-rules.md`。

## 诊断

见 `references/diagnostics.md`。

## 安全边界

- 不读取或保存明文密码。
- 不自动读取短信验证码。
- 不绕验证码、滑块、安全验证、风控、登录限制。
- 不在用户未明确确认时点击真实发布按钮。
- 发布后必须读取 `result.json`，不能只根据命令退出码判断。
