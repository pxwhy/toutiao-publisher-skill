# Toutiao Publisher Skill

用于 Codex、Hermes 或其他编码 Agent 的头条号自动发布 Skill。

## 能力

- 打开头条号登录页，由用户自行扫码、验证码或账号登录。
- 使用 Playwright `storage_state` 保存登录态。
- 按结构化 `content_blocks` 排版文章正文。
- 上传正文图片和独立封面图。
- 上传头条号视频和视频封面图。
- 处理视频生成图文、作品声明、可见范围等发布选项。
- 视频发布动作使用 `config/selectors.json` 中记录的严格 selector，不做通用文本兜底。
- 发布失败时保留日志、截图和 `result.json`。
- 支持多账号数据目录。

## 安全边界

- 不保存明文密码。
- 不自动读取短信验证码。
- 不绕验证码、滑块、安全验证或风控。
- 未获得用户明确发布指令时，不点击真实发布按钮。
- `data/` 目录包含账号状态、草稿、素材和运行日志，默认不会提交到 Git。

## 使用

登录：

```bash
python scripts/login.py --account default
```

服务器二维码登录：

```bash
python scripts/login.py --account default --qr --headless
```

二维码截图默认输出到：

```text
data/accounts/default/login/login-qr.png
```

扫码成功后脚本会自动保存登录态。等待时间可通过 `--qr-timeout` 调整。

发布：

```bash
python scripts/publish.py --account default --input data/accounts/default/inputs/article.json
```

视频发布：

```bash
python scripts/video.py --account default --input data/accounts/default/inputs/video.json
```

获取作品数据：

```bash
python scripts/works.py --account default
```

输入格式见：

```text
references/input-format.md
references/video-input-format.md
```
