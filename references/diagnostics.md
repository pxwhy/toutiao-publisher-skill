# 诊断约定

每次发布创建独立 run 目录：

```text
data/accounts/{account}/runs/toutiao-{timestamp}/
```

目录内容：

- `worker.log`：运行日志。
- `result.json`：结构化结果。
- `before_publish.png`：点击发布前截图。
- `after_first_publish_click.png`：点击第一阶段按钮后截图。
- `after_confirm_publish_click.png`：点击确认或授权按钮后截图。
- `failure.png`：失败时截图。
- `images/`：发布过程使用的临时图片。

成功结果示例：

```json
{
  "success": true,
  "published": true,
  "platform": "toutiao",
  "platform_url": "https://mp.toutiao.com/...",
  "message": "已自动发布到头条号",
  "run_dir": "/path/to/toutiao-publisher/data/runs/toutiao-20260610-120000"
}
```

失败结果示例：

```json
{
  "success": false,
  "published": false,
  "platform": "toutiao",
  "error_message": "等待发布结果超时",
  "run_dir": "/path/to/toutiao-publisher/data/runs/toutiao-20260610-120000"
}
```

Agent 回复用户时必须基于 `result.json` 和 `worker.log`。

路径显示规则：

- 文件实际存储在 Skill 安装目录下。
- `result.json` 中的 `run_dir`、`result_file`、`state_path` 等字段尽量使用相对 Skill 根目录的路径。
- 如果用户显式传入 Skill 目录外的 `--data-dir`、`--state-path` 或 `--run-dir`，输出会保留绝对路径。

## 作品数据

`scripts/works.py` 默认输出：

```text
data/accounts/{account}/works/latest.json
```

结构：

```json
{
  "success": true,
  "platform": "toutiao",
  "works": [
    {
      "platform_work_id": "...",
      "title": "...",
      "url": "...",
      "status": "已发布",
      "metrics": {
        "views": 0,
        "likes": 0,
        "comments": 0
      },
      "content": "..."
    }
  ],
  "total_count": 1
}
```
