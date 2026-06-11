# 视频输入格式

视频发布脚本接收一个 JSON 文件：

```json
{
  "title": "视频标题",
  "description": "视频简介，可选",
  "video": "data/accounts/default/assets/video.mp4",
  "cover_image": "data/accounts/default/assets/cover.png",
  "publish_mode": "auto",
  "options": {
    "ad_revenue": true,
    "video_to_article": false,
    "personal_opinion": true
  }
}
```

字段说明：

- `title`：必填，视频标题，脚本最多填充 30 字。
- `description`：可选，视频简介或补充说明。
- `video`：必填，视频文件路径，支持相对 Skill 根目录路径或本地绝对路径。
- `cover_image`：可选，封面图片路径，支持相对 Skill 根目录路径或本地绝对路径。
- `publish_mode`：可选，`auto` 或 `draft`，默认为 `auto`。
- `options.ad_revenue`：可选，默认 `true`，尽量选择“投放广告赚收益”。
- `options.video_to_article`：可选，默认 `false`，不默认开启“视频生成图文”。
- `options.personal_opinion`：可选，默认 `true`，尽量选择“个人观点，仅供参考”。

路径规则：

- 相对路径基于 Skill 根目录解析。
- 多账号默认输入文件建议放在 `data/accounts/{account}/inputs/`。
- 多账号默认素材建议放在 `data/accounts/{account}/assets/`。

安全要求：

- `publish_mode: "auto"` 会点击真实发布按钮，执行前必须得到用户确认。
- 不要上传违规、侵权或无授权的视频素材。
- 不要把账号密码、短信验证码、Cookie 明文放入 JSON。
