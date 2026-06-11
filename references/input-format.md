# 输入格式

发布脚本接收一个 JSON 文件：

```json
{
  "title": "文章标题",
  "cover_image": "data/accounts/default/assets/cover.png",
  "content_blocks": [
    {
      "type": "paragraph",
      "text": "开头段落。"
    },
    {
      "type": "heading",
      "text": "一、分段小标题"
    },
    {
      "type": "paragraph",
      "text": "正文段落。"
    },
    {
      "type": "image",
      "src": "data/accounts/default/assets/body-1.png",
      "caption": "可选图片说明"
    }
  ],
  "publish_mode": "auto",
  "options": {
    "ad_revenue": true,
    "cover_mode": "single",
    "first_publish": false,
    "source_declaration": "personal_opinion",
    "sync_weitoutiao": false
  }
}
```

字段说明：

- `title`：必填，最多填充 80 字。
- `cover_image`：必填，单张封面图，支持相对 Skill 根目录的路径、本地绝对路径或 `http/https` 图片 URL。
- `content_blocks`：必填数组，发布脚本会严格按数组顺序插入正文内容。
- `content_blocks[].type`：支持 `paragraph`、`heading`、`image`。
- `paragraph.text`：正文段落。
- `heading.text`：小标题。脚本按普通文本插入，生成内容时建议自带“一、”“二、”等编号。
- `image.src`：正文图片，支持相对 Skill 根目录的路径、本地绝对路径或 `http/https` 图片 URL。
- `image.caption`：可选，图片说明，会插入到图片下方。
- `publish_mode`：可选，`auto` 或 `draft`，默认为 `auto`。
- `options.ad_revenue`：可选，默认 `true`，选择“投放广告赚收益”。
- `options.cover_mode`：可选，封面模式，支持 `single`、`triple`、`none`；不填时有封面图默认 `single`。
- `options.first_publish`：可选，默认 `false`，不默认声明首发，避免触发作品同步授权弹窗。
- `options.source_declaration`：可选，作品声明，支持 `network`、`internal`、`personal_opinion`、`ai`、`fiction`、`investment`、`health`。
- `options.source_declarations`：可选，作品声明数组；如果同时提供，优先使用数组。
- `options.personal_opinion`：兼容旧字段；未提供 `source_declaration/source_declarations` 且该值为 `true` 时，会选择 `personal_opinion`。
- `options.sync_weitoutiao`：可选，默认 `false`，不默认同步发布微头条。

路径规则：

- 相对路径基于 Skill 根目录解析。
- 多账号默认输入文件建议放在 `data/accounts/{account}/inputs/`。
- 多账号默认素材建议放在 `data/accounts/{account}/assets/`。

安全要求：

- 不要把账号密码、短信验证码、Cookie 明文放入 JSON。
- `publish_mode: "auto"` 会点击真实发布按钮，执行前必须得到用户确认。
