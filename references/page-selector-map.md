# 头条号页面 Selector 采集

- 生成时间：20260611-131110
- 账号：default
- 运行目录：`data/accounts/default/runs/selector-audit-20260611-131110`
- 安全边界：未点击真实发布、删除、撤回等危险动作。

## 命名功能点

### home

| 功能点 | selector | visible | count | text |
|---|---|---:|---:|---|
| `logo` | `.shead_logo` | True | 1 | 头条号 |
| `message` | `.sys-msg-entity` | True | 1 | 消息 |
| `avatar` | `.user-avatar, .account-avatar, img[class*='avatar']` | False | 0 |  |
| `creation_menu` | `.base_creation_tab` | True | 1 | 创作 文章 视频 微头条 音频 |
| `management_menu` | `.management_tab` | True | 1 | 管理 作品管理 评论管理 草稿箱 |
| `article_publish_entry` | `a[href*='graphic/publish']` | True | 1 | 文章 |
| `video_publish_entry` | `#masterRoot > div > div.pgc-content > section > aside > div > div > div > div.byte-menu-inline.base_creation_tab > div.byte-menu-inline-content > div:nth-child(2) > span > a` | True | 1 | 视频 |
| `work_management_entry` | `#masterRoot > div > div.pgc-content > section > aside > div > div > div > div.byte-menu-inline.management_tab > div.byte-menu-inline-content > div.byte-menu-item.selected > span > a > span` | False | 0 |  |

### article_publish

| 功能点 | selector | visible | count | text |
|---|---|---:|---:|---|
| `title` | `#root > div > div.left-column > div > div.publish-editor > div.publish-editor-title-wrapper > div > div > div.title-wrapper > div > div > div > textarea` | True | 1 |  |
| `content` | `#root > div > div.left-column > div > div.publish-editor > div.syl-editor-wrap > div > div.ProseMirror > p > span` | True | 1 | 请输入正文 |
| `cover_single` | `#root > div > div.left-column > div > div.form-wrap > div.form-container > div:nth-child(1) > div > div.edit-input > div > div.byte-radio-group.byte-radio-size-default.byte-radio-mode-outline.pgc-radio.article-cover-radio-group > label:nth-child(1) > span` | True | 1 | 单图 |
| `cover_triple` | `#root > div > div.left-column > div > div.form-wrap > div.form-container > div:nth-child(1) > div > div.edit-input > div > div.byte-radio-group.byte-radio-size-default.byte-radio-mode-outline.pgc-radio.article-cover-radio-group > label:nth-child(2) > span` | True | 1 | 三图 |
| `cover_none` | `#root > div > div.left-column > div > div.form-wrap > div.form-container > div:nth-child(1) > div > div.edit-input > div > div.byte-radio-group.byte-radio-size-default.byte-radio-mode-outline.pgc-radio.article-cover-radio-group > label:nth-child(3) > span` | True | 1 | 无封面 |
| `cover_upload` | `#root > div > div.left-column > div > div.form-wrap > div.form-container > div:nth-child(1) > div > div.edit-input > div > div.article-cover-images-wrap > div.article-cover-images > div > div > div > div` | True | 1 |  |
| `ad_enable_revenue` | `#root > div > div.left-column > div > div.form-wrap > div.form-container > div.pgc-edit-cell.edit-cell.required > div.edit-input > div > span > label > span` | True | 1 | 投放广告赚收益 |
| `ad_disable` | `#root > div > div.left-column > div > div.form-wrap > div.form-container > div.pgc-edit-cell.edit-cell.required > div.edit-input > div > label > span` | True | 1 | 不投放广告 |
| `first_publish` | `#root > div > div.left-column > div > div.form-wrap > div.form-container > div:nth-child(4) > div.edit-input > div > div.exclusive-checkbox-wraper > label > span` | True | 1 | 头条首发 |
| `sync_weitoutiao` | `#root > div > div.left-column > div > div.form-wrap > div.form-container > div.form-item > div > div.edit-input > span > label` | True | 1 | 发布得更多收益 |
| `work_declaration` | `#root > div > div.left-column > div > div.form-wrap > div.form-container > div.source-wrap > div > div.edit-input > div > div` | True | 1 | 取材网络引用站内个人观点，仅供参考引用AI虚构演绎，故事经历投资观点，仅供参考健康医疗分享，仅供参考 |
| `preview_and_publish` | `#root > div > div.left-column > div > div.publish-footer.inline-editor > div > button.byte-btn.byte-btn-primary.byte-btn-size-large.byte-btn-shape-square.publish-btn.publish-btn-last` | True | 1 | 预览并发布 |
| `confirm_publish` | `#root > div > div.left-column > div > div.publish-footer.inline-editor > div > button.byte-btn.byte-btn-primary.byte-btn-size-large.byte-btn-shape-square.publish-btn.publish-btn-last` | True | 1 | 预览并发布 |

### work_management

| 功能点 | selector | visible | count | text |
|---|---|---:|---:|---|
| `entry` | `#masterRoot > div > div.pgc-content > section > aside > div > div > div > div.byte-menu-inline.management_tab > div.byte-menu-inline-content > div.byte-menu-item.selected > span > a > span` | False | 0 |  |
| `tab_all` | `#masterRoot > div > div.pgc-content > section > main > div.work-manage-header.menu-tab-wrapper.sticky > div > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default > div > div > div.byte-tabs-header-title.active` | False | 0 |  |
| `tab_article` | `#masterRoot > div > div.pgc-content > section > main > div.work-manage-header.menu-tab-wrapper.sticky > div > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default > div > div > div:nth-child(2)` | False | 0 |  |
| `tab_video` | `#masterRoot > div > div.pgc-content > section > main > div.work-manage-header.menu-tab-wrapper.sticky > div > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default > div > div > div:nth-child(3)` | False | 0 |  |
| `tab_weitoutiao` | `#masterRoot > div > div.pgc-content > section > main > div.work-manage-header.menu-tab-wrapper.sticky > div > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default > div > div > div:nth-child(4)` | False | 0 |  |
| `tab_short_video` | `#masterRoot > div > div.pgc-content > section > main > div.work-manage-header.menu-tab-wrapper.sticky > div > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default > div > div > div.byte-tabs-header-title.active > span` | False | 0 |  |
| `tab_audio` | `#masterRoot > div > div.pgc-content > section > main > div.work-manage-header.menu-tab-wrapper.sticky > div > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default > div > div > div:nth-child(6)` | False | 0 |  |
| `tab_collection` | `#masterRoot > div > div.pgc-content > section > main > div.work-manage-header.menu-tab-wrapper.sticky > div > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default > div > div > div:nth-child(7) > span` | False | 0 |  |
| `tab_draft` | `#masterRoot > div > div.pgc-content > section > main > div.work-manage-header.menu-tab-wrapper.sticky > div > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default > div > div > div.byte-tabs-header-title.active > span > span` | False | 0 |  |
| `status_all` | `#root > div > div.filter-wrapper > div.filter-field.status-filter-list > span.filter-item.selected` | False | 0 |  |
| `status_published` | `#root > div > div.filter-wrapper > div.filter-field.status-filter-list > span:nth-child(3)` | False | 0 |  |
| `status_reviewing` | `#root > div > div.filter-wrapper > div.filter-field.status-filter-list > span:nth-child(4)` | False | 0 |  |
| `status_rejected` | `#root > div > div.filter-wrapper > div.filter-field.status-filter-list > span:nth-child(5)` | False | 0 |  |
| `status_private` | `#root > div > div.filter-wrapper > div.filter-field.status-filter-list > span:nth-child(6)` | False | 0 |  |
| `list_root` | `#root` | True | 1 | 粉丝数 43  昨日无变化  总阅读(播放)量 164,527  昨日 22  累计收益 11.37元  昨日 0.03  06-10 16:44 发布了微头条 程序员用AI，已经从尝鲜变成日常了 27 展现量 0 阅读量 0 评论 0 点 |
| `work_card` | `.work-card, .content-card, [class*='work'] [class*='card']` | False | 0 |  |
| `pagination` | `.byte-pagination, .pagination, [class*='pagination']` | False | 0 |  |

### video_publish_initial

| 功能点 | selector | visible | count | text |
|---|---|---:|---:|---|
| `entry` | `#masterRoot > div > div.pgc-content > section > aside > div > div > div > div.byte-menu-inline.base_creation_tab > div.byte-menu-inline-content > div:nth-child(2) > span > a` | False | 0 |  |
| `upload_trigger` | `#root > div > div > div.byte-tabs-content.byte-tabs-content-horizontal > div > div.byte-tabs-content-item.byte-tabs-content-item-active > div > div > div > div.upload-video-trigger > div > div > div > div > div > div` | True | 1 | 点击上传或将文件拖入此区域 正常预计审核完成时间：1 小时内 |
| `video_file_input` | `input[type='file'][accept*='video']` | False | 1 |  |

### video_publish_form

| 功能点 | selector | visible | count | text |
|---|---|---:|---:|---|
| `title` | `.form-item-title input[placeholder='请输入 1～30 个字符']` | True | 1 |  |
| `topic` | `.arco-input-tag-input` | True | 1 |  |
| `description` | `.form-item-abstract textarea[placeholder='请输入视频简介']` | True | 1 |  |
| `cover_trigger` | `.form-item-poster .trigger-tip` | True | 1 | 上传封面 |
| `video_to_article_checkbox` | `.form-item-video2art label.byte-checkbox` | True | 1 | 生成图文 |
| `benefit` | `.form-item-benefit` | True | 1 | 创作收益 开通头条视频创作权益，发布横版视频可获得创作收益 |
| `collection` | `.form-item-collection` | True | 1 | 合集 选择合集 |
| `stickers` | `.form-item-stickers` | True | 1 | 互动贴纸 添加贴纸 在视频中添加互动贴纸，可以获得更多的关注、点赞 |
| `source` | `.form-item-source` | True | 1 | 作品声明 取自站外引用站内自行拍摄AI生成虚构演绎，故事经历投资观点，仅供参考健康医疗分享，仅供参考 |
| `source_external` | `.form-item-source label:has-text('取自站外')` | True | 1 | 取自站外 |
| `source_internal` | `.form-item-source label:has-text('引用站内')` | True | 1 | 引用站内 |
| `source_self_shot` | `.form-item-source label:has-text('自行拍摄')` | True | 1 | 自行拍摄 |
| `source_ai` | `.form-item-source label:has-text('AI生成')` | True | 1 | AI生成 |
| `source_fiction` | `.form-item-source label:has-text('虚构演绎，故事经历')` | True | 1 | 虚构演绎，故事经历 |
| `source_investment` | `.form-item-source label:has-text('投资观点，仅供参考')` | True | 1 | 投资观点，仅供参考 |
| `source_health` | `.form-item-source label:has-text('健康医疗分享，仅供参考')` | True | 1 | 健康医疗分享，仅供参考 |
| `external_link` | `.form-item-external-link label.byte-checkbox` | True | 1 |  |
| `visibility_public` | `.form-item-privacy label:has-text('公开')` | True | 1 | 公开 |
| `visibility_fans` | `.form-item-privacy label:has-text('粉丝可见')` | True | 1 | 粉丝可见 |
| `visibility_private` | `.form-item-privacy label:has-text('仅我可见')` | True | 1 | 仅我可见 |
| `draft` | `button.action-footer-btn.draft` | True | 1 | 存草稿 |
| `timer` | `button.action-footer-btn.timer` | True | 1 | 定时发布 |
| `publish` | `button.action-footer-btn.submit` | True | 1 | 发布 |

### video_cover_frame_dialog

| 功能点 | selector | visible | count | text |
|---|---|---:|---:|---|
| `local_upload_tab` | `body > div.Dialog-container > div > div.m-content > div > div.body.undefined > ul > li:nth-child(2)` | True | 1 | 本地上传 |
| `next` | `body > div.Dialog-container > div > div.m-content > div > div.footer.undefined > div` | True | 1 | 下一步 |
| `close` | `.Dialog-container .close` | False | 0 | Locator.inner_text: Error: Node is not an HTMLElement Call log:   - waiting for locator(".Dialog-container .close").first  |

### video_cover_local_dialog

| 功能点 | selector | visible | count | text |
|---|---|---:|---:|---|
| `file_input` | `.Dialog-container .xigua-upload-poster-trigger input[type='file']` | False | 1 |  |
| `next` | `body > div.Dialog-container > div > div.m-content > div > div.footer.undefined > div` | True | 1 | 下一步 |
| `close` | `.Dialog-container .close` | False | 0 | Locator.inner_text: Error: Node is not an HTMLElement Call log:   - waiting for locator(".Dialog-container .close").first  |

### video_cover_editor

| 功能点 | selector | visible | count | text |
|---|---|---:|---:|---|
| `template_tab` | `.xigua-image-editor-core .tool-menu li:has-text('模版')` | True | 1 | 模版 |
| `sticker_tab` | `.xigua-image-editor-core .tool-menu li:has-text('贴纸')` | True | 1 | 贴纸 |
| `text_tab` | `.xigua-image-editor-core .tool-menu li:has-text('文字')` | True | 1 | 文字 |
| `filter_tab` | `.xigua-image-editor-core .tool-menu li:has-text('滤镜')` | True | 1 | 滤镜 |
| `save_template` | `.xigua-image-editor-core .footer-option-item` | True | 1 | 保存为模板 |
| `reselect_cover` | `.xigua-image-editor-core .footer-btns button.btn-cancel` | True | 1 | 重选封面 |
| `confirm` | `.xigua-image-editor-core .footer-btns button.btn-sure` | True | 1 | 确定 |
| `close` | `.xigua-image-editor-core .close` | False | 0 | Locator.inner_text: Error: Node is not an HTMLElement Call log:   - waiting for locator(".xigua-image-editor-core .close").first  |

### video_cover_finish_confirm

| 功能点 | selector | visible | count | text |
|---|---|---:|---:|---|
| `cancel` | `.m-dialog-edit .footer button.m-button:not(.red)` | True | 1 | 取消 |
| `confirm` | `.m-dialog-edit .footer button.m-button.red` | True | 1 | 确定 |
| `close` | `.m-dialog-edit .close` | False | 0 | Locator.inner_text: Error: Node is not an HTMLElement Call log:   - waiting for locator(".m-dialog-edit .close").first  |

### work_management_real

| 功能点 | selector | visible | count | text |
|---|---|---:|---:|---|
| `entry_from_home` | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.management_tab:nth-of-type(3) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` | True | 1 | 作品管理 |
| `tab_all` | `.byte-tabs-header-title:has-text("全部")` | True | 1 | 全部 |
| `tab_article` | `.byte-tabs-header-title:has-text("文章")` | True | 1 | 文章 |
| `tab_video` | `.byte-tabs-header-title:has-text("视频")` | True | 2 | 视频 |
| `tab_weitoutiao` | `.byte-tabs-header-title:has-text("微头条")` | True | 1 | 微头条 |
| `tab_short_video` | `.byte-tabs-header-title:has-text("小视频")` | True | 1 | 小视频 |
| `tab_audio` | `.byte-tabs-header-title:has-text("音频")` | True | 1 | 音频 |
| `tab_collection` | `.byte-tabs-header-title:has-text("合集")` | True | 1 | 合集 |
| `status_all` | `.status-filter-list .filter-item:has-text("全部")` | True | 1 | 全部 |
| `status_published` | `.status-filter-list .filter-item:has-text("已发布")` | True | 1 | 已发布 |
| `status_reviewing` | `.status-filter-list .filter-item:has-text("审核中")` | True | 1 | 审核中 |
| `status_rejected` | `.status-filter-list .filter-item:has-text("未通过")` | True | 1 | 未通过 |
| `status_private` | `.status-filter-list .filter-item:has-text("仅我可见")` | True | 1 | 仅我可见 |
| `search_input` | `input[placeholder*="搜索"], input[placeholder*="标题"]` | True | 1 |  |
| `work_list_root` | `#root` | True | 1 | 状态全部已发布审核中未通过仅我可见 ~ 共 20 条内容 程序员用AI，已经从尝鲜变成日常了 +1 06-10 16:44 由文章生成 查看数据 查看评论 修改 更多 展现 27阅读 0点赞 0评论 0 程序员用AI，已经从尝鲜变成日常了  |
| `work_item` | `.article-card, .content-card, .work-card, [class*="article"]` | True | 32 | 程序员用AI，已经从尝鲜变成日常了 06-10 16:42 已发布 已推送 展现 4111阅读 40点赞 0评论 0 查看数据 查看评论 修改 更多 |
| `pagination` | `.byte-pagination, .pagination, [class*="pagination"]` | True | 6 | 12 |

## 页面扫描

### home

- URL：`https://mp.toutiao.com/profile_v4/index`
- 截图：`data/accounts/default/runs/selector-audit-20260611-131110/home.png`

| role | text | selector |
|---|---|---|
| action | 头条号 | `div#masterRoot > div.pgc-wrapper.pgc-index.index-wrapper:nth-of-type(1) > div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > a.shead_logo:nth-of-type(1)` |
| action | 消息 | `div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > div.shead_right:nth-of-type(1) > div.sys-msg:nth-of-type(1) > div:nth-of-type(1) > a.sys-msg-entity:nth-of-type(1)` |
| action | 不敬业的码农 | `div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > div.shead_right:nth-of-type(1) > div.user-panel:nth-of-type(3) > div.information:nth-of-type(1) > a:nth-of-type(1)` |
| action | 主页 | `div.byte-layout-sider-children:nth-of-type(1) > div.mp-menu-wrapper.f-min-scroll.f-hover-scroll:nth-of-type(1) > div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-item.主页_tab:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 文章 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.base_creation_tab:nth-of-type(2) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 视频 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.base_creation_tab:nth-of-type(2) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(2) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 微头条 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.base_creation_tab:nth-of-type(2) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 音频 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.base_creation_tab:nth-of-type(2) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(4) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 作品管理 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.management_tab:nth-of-type(3) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 评论管理 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.management_tab:nth-of-type(3) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(2) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 草稿箱 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.management_tab:nth-of-type(3) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 收益数据 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.data_helper_tab:nth-of-type(4) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 作品数据 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.data_helper_tab:nth-of-type(4) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(2) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 粉丝数据 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.data_helper_tab:nth-of-type(4) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 提现 | `div.byte-layout-sider-children:nth-of-type(1) > div.mp-menu-wrapper.f-min-scroll.f-hover-scroll:nth-of-type(1) > div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-item.提现_tab:nth-of-type(6) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 创作权益 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.guide_tab:nth-of-type(7) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(2) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 头条认证 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.guide_tab:nth-of-type(7) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 创作灵感 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.guide_tab:nth-of-type(7) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(4) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 创作训练营 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.guide_tab:nth-of-type(7) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(5) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 功能实验室 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.tools_tab:nth-of-type(8) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 创作保护 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.tools_tab:nth-of-type(8) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 图片素材 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.tools_tab:nth-of-type(8) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(4) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 设置 | `div.byte-layout-sider-children:nth-of-type(1) > div.mp-menu-wrapper.f-min-scroll.f-hover-scroll:nth-of-type(1) > div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-item.设置_tab:nth-of-type(9) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 43 | `div.home-block:nth-of-type(1) > div.byte-row.data-board.data-notice:nth-of-type(1) > div.mp-col.byte-col.byte-col-xs-24:nth-of-type(1) > div.data-board-item:nth-of-type(1) > div.data-board-item-primary:nth-of-type(2) > a:nth-of-type(1)` |
| action | 164,527 | `div.home-block:nth-of-type(1) > div.byte-row.data-board.data-notice:nth-of-type(1) > div.mp-col.byte-col.byte-col-xs-24:nth-of-type(2) > div.data-board-item:nth-of-type(1) > div.data-board-item-primary:nth-of-type(2) > a:nth-of-type(1)` |
| action | 11.37元 | `div.home-block:nth-of-type(1) > div.byte-row.data-board.data-notice:nth-of-type(1) > div.mp-col.byte-col.byte-col-xs-24:nth-of-type(3) > div.data-board-item:nth-of-type(1) > div.data-board-item-primary:nth-of-type(2) > a:nth-of-type(1)` |
| action |  | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.wtt-item:nth-of-type(1) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-content-wrap:nth-of-type(1) > a.cover-wrap.cover-wrap-wtt-item:nth-of-type(1)` |
| action | 程序员用AI，已经从尝鲜变成日常了 | `div.recent-works-list:nth-of-type(1) > div.recent-works-item.wtt-item:nth-of-type(1) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-content-wrap:nth-of-type(1) > div.content:nth-of-type(1) > a.content-title:nth-of-type(1)` |
| action | 27 展现量 | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.wtt-item:nth-of-type(1) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-data-item:nth-of-type(2) > a.data-item-link:nth-of-type(1)` |
| action | 0 阅读量 | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.wtt-item:nth-of-type(1) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-data-item:nth-of-type(3) > a.data-item-link:nth-of-type(1)` |
| action | 0 评论 | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.wtt-item:nth-of-type(1) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-data-item:nth-of-type(4) > a.data-item-link:nth-of-type(1)` |
| action | 0 点赞 | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.wtt-item:nth-of-type(1) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-data-item:nth-of-type(5) > a.data-item-link:nth-of-type(1)` |
| action | 程序员用AI，已经从尝鲜变成日常了 | `div.recent-works-list:nth-of-type(1) > div.recent-works-item.pgc-item:nth-of-type(2) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-content-wrap:nth-of-type(1) > div.content:nth-of-type(1) > a.content-title:nth-of-type(1)` |
| action | 4,111 展现量 | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.pgc-item:nth-of-type(2) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-data-item:nth-of-type(2) > a.data-item-link:nth-of-type(1)` |
| action | 40 阅读量 | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.pgc-item:nth-of-type(2) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-data-item:nth-of-type(3) > a.data-item-link:nth-of-type(1)` |
| action | 0 评论 | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.pgc-item:nth-of-type(2) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-data-item:nth-of-type(4) > a.data-item-link:nth-of-type(1)` |
| action | 0 点赞 | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.pgc-item:nth-of-type(2) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-data-item:nth-of-type(5) > a.data-item-link:nth-of-type(1)` |
| action |  | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.wtt-item:nth-of-type(3) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-content-wrap:nth-of-type(1) > a.cover-wrap.cover-wrap-wtt-item:nth-of-type(1)` |
| action | AI省下的时间，为什么又被工作填满了？ | `div.recent-works-list:nth-of-type(1) > div.recent-works-item.wtt-item:nth-of-type(3) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-content-wrap:nth-of-type(1) > div.content:nth-of-type(1) > a.content-title:nth-of-type(1)` |
| action | 5 展现量 | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.wtt-item:nth-of-type(3) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-data-item:nth-of-type(2) > a.data-item-link:nth-of-type(1)` |
| action | 0 阅读量 | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.wtt-item:nth-of-type(3) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-data-item:nth-of-type(3) > a.data-item-link:nth-of-type(1)` |
| action | 0 评论 | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.wtt-item:nth-of-type(3) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-data-item:nth-of-type(4) > a.data-item-link:nth-of-type(1)` |
| action | 0 点赞 | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.wtt-item:nth-of-type(3) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-data-item:nth-of-type(5) > a.data-item-link:nth-of-type(1)` |
| action | 查看更多作品 | `div.byte-row:nth-of-type(1) > div.mp-col.byte-col.byte-col-xs-24:nth-of-type(1) > div.home-block:nth-of-type(1) > div.recent-works-wrap:nth-of-type(2) > div.recent-works-item.recent-works-footer:nth-of-type(2) > a.recent-works-header-more.activity-more:nth-of-type(1)` |
| action | 更多 | `div.byte-row:nth-of-type(1) > div.mp-col.byte-col.byte-col-xs-24:nth-of-type(1) > div.home-block:nth-of-type(2) > div.home-creative-activity-wrap:nth-of-type(2) > div.home-creative-activity-header:nth-of-type(1) > a.home-creative-activity-header-more.activity-more:nth-of-type(1)` |
| action | 更多 | `div.byte-row:nth-of-type(1) > div.mp-col.byte-col.byte-col-xs-24:nth-of-type(2) > div.home-block:nth-of-type(1) > div.home-notice-swiper:nth-of-type(1) > div.home-notice-swiper-header:nth-of-type(1) > a.home-notice-swiper-more.more:nth-of-type(1)` |
| action | 今日头条低质账号专项治理公告（5月） | `div.home-notice-swiper:nth-of-type(1) > div.home-notice-swiper-region:nth-of-type(2) > div.swiper-item-wrap:nth-of-type(1) > div.home-notice-swiper-item:nth-of-type(1) > div.home-notice-swiper-item-title:nth-of-type(2) > a:nth-of-type(1)` |
| action | 今日头条低质账号专项治理公告（4月） | `div.home-notice-swiper:nth-of-type(1) > div.home-notice-swiper-region:nth-of-type(2) > div.swiper-item-wrap:nth-of-type(2) > div.home-notice-swiper-item:nth-of-type(1) > div.home-notice-swiper-item-title:nth-of-type(2) > a:nth-of-type(1)` |
| action | 今日头条不实信息治理公告（2026年4月20日） | `div.home-notice-swiper:nth-of-type(1) > div.home-notice-swiper-region:nth-of-type(2) > div.swiper-item-wrap:nth-of-type(3) > div.home-notice-swiper-item:nth-of-type(1) > div.home-notice-swiper-item-title:nth-of-type(2) > a:nth-of-type(1)` |
| action | 更多 | `div.byte-row:nth-of-type(1) > div.mp-col.byte-col.byte-col-xs-24:nth-of-type(2) > div.home-block.hot-board-wrapper:nth-of-type(2) > div.home-hot-board-container:nth-of-type(1) > div.home-hot-board-container-header:nth-of-type(1) > a.home-hot-board-container-header-more.more:nth-of-type(1)` |
| action | #AI真的能取代人类的工作吗？# | `div.home-hot-board-container:nth-of-type(1) > div.hot-board-list:nth-of-type(2) > div.byte-row:nth-of-type(1) > div.mp-col.byte-col.byte-col-xs-12:nth-of-type(1) > div.hot-board-list-col-items:nth-of-type(1) > a.hot-board-item:nth-of-type(1)` |
| action | #健康和挣钱谁应该排第一?# | `div.home-hot-board-container:nth-of-type(1) > div.hot-board-list:nth-of-type(2) > div.byte-row:nth-of-type(1) > div.mp-col.byte-col.byte-col-xs-12:nth-of-type(1) > div.hot-board-list-col-items:nth-of-type(1) > a.hot-board-item:nth-of-type(2)` |
| action | #在今日头条，你能坚持每天发文吗# | `div.home-hot-board-container:nth-of-type(1) > div.hot-board-list:nth-of-type(2) > div.byte-row:nth-of-type(1) > div.mp-col.byte-col.byte-col-xs-12:nth-of-type(1) > div.hot-board-list-col-items:nth-of-type(1) > a.hot-board-item:nth-of-type(3)` |
| action | #AI材料发现需要哪些技术支持# | `div.home-hot-board-container:nth-of-type(1) > div.hot-board-list:nth-of-type(2) > div.byte-row:nth-of-type(1) > div.mp-col.byte-col.byte-col-xs-12:nth-of-type(2) > div.hot-board-list-col-items:nth-of-type(1) > a.hot-board-item:nth-of-type(1)` |
| action | #上传视频就是做自媒体吗# | `div.home-hot-board-container:nth-of-type(1) > div.hot-board-list:nth-of-type(2) > div.byte-row:nth-of-type(1) > div.mp-col.byte-col.byte-col-xs-12:nth-of-type(2) > div.hot-board-list-col-items:nth-of-type(1) > a.hot-board-item:nth-of-type(2)` |
| action | 更多 | `div.byte-row:nth-of-type(1) > div.mp-col.byte-col.byte-col-xs-24:nth-of-type(3) > div.home-block:nth-of-type(1) > div.course-list-wrap:nth-of-type(1) > div.list-title:nth-of-type(1) > a.course-list-more.more:nth-of-type(1)` |
| action | 关于今日头条 | `div#masterRoot > div.pgc-wrapper.pgc-index.index-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_about:nth-of-type(1)` |
| action | 用户协议 | `div#masterRoot > div.pgc-wrapper.pgc-index.index-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_agreement:nth-of-type(2)` |
| action | 隐私政策 | `div#masterRoot > div.pgc-wrapper.pgc-index.index-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_agreement:nth-of-type(3)` |
| action | 社区规范 | `div#masterRoot > div.pgc-wrapper.pgc-index.index-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_operation:nth-of-type(4)` |
| action | 自律公约 | `div#masterRoot > div.pgc-wrapper.pgc-index.index-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_agreement:nth-of-type(5)` |
| action | 侵权投诉 | `div.pgc-wrapper.pgc-index.index-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > span:nth-of-type(6) > a.sfoot_agreement:nth-of-type(1)` |
| action | 联系我们 | `div#masterRoot > div.pgc-wrapper.pgc-index.index-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_contact:nth-of-type(6)` |
| action | 常见问题 | `div.pgc-wrapper.pgc-index.index-wrapper:nth-of-type(1) > div.pgc-feedback:nth-of-type(5) > div.fb-sidebar:nth-of-type(1) > div:nth-of-type(1) > div.feedback-container:nth-of-type(2) > a.feedback-wrapper.feedback-questions:nth-of-type(1)` |

### article_publish

- URL：`https://mp.toutiao.com/profile_v4/graphic/publish`
- 截图：`data/accounts/default/runs/selector-audit-20260611-131110/article_publish.png`

| role | text | selector |
|---|---|---|
| action | 消息 | `div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > div.shead_right:nth-of-type(1) > div.sys-msg:nth-of-type(2) > div:nth-of-type(1) > a.sys-msg-entity:nth-of-type(1)` |
| action |  | `div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > div.shead_right:nth-of-type(1) > div.user-panel.hide-name:nth-of-type(3) > div.information:nth-of-type(1) > a:nth-of-type(1)` |
| action |  | `div.publish-editor:nth-of-type(1) > div.syl-editor-toolbar.visible.inline:nth-of-type(1) > div.syl-toolbar:nth-of-type(1) > div.syl-toolbar-tool.undo.static:nth-of-type(1) > div:nth-of-type(1) > button.syl-toolbar-button:nth-of-type(1)` |
| action |  | `div.publish-editor:nth-of-type(1) > div.syl-editor-toolbar.visible.inline:nth-of-type(1) > div.syl-toolbar:nth-of-type(1) > div.syl-toolbar-tool.redo.static:nth-of-type(2) > div:nth-of-type(1) > button.syl-toolbar-button:nth-of-type(1)` |
| action |  | `div.publish-editor:nth-of-type(1) > div.syl-editor-toolbar.visible.inline:nth-of-type(1) > div.syl-toolbar:nth-of-type(1) > div.syl-toolbar-tool.format_clear.static:nth-of-type(3) > div:nth-of-type(1) > button.syl-toolbar-button:nth-of-type(1)` |
| action |  | `div.publish-editor:nth-of-type(1) > div.syl-editor-toolbar.visible.inline:nth-of-type(1) > div.syl-toolbar:nth-of-type(1) > div.syl-toolbar-tool.format_painter.static:nth-of-type(4) > div:nth-of-type(1) > button.syl-toolbar-button:nth-of-type(1)` |
| action |  | `div.publish-editor:nth-of-type(1) > div.syl-editor-toolbar.visible.inline:nth-of-type(1) > div.syl-toolbar:nth-of-type(1) > div.syl-toolbar-tool.header.static:nth-of-type(5) > div:nth-of-type(1) > button.syl-toolbar-button:nth-of-type(1)` |
| action |  | `div.publish-editor:nth-of-type(1) > div.syl-editor-toolbar.visible.inline:nth-of-type(1) > div.syl-toolbar:nth-of-type(1) > div.syl-toolbar-tool.bold.static:nth-of-type(6) > div:nth-of-type(1) > button.syl-toolbar-button:nth-of-type(1)` |
| action |  | `div.publish-editor:nth-of-type(1) > div.syl-editor-toolbar.visible.inline:nth-of-type(1) > div.syl-toolbar:nth-of-type(1) > div.syl-toolbar-tool.block_quote.static:nth-of-type(7) > div:nth-of-type(1) > button.syl-toolbar-button:nth-of-type(1)` |
| action |  | `div.publish-editor:nth-of-type(1) > div.syl-editor-toolbar.visible.inline:nth-of-type(1) > div.syl-toolbar:nth-of-type(1) > div.syl-toolbar-tool.list_util.static:nth-of-type(8) > div:nth-of-type(1) > button.syl-toolbar-button:nth-of-type(1)` |
| action |  | `div.publish-editor:nth-of-type(1) > div.syl-editor-toolbar.visible.inline:nth-of-type(1) > div.syl-toolbar:nth-of-type(1) > div.syl-toolbar-tool.hr.static:nth-of-type(9) > div:nth-of-type(1) > button.syl-toolbar-button:nth-of-type(1)` |
| action |  | `div.publish-editor:nth-of-type(1) > div.syl-editor-toolbar.visible.inline:nth-of-type(1) > div.syl-toolbar:nth-of-type(1) > div.syl-toolbar-tool.strike.static:nth-of-type(10) > div:nth-of-type(1) > button.syl-toolbar-button:nth-of-type(1)` |
| action |  | `div.publish-editor:nth-of-type(1) > div.syl-editor-toolbar.visible.inline:nth-of-type(1) > div.syl-toolbar:nth-of-type(1) > div.syl-toolbar-tool.code_block.static:nth-of-type(11) > span:nth-of-type(1) > button.syl-toolbar-button:nth-of-type(1)` |
| action |  | `div.publish-editor:nth-of-type(1) > div.syl-editor-toolbar.visible.inline:nth-of-type(1) > div.syl-toolbar:nth-of-type(1) > div.syl-toolbar-tool.image.static:nth-of-type(12) > div:nth-of-type(1) > button.syl-toolbar-button:nth-of-type(1)` |
| action |  | `div.publish-editor:nth-of-type(1) > div.syl-editor-toolbar.visible.inline:nth-of-type(1) > div.syl-toolbar:nth-of-type(1) > div.syl-toolbar-tool.link.static:nth-of-type(13) > div:nth-of-type(1) > button.syl-toolbar-button:nth-of-type(1)` |
| action |  | `div.publish-editor:nth-of-type(1) > div.syl-editor-toolbar.visible.inline:nth-of-type(1) > div.syl-toolbar:nth-of-type(1) > div.syl-toolbar-tool.emoji.static:nth-of-type(14) > div:nth-of-type(1) > button.syl-toolbar-button:nth-of-type(1)` |
| action |  | `div.publish-editor:nth-of-type(1) > div.syl-editor-toolbar.visible.inline:nth-of-type(1) > div.syl-toolbar:nth-of-type(1) > div.syl-toolbar-tool.table.static:nth-of-type(15) > div:nth-of-type(1) > button.syl-toolbar-button:nth-of-type(1)` |
| action |  | `div.publish-editor:nth-of-type(1) > div.syl-editor-toolbar.visible.inline:nth-of-type(1) > div.syl-toolbar:nth-of-type(1) > div.syl-toolbar-tool.card.static:nth-of-type(16) > div:nth-of-type(1) > button.syl-toolbar-button:nth-of-type(1)` |
| action |  | `div.publish-editor:nth-of-type(1) > div.syl-editor-toolbar.visible.inline:nth-of-type(1) > div.syl-toolbar:nth-of-type(1) > div.syl-toolbar-tool.doc-import.static:nth-of-type(17) > div:nth-of-type(1) > button.syl-toolbar-button:nth-of-type(1)` |
| input | 请输入文章标题（2～30个字） | `textarea[placeholder="请输入文章标题（2～30个字）"]` |
| input | 请输入正文 | `div.left-column:nth-of-type(1) > div.edit-wrap.common-container-wrapper:nth-of-type(1) > div.publish-editor:nth-of-type(1) > div.syl-editor-wrap:nth-of-type(4) > div.syl-editor:nth-of-type(1) > div.ProseMirror:nth-of-type(1)` |
| action | 单图 | `div:nth-of-type(1) > div.pgc-edit-cell.edit-cell.required:nth-of-type(1) > div.edit-input:nth-of-type(2) > div.article-cover:nth-of-type(1) > div.byte-radio-group.byte-radio-size-default.byte-radio-mode-outline:nth-of-type(1) > label.byte-radio:nth-of-type(1)` |
| action | 三图 | `div:nth-of-type(1) > div.pgc-edit-cell.edit-cell.required:nth-of-type(1) > div.edit-input:nth-of-type(2) > div.article-cover:nth-of-type(1) > div.byte-radio-group.byte-radio-size-default.byte-radio-mode-outline:nth-of-type(1) > label.byte-radio:nth-of-type(2)` |
| action | 无封面 | `div:nth-of-type(1) > div.pgc-edit-cell.edit-cell.required:nth-of-type(1) > div.edit-input:nth-of-type(2) > div.article-cover:nth-of-type(1) > div.byte-radio-group.byte-radio-size-default.byte-radio-mode-outline:nth-of-type(1) > label.byte-radio:nth-of-type(3)` |
| action | 投放广告赚收益 | `div.form-container:nth-of-type(2) > div.pgc-edit-cell.edit-cell.required:nth-of-type(3) > div.edit-input:nth-of-type(2) > div.byte-radio-group.byte-radio-size-default.byte-radio-mode-outline:nth-of-type(1) > span.combine-tip-wrap:nth-of-type(1) > label.byte-radio.article-ad-radio:nth-of-type(1)` |
| action | 不投放广告 | `div.form-wrap:nth-of-type(2) > div.form-container:nth-of-type(2) > div.pgc-edit-cell.edit-cell.required:nth-of-type(3) > div.edit-input:nth-of-type(2) > div.byte-radio-group.byte-radio-size-default.byte-radio-mode-outline:nth-of-type(1) > label.byte-radio.article-ad-radio:nth-of-type(1)` |
| action | 头条首发 | `div.form-container:nth-of-type(2) > div.pgc-edit-cell.edit-cell:nth-of-type(4) > div.edit-input:nth-of-type(2) > div.exclusive:nth-of-type(1) > div.exclusive-checkbox-wraper:nth-of-type(1) > label.byte-checkbox.checkbot-item.checkbox-with-tip:nth-of-type(1)` |
| action | 详细了解 | `div.pgc-edit-cell.edit-cell:nth-of-type(4) > div.edit-input:nth-of-type(2) > div.exclusive:nth-of-type(1) > div.exclusive-detail:nth-of-type(2) > div.exclusive-detail-content:nth-of-type(1) > a:nth-of-type(1)` |
| action | 添加至合集 | `div.form-container:nth-of-type(2) > div.pgc-edit-cell.edit-cell.collection-form-item:nth-of-type(5) > div.edit-input:nth-of-type(2) > section.collection-wrapper:nth-of-type(1) > div:nth-of-type(1) > button.byte-btn.byte-btn-default.byte-btn-size-large:nth-of-type(1)` |
| region | 同时发布微头条 发布得更多收益 | `div.pagelet-write.garr-container-white.newVersion:nth-of-type(1) > div.left-column:nth-of-type(1) > div.edit-wrap.common-container-wrapper:nth-of-type(1) > div.form-wrap:nth-of-type(2) > div.form-container:nth-of-type(2) > div.form-item:nth-of-type(8)` |
| action | 发布得更多收益 | `div.form-container:nth-of-type(2) > div.form-item:nth-of-type(8) > div.pgc-edit-cell.edit-cell.form-tuwen_wtt_trans:nth-of-type(1) > div.edit-input:nth-of-type(2) > span.combine-tip-wrap:nth-of-type(1) > label.byte-checkbox.item-checkbox.byte-checkbox-checked:nth-of-type(1)` |
| action | 取材网络 | `div.pgc-edit-cell.edit-cell:nth-of-type(1) > div.edit-input:nth-of-type(2) > div:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(1)` |
| action | 引用站内 | `div.pgc-edit-cell.edit-cell:nth-of-type(1) > div.edit-input:nth-of-type(2) > div:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(2)` |
| action | 个人观点，仅供参考 | `div.pgc-edit-cell.edit-cell:nth-of-type(1) > div.edit-input:nth-of-type(2) > div:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(3)` |
| action | 引用AI | `div.edit-input:nth-of-type(2) > div:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > span.combine-tip-wrap:nth-of-type(1) > label.byte-checkbox.checkbot-item.checkbox-with-tip:nth-of-type(1)` |
| action | 虚构演绎，故事经历 | `div.edit-input:nth-of-type(2) > div:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > span.combine-tip-wrap:nth-of-type(2) > label.byte-checkbox.checkbot-item.checkbox-with-tip:nth-of-type(1)` |
| action | 投资观点，仅供参考 | `div.pgc-edit-cell.edit-cell:nth-of-type(1) > div.edit-input:nth-of-type(2) > div:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(4)` |
| action | 健康医疗分享，仅供参考 | `div.pgc-edit-cell.edit-cell:nth-of-type(1) > div.edit-input:nth-of-type(2) > div:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(5)` |
| action | 预览 | `div.pagelet-write.garr-container-white.newVersion:nth-of-type(1) > div.left-column:nth-of-type(1) > div.edit-wrap.common-container-wrapper:nth-of-type(1) > div.publish-footer.inline-editor:nth-of-type(3) > div.garr-footer-publish-content.publish-footer-content:nth-of-type(1) > button.byte-btn.byte-btn-default.byte-btn-size-large:nth-of-type(1)` |
| action | 定时发布 | `div.pagelet-write.garr-container-white.newVersion:nth-of-type(1) > div.left-column:nth-of-type(1) > div.edit-wrap.common-container-wrapper:nth-of-type(1) > div.publish-footer.inline-editor:nth-of-type(3) > div.garr-footer-publish-content.publish-footer-content:nth-of-type(1) > button.byte-btn.byte-btn-default.byte-btn-size-large:nth-of-type(2)` |
| action | 预览并发布 | `div.pagelet-write.garr-container-white.newVersion:nth-of-type(1) > div.left-column:nth-of-type(1) > div.edit-wrap.common-container-wrapper:nth-of-type(1) > div.publish-footer.inline-editor:nth-of-type(3) > div.garr-footer-publish-content.publish-footer-content:nth-of-type(1) > button.byte-btn.byte-btn-primary.byte-btn-size-large:nth-of-type(3)` |
| region | AI 创作 | `div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-large:nth-of-type(1) > div.byte-tabs-header-scroll.is-dropdown:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(1)` |
| region | 内容建议 | `div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-large:nth-of-type(1) > div.byte-tabs-header-scroll.is-dropdown:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(2)` |
| input | 输入创作主题、观点或大纲，AI 帮你写 | `textarea[placeholder="输入创作主题、观点或大纲，AI 帮你写"]` |
| action | 详细功能 | `div.byte-tabs-content-item:nth-of-type(2) > div.byte-tabs-pane:nth-of-type(1) > div.publish-assistant-panel.publish-assistant-panel-in-ai-assistant:nth-of-type(1) > div.header.header-empty:nth-of-type(1) > div.introduction-wrap:nth-of-type(1) > a.link:nth-of-type(1)` |
| action | 常见问题 | `div.pgc-wrapper.pgc-index.is-full-screen:nth-of-type(1) > div.pgc-feedback:nth-of-type(4) > div.fb-sidebar:nth-of-type(1) > div:nth-of-type(1) > div.feedback-container:nth-of-type(2) > a.feedback-wrapper.feedback-questions:nth-of-type(1)` |

### work_management

- URL：`https://mp.toutiao.com/profile_v4/index`
- 截图：`data/accounts/default/runs/selector-audit-20260611-131110/work_management.png`

| role | text | selector |
|---|---|---|
| action | 头条号 | `div#masterRoot > div.pgc-wrapper.pgc-index.index-wrapper:nth-of-type(1) > div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > a.shead_logo:nth-of-type(1)` |
| action | 消息 | `div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > div.shead_right:nth-of-type(1) > div.sys-msg:nth-of-type(1) > div:nth-of-type(1) > a.sys-msg-entity:nth-of-type(1)` |
| action | 不敬业的码农 | `div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > div.shead_right:nth-of-type(1) > div.user-panel:nth-of-type(3) > div.information:nth-of-type(1) > a:nth-of-type(1)` |
| action | 主页 | `div.byte-layout-sider-children:nth-of-type(1) > div.mp-menu-wrapper.f-min-scroll.f-hover-scroll:nth-of-type(1) > div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-item.主页_tab:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 文章 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.base_creation_tab:nth-of-type(2) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 视频 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.base_creation_tab:nth-of-type(2) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(2) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 微头条 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.base_creation_tab:nth-of-type(2) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 音频 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.base_creation_tab:nth-of-type(2) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(4) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 作品管理 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.management_tab:nth-of-type(3) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 评论管理 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.management_tab:nth-of-type(3) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(2) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 草稿箱 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.management_tab:nth-of-type(3) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 收益数据 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.data_helper_tab:nth-of-type(4) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 作品数据 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.data_helper_tab:nth-of-type(4) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(2) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 粉丝数据 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.data_helper_tab:nth-of-type(4) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 提现 | `div.byte-layout-sider-children:nth-of-type(1) > div.mp-menu-wrapper.f-min-scroll.f-hover-scroll:nth-of-type(1) > div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-item.提现_tab:nth-of-type(6) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 创作权益 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.guide_tab:nth-of-type(7) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(2) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 头条认证 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.guide_tab:nth-of-type(7) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 创作灵感 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.guide_tab:nth-of-type(7) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(4) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 创作训练营 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.guide_tab:nth-of-type(7) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(5) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 功能实验室 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.tools_tab:nth-of-type(8) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 创作保护 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.tools_tab:nth-of-type(8) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 图片素材 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.tools_tab:nth-of-type(8) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(4) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 设置 | `div.byte-layout-sider-children:nth-of-type(1) > div.mp-menu-wrapper.f-min-scroll.f-hover-scroll:nth-of-type(1) > div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-item.设置_tab:nth-of-type(9) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 43 | `div.home-block:nth-of-type(1) > div.byte-row.data-board.data-notice:nth-of-type(1) > div.mp-col.byte-col.byte-col-xs-24:nth-of-type(1) > div.data-board-item:nth-of-type(1) > div.data-board-item-primary:nth-of-type(2) > a:nth-of-type(1)` |
| action | 164,527 | `div.home-block:nth-of-type(1) > div.byte-row.data-board.data-notice:nth-of-type(1) > div.mp-col.byte-col.byte-col-xs-24:nth-of-type(2) > div.data-board-item:nth-of-type(1) > div.data-board-item-primary:nth-of-type(2) > a:nth-of-type(1)` |
| action | 11.37元 | `div.home-block:nth-of-type(1) > div.byte-row.data-board.data-notice:nth-of-type(1) > div.mp-col.byte-col.byte-col-xs-24:nth-of-type(3) > div.data-board-item:nth-of-type(1) > div.data-board-item-primary:nth-of-type(2) > a:nth-of-type(1)` |
| action |  | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.wtt-item:nth-of-type(1) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-content-wrap:nth-of-type(1) > a.cover-wrap.cover-wrap-wtt-item:nth-of-type(1)` |
| action | 程序员用AI，已经从尝鲜变成日常了 | `div.recent-works-list:nth-of-type(1) > div.recent-works-item.wtt-item:nth-of-type(1) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-content-wrap:nth-of-type(1) > div.content:nth-of-type(1) > a.content-title:nth-of-type(1)` |
| action | 27 展现量 | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.wtt-item:nth-of-type(1) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-data-item:nth-of-type(2) > a.data-item-link:nth-of-type(1)` |
| action | 0 阅读量 | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.wtt-item:nth-of-type(1) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-data-item:nth-of-type(3) > a.data-item-link:nth-of-type(1)` |
| action | 0 评论 | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.wtt-item:nth-of-type(1) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-data-item:nth-of-type(4) > a.data-item-link:nth-of-type(1)` |
| action | 0 点赞 | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.wtt-item:nth-of-type(1) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-data-item:nth-of-type(5) > a.data-item-link:nth-of-type(1)` |
| action | 程序员用AI，已经从尝鲜变成日常了 | `div.recent-works-list:nth-of-type(1) > div.recent-works-item.pgc-item:nth-of-type(2) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-content-wrap:nth-of-type(1) > div.content:nth-of-type(1) > a.content-title:nth-of-type(1)` |
| action | 4,111 展现量 | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.pgc-item:nth-of-type(2) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-data-item:nth-of-type(2) > a.data-item-link:nth-of-type(1)` |
| action | 40 阅读量 | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.pgc-item:nth-of-type(2) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-data-item:nth-of-type(3) > a.data-item-link:nth-of-type(1)` |
| action | 0 评论 | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.pgc-item:nth-of-type(2) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-data-item:nth-of-type(4) > a.data-item-link:nth-of-type(1)` |
| action | 0 点赞 | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.pgc-item:nth-of-type(2) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-data-item:nth-of-type(5) > a.data-item-link:nth-of-type(1)` |
| action |  | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.wtt-item:nth-of-type(3) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-content-wrap:nth-of-type(1) > a.cover-wrap.cover-wrap-wtt-item:nth-of-type(1)` |
| action | AI省下的时间，为什么又被工作填满了？ | `div.recent-works-list:nth-of-type(1) > div.recent-works-item.wtt-item:nth-of-type(3) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-content-wrap:nth-of-type(1) > div.content:nth-of-type(1) > a.content-title:nth-of-type(1)` |
| action | 5 展现量 | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.wtt-item:nth-of-type(3) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-data-item:nth-of-type(2) > a.data-item-link:nth-of-type(1)` |
| action | 0 阅读量 | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.wtt-item:nth-of-type(3) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-data-item:nth-of-type(3) > a.data-item-link:nth-of-type(1)` |
| action | 0 评论 | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.wtt-item:nth-of-type(3) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-data-item:nth-of-type(4) > a.data-item-link:nth-of-type(1)` |
| action | 0 点赞 | `div.recent-works-wrap:nth-of-type(2) > div.recent-works-list:nth-of-type(1) > div.recent-works-item.wtt-item:nth-of-type(3) > div.item-wrapper:nth-of-type(2) > div.recent-works-item-data-item:nth-of-type(5) > a.data-item-link:nth-of-type(1)` |
| action | 查看更多作品 | `div.byte-row:nth-of-type(1) > div.mp-col.byte-col.byte-col-xs-24:nth-of-type(1) > div.home-block:nth-of-type(1) > div.recent-works-wrap:nth-of-type(2) > div.recent-works-item.recent-works-footer:nth-of-type(2) > a.recent-works-header-more.activity-more:nth-of-type(1)` |
| action | 更多 | `div.byte-row:nth-of-type(1) > div.mp-col.byte-col.byte-col-xs-24:nth-of-type(1) > div.home-block:nth-of-type(2) > div.home-creative-activity-wrap:nth-of-type(2) > div.home-creative-activity-header:nth-of-type(1) > a.home-creative-activity-header-more.activity-more:nth-of-type(1)` |
| action | 更多 | `div.byte-row:nth-of-type(1) > div.mp-col.byte-col.byte-col-xs-24:nth-of-type(2) > div.home-block:nth-of-type(1) > div.home-notice-swiper:nth-of-type(1) > div.home-notice-swiper-header:nth-of-type(1) > a.home-notice-swiper-more.more:nth-of-type(1)` |
| action | 今日头条低质账号专项治理公告（5月） | `div.home-notice-swiper:nth-of-type(1) > div.home-notice-swiper-region.enter-done:nth-of-type(2) > div.swiper-item-wrap:nth-of-type(1) > div.home-notice-swiper-item:nth-of-type(1) > div.home-notice-swiper-item-title:nth-of-type(2) > a:nth-of-type(1)` |
| action | 今日头条低质账号专项治理公告（4月） | `div.home-notice-swiper:nth-of-type(1) > div.home-notice-swiper-region.enter-done:nth-of-type(2) > div.swiper-item-wrap:nth-of-type(2) > div.home-notice-swiper-item:nth-of-type(1) > div.home-notice-swiper-item-title:nth-of-type(2) > a:nth-of-type(1)` |
| action | 今日头条不实信息治理公告（2026年4月20日） | `div.home-notice-swiper:nth-of-type(1) > div.home-notice-swiper-region.enter-done:nth-of-type(2) > div.swiper-item-wrap:nth-of-type(3) > div.home-notice-swiper-item:nth-of-type(1) > div.home-notice-swiper-item-title:nth-of-type(2) > a:nth-of-type(1)` |
| action | 更多 | `div.byte-row:nth-of-type(1) > div.mp-col.byte-col.byte-col-xs-24:nth-of-type(2) > div.home-block.hot-board-wrapper:nth-of-type(2) > div.home-hot-board-container:nth-of-type(1) > div.home-hot-board-container-header:nth-of-type(1) > a.home-hot-board-container-header-more.more:nth-of-type(1)` |
| action | #你的工作距离被Ai取代还要多久？# | `div.home-hot-board-container:nth-of-type(1) > div.hot-board-list:nth-of-type(2) > div.byte-row:nth-of-type(1) > div.mp-col.byte-col.byte-col-xs-12:nth-of-type(1) > div.hot-board-list-col-items:nth-of-type(1) > a.hot-board-item:nth-of-type(1)` |
| action | #你在生活中常用到哪些AI应用# | `div.home-hot-board-container:nth-of-type(1) > div.hot-board-list:nth-of-type(2) > div.byte-row:nth-of-type(1) > div.mp-col.byte-col.byte-col-xs-12:nth-of-type(1) > div.hot-board-list-col-items:nth-of-type(1) > a.hot-board-item:nth-of-type(2)` |
| action | #论工作赚钱重要，还是身体健康重要# | `div.home-hot-board-container:nth-of-type(1) > div.hot-board-list:nth-of-type(2) > div.byte-row:nth-of-type(1) > div.mp-col.byte-col.byte-col-xs-12:nth-of-type(1) > div.hot-board-list-col-items:nth-of-type(1) > a.hot-board-item:nth-of-type(3)` |
| action | #上联：冬去山明水秀，下联：请你来# | `div.home-hot-board-container:nth-of-type(1) > div.hot-board-list:nth-of-type(2) > div.byte-row:nth-of-type(1) > div.mp-col.byte-col.byte-col-xs-12:nth-of-type(2) > div.hot-board-list-col-items:nth-of-type(1) > a.hot-board-item:nth-of-type(1)` |
| action | #头条里谁的视频做的最好# | `div.home-hot-board-container:nth-of-type(1) > div.hot-board-list:nth-of-type(2) > div.byte-row:nth-of-type(1) > div.mp-col.byte-col.byte-col-xs-12:nth-of-type(2) > div.hot-board-list-col-items:nth-of-type(1) > a.hot-board-item:nth-of-type(2)` |
| action | 更多 | `div.byte-row:nth-of-type(1) > div.mp-col.byte-col.byte-col-xs-24:nth-of-type(3) > div.home-block:nth-of-type(1) > div.course-list-wrap:nth-of-type(1) > div.list-title:nth-of-type(1) > a.course-list-more.more:nth-of-type(1)` |
| action | 关于今日头条 | `div#masterRoot > div.pgc-wrapper.pgc-index.index-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_about:nth-of-type(1)` |
| action | 用户协议 | `div#masterRoot > div.pgc-wrapper.pgc-index.index-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_agreement:nth-of-type(2)` |
| action | 隐私政策 | `div#masterRoot > div.pgc-wrapper.pgc-index.index-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_agreement:nth-of-type(3)` |
| action | 社区规范 | `div#masterRoot > div.pgc-wrapper.pgc-index.index-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_operation:nth-of-type(4)` |
| action | 自律公约 | `div#masterRoot > div.pgc-wrapper.pgc-index.index-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_agreement:nth-of-type(5)` |
| action | 侵权投诉 | `div.pgc-wrapper.pgc-index.index-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > span:nth-of-type(6) > a.sfoot_agreement:nth-of-type(1)` |
| action | 联系我们 | `div#masterRoot > div.pgc-wrapper.pgc-index.index-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_contact:nth-of-type(6)` |
| action | 常见问题 | `div.pgc-wrapper.pgc-index.index-wrapper:nth-of-type(1) > div.pgc-feedback:nth-of-type(5) > div.fb-sidebar:nth-of-type(1) > div:nth-of-type(1) > div.feedback-container:nth-of-type(2) > a.feedback-wrapper.feedback-questions:nth-of-type(1)` |

### video_publish_initial

- URL：`https://mp.toutiao.com/profile_v4/xigua/upload-video`
- 截图：`data/accounts/default/runs/selector-audit-20260611-131110/video_publish_initial.png`

| role | text | selector |
|---|---|---|
| action | 头条号 | `div.full-screen#masterRoot > div.pgc-wrapper.pgc-index.is-full-screen:nth-of-type(1) > div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > a.shead_logo:nth-of-type(1)` |
| action | 消息 | `div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > div.shead_right:nth-of-type(1) > div.sys-msg:nth-of-type(1) > div:nth-of-type(1) > a.sys-msg-entity:nth-of-type(1)` |
| action |  | `div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > div.shead_right:nth-of-type(1) > div.user-panel.hide-name:nth-of-type(2) > div.information:nth-of-type(1) > a:nth-of-type(1)` |
| region | 发布视频 | `div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-scroll.is-dropdown:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(1)` |
| region | 创建合集 | `div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-scroll.is-dropdown:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(2)` |
| action | 常见问题 | `div.pgc-wrapper.pgc-index.is-full-screen:nth-of-type(1) > div.pgc-feedback:nth-of-type(4) > div.fb-sidebar:nth-of-type(1) > div:nth-of-type(1) > div.feedback-container:nth-of-type(2) > a.feedback-wrapper.feedback-questions:nth-of-type(1)` |

### video_publish_form

- URL：`https://mp.toutiao.com/profile_v4/xigua/upload-video`
- 截图：`data/accounts/default/runs/selector-audit-20260611-131110/video_publish_form.png`

| role | text | selector |
|---|---|---|
| action | 头条号 | `div.full-screen#masterRoot > div.pgc-wrapper.pgc-index.is-full-screen:nth-of-type(1) > div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > a.shead_logo:nth-of-type(1)` |
| action | 消息 | `div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > div.shead_right:nth-of-type(1) > div.sys-msg:nth-of-type(1) > div:nth-of-type(1) > a.sys-msg-entity:nth-of-type(1)` |
| action |  | `div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > div.shead_right:nth-of-type(1) > div.user-panel.hide-name:nth-of-type(2) > div.information:nth-of-type(1) > a:nth-of-type(1)` |
| region | 发布视频 | `div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-scroll.is-dropdown:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(1)` |
| region | 创建合集 | `div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-scroll.is-dropdown:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(2)` |
| action | 添加视频 | `div.xigua-upload-video-content:nth-of-type(1) > div.video-show-progress:nth-of-type(1) > div.byte-upload.xigua-upload-video-trigger.upload-video-trigger-btn:nth-of-type(2) > div.byte-upload-trigger:nth-of-type(1) > div:nth-of-type(1) > button.byte-btn.byte-btn-primary.byte-btn-size-huge:nth-of-type(1)` |
| region | 标题 9/30 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-title:nth-of-type(1)` |
| input | 请输入 1～30 个字符 | `input[placeholder="请输入 1～30 个字符"]` |
| region | 话题 还可以添加10个话题 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-hash_tag:nth-of-type(2)` |
| input | 请输入 | `input[placeholder="请输入"]` |
| region | 封面 上传封面 清晰美观的封面有利于推荐，建议分辨率不低于 1920*1080（大小不超过 20M）建议的封面 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-poster:nth-of-type(3)` |
| action | 建议的封面 | `div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-poster:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-help:nth-of-type(2) > a:nth-of-type(1)` |
| region | 视频简介 0/400 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-abstract:nth-of-type(4)` |
| input | 请输入视频简介 | `textarea[placeholder="请输入视频简介"]` |
| region | 视频生成图文 生成图文勾选后额外得图文创作收益 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-video2art:nth-of-type(5)` |
| action | 生成图文 | `div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-video2art:nth-of-type(5) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.top:nth-of-type(2) > label.byte-checkbox:nth-of-type(1)` |
| region | 创作收益 开通头条视频创作权益，发布横版视频可获得创作收益 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-benefit:nth-of-type(6)` |
| region | 合集 选择合集 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-collection:nth-of-type(1)` |
| action | 选择合集 | `div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-collection:nth-of-type(1) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > button.byte-btn.byte-btn-default.byte-btn-size-large:nth-of-type(1)` |
| region | 互动贴纸 添加贴纸 在视频中添加互动贴纸，可以获得更多的关注、点赞 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-stickers:nth-of-type(2)` |
| action | 添加贴纸 | `div.video-form-item.form-item-stickers:nth-of-type(2) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.m-follow-guide-btn:nth-of-type(1) > span:nth-of-type(1) > button.byte-btn.byte-btn-default.byte-btn-size-large:nth-of-type(1)` |
| region | 作品声明 取自站外引用站内自行拍摄AI生成虚构演绎，故事经历投资观点，仅供参考健康医疗分享，仅供参考 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-source:nth-of-type(3)` |
| action | 取自站外 | `div.video-form-item.form-item-source:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(1)` |
| action | 引用站内 | `div.video-form-item.form-item-source:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(2)` |
| action | 自行拍摄 | `div.video-form-item.form-item-source:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(3)` |
| action | AI生成 | `div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > span.combine-tip-wrap:nth-of-type(1) > label.byte-checkbox.checkbot-item.checkbox-with-tip:nth-of-type(1)` |
| action | 虚构演绎，故事经历 | `div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > span.combine-tip-wrap:nth-of-type(2) > label.byte-checkbox.checkbot-item.checkbox-with-tip:nth-of-type(1)` |
| action | 投资观点，仅供参考 | `div.video-form-item.form-item-source:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(4)` |
| action | 健康医疗分享，仅供参考 | `div.video-form-item.form-item-source:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(5)` |
| region | 扩展链接 在今日头条APP的固定位置插入链接 了解扩展链接 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-external-link:nth-of-type(4)` |
| action |  | `div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-external-link:nth-of-type(4) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > label.byte-checkbox:nth-of-type(1)` |
| action | 了解扩展链接 | `div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-external-link:nth-of-type(4) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > a.video-form-item-link:nth-of-type(1)` |
| region | 谁可以看 公开粉丝可见仅我可见 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-privacy:nth-of-type(5)` |
| action | 公开 | `div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-privacy:nth-of-type(5) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.byte-radio-group.byte-radio-size-default.byte-radio-mode-outline:nth-of-type(1) > label.byte-radio:nth-of-type(1)` |
| action | 粉丝可见 | `div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-privacy:nth-of-type(5) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.byte-radio-group.byte-radio-size-default.byte-radio-mode-outline:nth-of-type(1) > label.byte-radio:nth-of-type(2)` |
| action | 仅我可见 | `div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-privacy:nth-of-type(5) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.byte-radio-group.byte-radio-size-default.byte-radio-mode-outline:nth-of-type(1) > label.byte-radio:nth-of-type(3)` |
| action | 存草稿 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-batch-footer:nth-of-type(3) > div.button-group:nth-of-type(1) > button.byte-btn.byte-btn-default.byte-btn-size-large:nth-of-type(1)` |
| action | 定时发布 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-batch-footer:nth-of-type(3) > div.button-group:nth-of-type(1) > button.byte-btn.byte-btn-default.byte-btn-size-large:nth-of-type(2)` |
| action | 发布 | `button[data-wkswitch="disable-auto-publish"]` |
| action | 常见问题 | `div.pgc-wrapper.pgc-index.is-full-screen:nth-of-type(1) > div.pgc-feedback:nth-of-type(4) > div.fb-sidebar:nth-of-type(1) > div:nth-of-type(1) > div.feedback-container:nth-of-type(2) > a.feedback-wrapper.feedback-questions:nth-of-type(1)` |

### video_cover_frame_dialog

- URL：`https://mp.toutiao.com/profile_v4/xigua/upload-video`
- 截图：`data/accounts/default/runs/selector-audit-20260611-131110/video_cover_frame_dialog.png`

| role | text | selector |
|---|---|---|
| action | 头条号 | `div.full-screen#masterRoot > div.pgc-wrapper.pgc-index.is-full-screen:nth-of-type(1) > div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > a.shead_logo:nth-of-type(1)` |
| action | 消息 | `div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > div.shead_right:nth-of-type(1) > div.sys-msg:nth-of-type(1) > div:nth-of-type(1) > a.sys-msg-entity:nth-of-type(1)` |
| action |  | `div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > div.shead_right:nth-of-type(1) > div.user-panel.hide-name:nth-of-type(2) > div.information:nth-of-type(1) > a:nth-of-type(1)` |
| region | 发布视频 | `div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-scroll.is-dropdown:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(1)` |
| region | 创建合集 | `div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-scroll.is-dropdown:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(2)` |
| action | 添加视频 | `div.xigua-upload-video-content:nth-of-type(1) > div.video-show-progress:nth-of-type(1) > div.byte-upload.xigua-upload-video-trigger.upload-video-trigger-btn:nth-of-type(2) > div.byte-upload-trigger:nth-of-type(1) > div:nth-of-type(1) > button.byte-btn.byte-btn-primary.byte-btn-size-huge:nth-of-type(1)` |
| region | 标题 9/30 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-title:nth-of-type(1)` |
| input | 请输入 1～30 个字符 | `input[placeholder="请输入 1～30 个字符"]` |
| region | 话题 还可以添加10个话题 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-hash_tag:nth-of-type(2)` |
| input | 请输入 | `input[placeholder="请输入"]` |
| region | 封面 上传封面 清晰美观的封面有利于推荐，建议分辨率不低于 1920*1080（大小不超过 20M）建议的封面 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-poster:nth-of-type(3)` |
| action | 建议的封面 | `div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-poster:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-help:nth-of-type(2) > a:nth-of-type(1)` |
| region | 视频简介 0/400 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-abstract:nth-of-type(4)` |
| input | 请输入视频简介 | `textarea[placeholder="请输入视频简介"]` |
| region | 视频生成图文 生成图文勾选后额外得图文创作收益 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-video2art:nth-of-type(5)` |
| action | 生成图文 | `div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-video2art:nth-of-type(5) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.top:nth-of-type(2) > label.byte-checkbox:nth-of-type(1)` |
| region | 创作收益 开通头条视频创作权益，发布横版视频可获得创作收益 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-benefit:nth-of-type(6)` |
| region | 合集 选择合集 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-collection:nth-of-type(1)` |
| action | 选择合集 | `div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-collection:nth-of-type(1) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > button.byte-btn.byte-btn-default.byte-btn-size-large:nth-of-type(1)` |
| region | 互动贴纸 添加贴纸 在视频中添加互动贴纸，可以获得更多的关注、点赞 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-stickers:nth-of-type(2)` |
| action | 添加贴纸 | `div.video-form-item.form-item-stickers:nth-of-type(2) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.m-follow-guide-btn:nth-of-type(1) > span:nth-of-type(1) > button.byte-btn.byte-btn-default.byte-btn-size-large:nth-of-type(1)` |
| region | 作品声明 取自站外引用站内自行拍摄AI生成虚构演绎，故事经历投资观点，仅供参考健康医疗分享，仅供参考 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-source:nth-of-type(3)` |
| action | 取自站外 | `div.video-form-item.form-item-source:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(1)` |
| action | 引用站内 | `div.video-form-item.form-item-source:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(2)` |
| action | 自行拍摄 | `div.video-form-item.form-item-source:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(3)` |
| action | AI生成 | `div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > span.combine-tip-wrap:nth-of-type(1) > label.byte-checkbox.checkbot-item.checkbox-with-tip:nth-of-type(1)` |
| action | 虚构演绎，故事经历 | `div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > span.combine-tip-wrap:nth-of-type(2) > label.byte-checkbox.checkbot-item.checkbox-with-tip:nth-of-type(1)` |
| action | 投资观点，仅供参考 | `div.video-form-item.form-item-source:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(4)` |
| action | 健康医疗分享，仅供参考 | `div.video-form-item.form-item-source:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(5)` |
| region | 扩展链接 在今日头条APP的固定位置插入链接 了解扩展链接 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-external-link:nth-of-type(4)` |
| action |  | `div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-external-link:nth-of-type(4) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > label.byte-checkbox:nth-of-type(1)` |
| action | 了解扩展链接 | `div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-external-link:nth-of-type(4) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > a.video-form-item-link:nth-of-type(1)` |
| region | 谁可以看 公开粉丝可见仅我可见 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-privacy:nth-of-type(5)` |
| action | 公开 | `div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-privacy:nth-of-type(5) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.byte-radio-group.byte-radio-size-default.byte-radio-mode-outline:nth-of-type(1) > label.byte-radio:nth-of-type(1)` |
| action | 粉丝可见 | `div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-privacy:nth-of-type(5) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.byte-radio-group.byte-radio-size-default.byte-radio-mode-outline:nth-of-type(1) > label.byte-radio:nth-of-type(2)` |
| action | 仅我可见 | `div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-privacy:nth-of-type(5) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.byte-radio-group.byte-radio-size-default.byte-radio-mode-outline:nth-of-type(1) > label.byte-radio:nth-of-type(3)` |
| action | 存草稿 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-batch-footer:nth-of-type(3) > div.button-group:nth-of-type(1) > button.byte-btn.byte-btn-default.byte-btn-size-large:nth-of-type(1)` |
| action | 定时发布 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-batch-footer:nth-of-type(3) > div.button-group:nth-of-type(1) > button.byte-btn.byte-btn-default.byte-btn-size-large:nth-of-type(2)` |
| action | 发布 | `button[data-wkswitch="disable-auto-publish"]` |
| action | 常见问题 | `div.pgc-wrapper.pgc-index.is-full-screen:nth-of-type(1) > div.pgc-feedback:nth-of-type(4) > div.fb-sidebar:nth-of-type(1) > div:nth-of-type(1) > div.feedback-container:nth-of-type(2) > a.feedback-wrapper.feedback-questions:nth-of-type(1)` |

### video_cover_local_dialog

- URL：`https://mp.toutiao.com/profile_v4/xigua/upload-video`
- 截图：`data/accounts/default/runs/selector-audit-20260611-131110/video_cover_local_dialog.png`

| role | text | selector |
|---|---|---|
| action | 头条号 | `div.full-screen#masterRoot > div.pgc-wrapper.pgc-index.is-full-screen:nth-of-type(1) > div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > a.shead_logo:nth-of-type(1)` |
| action | 消息 | `div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > div.shead_right:nth-of-type(1) > div.sys-msg:nth-of-type(1) > div:nth-of-type(1) > a.sys-msg-entity:nth-of-type(1)` |
| action |  | `div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > div.shead_right:nth-of-type(1) > div.user-panel.hide-name:nth-of-type(2) > div.information:nth-of-type(1) > a:nth-of-type(1)` |
| region | 发布视频 | `div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-scroll.is-dropdown:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(1)` |
| region | 创建合集 | `div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-scroll.is-dropdown:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(2)` |
| action | 添加视频 | `div.xigua-upload-video-content:nth-of-type(1) > div.video-show-progress:nth-of-type(1) > div.byte-upload.xigua-upload-video-trigger.upload-video-trigger-btn:nth-of-type(2) > div.byte-upload-trigger:nth-of-type(1) > div:nth-of-type(1) > button.byte-btn.byte-btn-primary.byte-btn-size-huge:nth-of-type(1)` |
| region | 标题 9/30 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-title:nth-of-type(1)` |
| input | 请输入 1～30 个字符 | `input[placeholder="请输入 1～30 个字符"]` |
| region | 话题 还可以添加10个话题 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-hash_tag:nth-of-type(2)` |
| input | 请输入 | `input[placeholder="请输入"]` |
| region | 封面 上传封面 清晰美观的封面有利于推荐，建议分辨率不低于 1920*1080（大小不超过 20M）建议的封面 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-poster:nth-of-type(3)` |
| action | 建议的封面 | `div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-poster:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-help:nth-of-type(2) > a:nth-of-type(1)` |
| region | 视频简介 0/400 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-abstract:nth-of-type(4)` |
| input | 请输入视频简介 | `textarea[placeholder="请输入视频简介"]` |
| region | 视频生成图文 生成图文勾选后额外得图文创作收益 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-video2art:nth-of-type(5)` |
| action | 生成图文 | `div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-video2art:nth-of-type(5) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.top:nth-of-type(2) > label.byte-checkbox:nth-of-type(1)` |
| region | 创作收益 开通头条视频创作权益，发布横版视频可获得创作收益 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-benefit:nth-of-type(6)` |
| region | 合集 选择合集 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-collection:nth-of-type(1)` |
| action | 选择合集 | `div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-collection:nth-of-type(1) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > button.byte-btn.byte-btn-default.byte-btn-size-large:nth-of-type(1)` |
| region | 互动贴纸 添加贴纸 在视频中添加互动贴纸，可以获得更多的关注、点赞 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-stickers:nth-of-type(2)` |
| action | 添加贴纸 | `div.video-form-item.form-item-stickers:nth-of-type(2) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.m-follow-guide-btn:nth-of-type(1) > span:nth-of-type(1) > button.byte-btn.byte-btn-default.byte-btn-size-large:nth-of-type(1)` |
| region | 作品声明 取自站外引用站内自行拍摄AI生成虚构演绎，故事经历投资观点，仅供参考健康医疗分享，仅供参考 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-source:nth-of-type(3)` |
| action | 取自站外 | `div.video-form-item.form-item-source:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(1)` |
| action | 引用站内 | `div.video-form-item.form-item-source:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(2)` |
| action | 自行拍摄 | `div.video-form-item.form-item-source:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(3)` |
| action | AI生成 | `div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > span.combine-tip-wrap:nth-of-type(1) > label.byte-checkbox.checkbot-item.checkbox-with-tip:nth-of-type(1)` |
| action | 虚构演绎，故事经历 | `div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > span.combine-tip-wrap:nth-of-type(2) > label.byte-checkbox.checkbot-item.checkbox-with-tip:nth-of-type(1)` |
| action | 投资观点，仅供参考 | `div.video-form-item.form-item-source:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(4)` |
| action | 健康医疗分享，仅供参考 | `div.video-form-item.form-item-source:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(5)` |
| region | 扩展链接 在今日头条APP的固定位置插入链接 了解扩展链接 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-external-link:nth-of-type(4)` |
| action |  | `div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-external-link:nth-of-type(4) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > label.byte-checkbox:nth-of-type(1)` |
| action | 了解扩展链接 | `div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-external-link:nth-of-type(4) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > a.video-form-item-link:nth-of-type(1)` |
| region | 谁可以看 公开粉丝可见仅我可见 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-privacy:nth-of-type(5)` |
| action | 公开 | `div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-privacy:nth-of-type(5) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.byte-radio-group.byte-radio-size-default.byte-radio-mode-outline:nth-of-type(1) > label.byte-radio:nth-of-type(1)` |
| action | 粉丝可见 | `div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-privacy:nth-of-type(5) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.byte-radio-group.byte-radio-size-default.byte-radio-mode-outline:nth-of-type(1) > label.byte-radio:nth-of-type(2)` |
| action | 仅我可见 | `div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-privacy:nth-of-type(5) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.byte-radio-group.byte-radio-size-default.byte-radio-mode-outline:nth-of-type(1) > label.byte-radio:nth-of-type(3)` |
| action | 存草稿 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-batch-footer:nth-of-type(3) > div.button-group:nth-of-type(1) > button.byte-btn.byte-btn-default.byte-btn-size-large:nth-of-type(1)` |
| action | 定时发布 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-batch-footer:nth-of-type(3) > div.button-group:nth-of-type(1) > button.byte-btn.byte-btn-default.byte-btn-size-large:nth-of-type(2)` |
| action | 发布 | `button[data-wkswitch="disable-auto-publish"]` |
| action | 常见问题 | `div.pgc-wrapper.pgc-index.is-full-screen:nth-of-type(1) > div.pgc-feedback:nth-of-type(4) > div.fb-sidebar:nth-of-type(1) > div:nth-of-type(1) > div.feedback-container:nth-of-type(2) > a.feedback-wrapper.feedback-questions:nth-of-type(1)` |

### video_cover_editor

- URL：`https://mp.toutiao.com/profile_v4/xigua/upload-video`
- 截图：`data/accounts/default/runs/selector-audit-20260611-131110/video_cover_editor.png`

| role | text | selector |
|---|---|---|
| action | 头条号 | `div.full-screen#masterRoot > div.pgc-wrapper.pgc-index.is-full-screen:nth-of-type(1) > div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > a.shead_logo:nth-of-type(1)` |
| action | 消息 | `div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > div.shead_right:nth-of-type(1) > div.sys-msg:nth-of-type(1) > div:nth-of-type(1) > a.sys-msg-entity:nth-of-type(1)` |
| action |  | `div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > div.shead_right:nth-of-type(1) > div.user-panel.hide-name:nth-of-type(2) > div.information:nth-of-type(1) > a:nth-of-type(1)` |
| region | 发布视频 | `div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-scroll.is-dropdown:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(1)` |
| region | 创建合集 | `div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-scroll.is-dropdown:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(2)` |
| action | 添加视频 | `div.xigua-upload-video-content:nth-of-type(1) > div.video-show-progress:nth-of-type(1) > div.byte-upload.xigua-upload-video-trigger.upload-video-trigger-btn:nth-of-type(2) > div.byte-upload-trigger:nth-of-type(1) > div:nth-of-type(1) > button.byte-btn.byte-btn-primary.byte-btn-size-huge:nth-of-type(1)` |
| region | 标题 9/30 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-title:nth-of-type(1)` |
| input | 请输入 1～30 个字符 | `input[placeholder="请输入 1～30 个字符"]` |
| region | 话题 还可以添加10个话题 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-hash_tag:nth-of-type(2)` |
| input | 请输入 | `input[placeholder="请输入"]` |
| region | 封面 上传封面 清晰美观的封面有利于推荐，建议分辨率不低于 1920*1080（大小不超过 20M）建议的封面 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-poster:nth-of-type(3)` |
| action | 建议的封面 | `div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-poster:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-help:nth-of-type(2) > a:nth-of-type(1)` |
| region | 视频简介 0/400 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-abstract:nth-of-type(4)` |
| input | 请输入视频简介 | `textarea[placeholder="请输入视频简介"]` |
| region | 视频生成图文 生成图文勾选后额外得图文创作收益 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-video2art:nth-of-type(5)` |
| action | 生成图文 | `div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-video2art:nth-of-type(5) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.top:nth-of-type(2) > label.byte-checkbox:nth-of-type(1)` |
| region | 创作收益 开通头条视频创作权益，发布横版视频可获得创作收益 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-benefit:nth-of-type(6)` |
| region | 合集 选择合集 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-collection:nth-of-type(1)` |
| action | 选择合集 | `div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-collection:nth-of-type(1) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > button.byte-btn.byte-btn-default.byte-btn-size-large:nth-of-type(1)` |
| region | 互动贴纸 添加贴纸 在视频中添加互动贴纸，可以获得更多的关注、点赞 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-stickers:nth-of-type(2)` |
| action | 添加贴纸 | `div.video-form-item.form-item-stickers:nth-of-type(2) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.m-follow-guide-btn:nth-of-type(1) > span:nth-of-type(1) > button.byte-btn.byte-btn-default.byte-btn-size-large:nth-of-type(1)` |
| region | 作品声明 取自站外引用站内自行拍摄AI生成虚构演绎，故事经历投资观点，仅供参考健康医疗分享，仅供参考 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-source:nth-of-type(3)` |
| action | 取自站外 | `div.video-form-item.form-item-source:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(1)` |
| action | 引用站内 | `div.video-form-item.form-item-source:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(2)` |
| action | 自行拍摄 | `div.video-form-item.form-item-source:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(3)` |
| action | AI生成 | `div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > span.combine-tip-wrap:nth-of-type(1) > label.byte-checkbox.checkbot-item.checkbox-with-tip:nth-of-type(1)` |
| action | 虚构演绎，故事经历 | `div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > span.combine-tip-wrap:nth-of-type(2) > label.byte-checkbox.checkbot-item.checkbox-with-tip:nth-of-type(1)` |
| action | 投资观点，仅供参考 | `div.video-form-item.form-item-source:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(4)` |
| action | 健康医疗分享，仅供参考 | `div.video-form-item.form-item-source:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(5)` |
| region | 扩展链接 在今日头条APP的固定位置插入链接 了解扩展链接 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-external-link:nth-of-type(4)` |
| action |  | `div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-external-link:nth-of-type(4) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > label.byte-checkbox:nth-of-type(1)` |
| action | 了解扩展链接 | `div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-external-link:nth-of-type(4) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > a.video-form-item-link:nth-of-type(1)` |
| region | 谁可以看 公开粉丝可见仅我可见 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-privacy:nth-of-type(5)` |
| action | 公开 | `div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-privacy:nth-of-type(5) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.byte-radio-group.byte-radio-size-default.byte-radio-mode-outline:nth-of-type(1) > label.byte-radio:nth-of-type(1)` |
| action | 粉丝可见 | `div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-privacy:nth-of-type(5) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.byte-radio-group.byte-radio-size-default.byte-radio-mode-outline:nth-of-type(1) > label.byte-radio:nth-of-type(2)` |
| action | 仅我可见 | `div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-privacy:nth-of-type(5) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.byte-radio-group.byte-radio-size-default.byte-radio-mode-outline:nth-of-type(1) > label.byte-radio:nth-of-type(3)` |
| action | 存草稿 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-batch-footer:nth-of-type(3) > div.button-group:nth-of-type(1) > button.byte-btn.byte-btn-default.byte-btn-size-large:nth-of-type(1)` |
| action | 定时发布 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-batch-footer:nth-of-type(3) > div.button-group:nth-of-type(1) > button.byte-btn.byte-btn-default.byte-btn-size-large:nth-of-type(2)` |
| action | 发布 | `button[data-wkswitch="disable-auto-publish"]` |
| action | 常见问题 | `div.pgc-wrapper.pgc-index.is-full-screen:nth-of-type(1) > div.pgc-feedback:nth-of-type(4) > div.fb-sidebar:nth-of-type(1) > div:nth-of-type(1) > div.feedback-container:nth-of-type(2) > a.feedback-wrapper.feedback-questions:nth-of-type(1)` |
| action | 重选封面 | `div#tc-ie-base-content > div.tc-ie-base:nth-of-type(2) > div.base-content-wrap:nth-of-type(2) > div.footer-btns:nth-of-type(3) > div.btns:nth-of-type(3) > button.btn-l.btn-cancel:nth-of-type(1)` |
| action | 确定 | `div#tc-ie-base-content > div.tc-ie-base:nth-of-type(2) > div.base-content-wrap:nth-of-type(2) > div.footer-btns:nth-of-type(3) > div.btns:nth-of-type(3) > button.btn-l.btn-sure.ml16:nth-of-type(2)` |

### video_cover_finish_confirm

- URL：`https://mp.toutiao.com/profile_v4/xigua/upload-video`
- 截图：`data/accounts/default/runs/selector-audit-20260611-131110/video_cover_finish_confirm.png`

| role | text | selector |
|---|---|---|
| action | 头条号 | `div.full-screen#masterRoot > div.pgc-wrapper.pgc-index.is-full-screen:nth-of-type(1) > div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > a.shead_logo:nth-of-type(1)` |
| action | 消息 | `div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > div.shead_right:nth-of-type(1) > div.sys-msg:nth-of-type(1) > div:nth-of-type(1) > a.sys-msg-entity:nth-of-type(1)` |
| action |  | `div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > div.shead_right:nth-of-type(1) > div.user-panel.hide-name:nth-of-type(2) > div.information:nth-of-type(1) > a:nth-of-type(1)` |
| region | 发布视频 | `div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-scroll.is-dropdown:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(1)` |
| region | 创建合集 | `div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-scroll.is-dropdown:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(2)` |
| action | 添加视频 | `div.xigua-upload-video-content:nth-of-type(1) > div.video-show-progress:nth-of-type(1) > div.byte-upload.xigua-upload-video-trigger.upload-video-trigger-btn:nth-of-type(2) > div.byte-upload-trigger:nth-of-type(1) > div:nth-of-type(1) > button.byte-btn.byte-btn-primary.byte-btn-size-huge:nth-of-type(1)` |
| region | 标题 9/30 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-title:nth-of-type(1)` |
| input | 请输入 1～30 个字符 | `input[placeholder="请输入 1～30 个字符"]` |
| region | 话题 还可以添加10个话题 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-hash_tag:nth-of-type(2)` |
| input | 请输入 | `input[placeholder="请输入"]` |
| region | 封面 上传封面 清晰美观的封面有利于推荐，建议分辨率不低于 1920*1080（大小不超过 20M）建议的封面 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-poster:nth-of-type(3)` |
| action | 建议的封面 | `div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-poster:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-help:nth-of-type(2) > a:nth-of-type(1)` |
| region | 视频简介 0/400 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-abstract:nth-of-type(4)` |
| input | 请输入视频简介 | `textarea[placeholder="请输入视频简介"]` |
| region | 视频生成图文 生成图文勾选后额外得图文创作收益 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-video2art:nth-of-type(5)` |
| action | 生成图文 | `div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-video2art:nth-of-type(5) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.top:nth-of-type(2) > label.byte-checkbox:nth-of-type(1)` |
| region | 创作收益 开通头条视频创作权益，发布横版视频可获得创作收益 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-basic:nth-of-type(1) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-benefit:nth-of-type(6)` |
| region | 合集 选择合集 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-collection:nth-of-type(1)` |
| action | 选择合集 | `div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-collection:nth-of-type(1) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > button.byte-btn.byte-btn-default.byte-btn-size-large:nth-of-type(1)` |
| region | 互动贴纸 添加贴纸 在视频中添加互动贴纸，可以获得更多的关注、点赞 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-stickers:nth-of-type(2)` |
| action | 添加贴纸 | `div.video-form-item.form-item-stickers:nth-of-type(2) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.m-follow-guide-btn:nth-of-type(1) > span:nth-of-type(1) > button.byte-btn.byte-btn-default.byte-btn-size-large:nth-of-type(1)` |
| region | 作品声明 取自站外引用站内自行拍摄AI生成虚构演绎，故事经历投资观点，仅供参考健康医疗分享，仅供参考 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-source:nth-of-type(3)` |
| action | 取自站外 | `div.video-form-item.form-item-source:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(1)` |
| action | 引用站内 | `div.video-form-item.form-item-source:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(2)` |
| action | 自行拍摄 | `div.video-form-item.form-item-source:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(3)` |
| action | AI生成 | `div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > span.combine-tip-wrap:nth-of-type(1) > label.byte-checkbox.checkbot-item.checkbox-with-tip:nth-of-type(1)` |
| action | 虚构演绎，故事经历 | `div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > span.combine-tip-wrap:nth-of-type(2) > label.byte-checkbox.checkbot-item.checkbox-with-tip:nth-of-type(1)` |
| action | 投资观点，仅供参考 | `div.video-form-item.form-item-source:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(4)` |
| action | 健康医疗分享，仅供参考 | `div.video-form-item.form-item-source:nth-of-type(3) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.source-info-wrap:nth-of-type(1) > span.byte-checkbox-group.group:nth-of-type(1) > label.byte-checkbox.checkbot-item:nth-of-type(5)` |
| region | 扩展链接 在今日头条APP的固定位置插入链接 了解扩展链接 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-external-link:nth-of-type(4)` |
| action |  | `div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-external-link:nth-of-type(4) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > label.byte-checkbox:nth-of-type(1)` |
| action | 了解扩展链接 | `div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-external-link:nth-of-type(4) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > a.video-form-item-link:nth-of-type(1)` |
| region | 谁可以看 公开粉丝可见仅我可见 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-form-bone.video-form-advanced:nth-of-type(2) > div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-privacy:nth-of-type(5)` |
| action | 公开 | `div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-privacy:nth-of-type(5) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.byte-radio-group.byte-radio-size-default.byte-radio-mode-outline:nth-of-type(1) > label.byte-radio:nth-of-type(1)` |
| action | 粉丝可见 | `div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-privacy:nth-of-type(5) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.byte-radio-group.byte-radio-size-default.byte-radio-mode-outline:nth-of-type(1) > label.byte-radio:nth-of-type(2)` |
| action | 仅我可见 | `div.video-form-wrapper:nth-of-type(2) > div.video-form-item.form-item-privacy:nth-of-type(5) > div.video-form-item-wrapper:nth-of-type(2) > div.video-form-item-control:nth-of-type(1) > div.byte-radio-group.byte-radio-size-default.byte-radio-mode-outline:nth-of-type(1) > label.byte-radio:nth-of-type(3)` |
| action | 存草稿 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-batch-footer:nth-of-type(3) > div.button-group:nth-of-type(1) > button.byte-btn.byte-btn-default.byte-btn-size-large:nth-of-type(1)` |
| action | 定时发布 | `div.video-list-content:nth-of-type(2) > div.video-item.show:nth-of-type(1) > div.video-from-container:nth-of-type(2) > div.video-batch-footer:nth-of-type(3) > div.button-group:nth-of-type(1) > button.byte-btn.byte-btn-default.byte-btn-size-large:nth-of-type(2)` |
| action | 发布 | `button[data-wkswitch="disable-auto-publish"]` |
| action | 常见问题 | `div.pgc-wrapper.pgc-index.is-full-screen:nth-of-type(1) > div.pgc-feedback:nth-of-type(4) > div.fb-sidebar:nth-of-type(1) > div:nth-of-type(1) > div.feedback-container:nth-of-type(2) > a.feedback-wrapper.feedback-questions:nth-of-type(1)` |
| action | 重选封面 | `div#tc-ie-base-content > div.tc-ie-base:nth-of-type(2) > div.base-content-wrap:nth-of-type(2) > div.footer-btns:nth-of-type(3) > div.btns:nth-of-type(3) > button.btn-l.btn-cancel:nth-of-type(1)` |
| action | 确定 | `div#tc-ie-base-content > div.tc-ie-base:nth-of-type(2) > div.base-content-wrap:nth-of-type(2) > div.footer-btns:nth-of-type(3) > div.btns:nth-of-type(3) > button.btn-l.btn-sure.ml16:nth-of-type(2)` |
| action | 取消 | `div.Dialog-container:nth-of-type(7) > div.m-xigua-dialog.m-modal.m-dialog-edit:nth-of-type(1) > div.m-content:nth-of-type(2) > div.content:nth-of-type(1) > div.footer.undefined:nth-of-type(2) > button.m-button:nth-of-type(1)` |
| action | 确定 | `div.Dialog-container:nth-of-type(7) > div.m-xigua-dialog.m-modal.m-dialog-edit:nth-of-type(1) > div.m-content:nth-of-type(2) > div.content:nth-of-type(1) > div.footer.undefined:nth-of-type(2) > button.m-button.red.undefined:nth-of-type(2)` |

### work_management_real

- URL：`https://mp.toutiao.com/profile_v4/manage/content/all`
- 截图：`data/accounts/default/runs/selector-audit-20260611-131110/work_management_real.png`

| role | text | selector |
|---|---|---|
| action | 头条号 | `div#masterRoot > div.pgc-wrapper.pgc-index.manage_content_all-wrapper:nth-of-type(1) > div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > a.shead_logo:nth-of-type(1)` |
| action | 消息 | `div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > div.shead_right:nth-of-type(1) > div.sys-msg:nth-of-type(1) > div:nth-of-type(1) > a.sys-msg-entity:nth-of-type(1)` |
| action | 不敬业的码农 | `div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > div.shead_right:nth-of-type(1) > div.user-panel:nth-of-type(3) > div.information:nth-of-type(1) > a:nth-of-type(1)` |
| action | 主页 | `div.byte-layout-sider-children:nth-of-type(1) > div.mp-menu-wrapper.f-min-scroll.f-hover-scroll:nth-of-type(1) > div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-item.主页_tab:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 文章 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.base_creation_tab:nth-of-type(2) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 视频 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.base_creation_tab:nth-of-type(2) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(2) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 微头条 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.base_creation_tab:nth-of-type(2) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 音频 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.base_creation_tab:nth-of-type(2) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(4) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 作品管理 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.management_tab:nth-of-type(3) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 评论管理 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.management_tab:nth-of-type(3) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(2) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 草稿箱 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.management_tab:nth-of-type(3) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 收益数据 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.data_helper_tab:nth-of-type(4) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 作品数据 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.data_helper_tab:nth-of-type(4) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(2) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 粉丝数据 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.data_helper_tab:nth-of-type(4) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 提现 | `div.byte-layout-sider-children:nth-of-type(1) > div.mp-menu-wrapper.f-min-scroll.f-hover-scroll:nth-of-type(1) > div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-item.提现_tab:nth-of-type(6) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 创作权益 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.guide_tab:nth-of-type(7) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(2) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 头条认证 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.guide_tab:nth-of-type(7) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 创作灵感 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.guide_tab:nth-of-type(7) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(4) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 创作训练营 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.guide_tab:nth-of-type(7) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(5) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 功能实验室 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.tools_tab:nth-of-type(8) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 创作保护 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.tools_tab:nth-of-type(8) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 图片素材 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.tools_tab:nth-of-type(8) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(4) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 设置 | `div.byte-layout-sider-children:nth-of-type(1) > div.mp-menu-wrapper.f-min-scroll.f-hover-scroll:nth-of-type(1) > div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-item.设置_tab:nth-of-type(9) > span:nth-of-type(1) > a:nth-of-type(1)` |
| region | 全部 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(1)` |
| region | 文章 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(2)` |
| region | 视频 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(3)` |
| region | 微头条 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(4)` |
| region | 小视频 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(5)` |
| region | 音频 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(6)` |
| region | 合集 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(7)` |
| region | 草稿箱 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(9)` |
| region | 全部 | `div#root > div.all-content:nth-of-type(1) > div.filter-wrapper:nth-of-type(1) > div.filter-field.status-filter-list:nth-of-type(1) > span.filter-item:nth-of-type(2)` |
| region | 已发布 | `div#root > div.all-content:nth-of-type(1) > div.filter-wrapper:nth-of-type(1) > div.filter-field.status-filter-list:nth-of-type(1) > span.filter-item.unselected:nth-of-type(3)` |
| region | 审核中 | `div#root > div.all-content:nth-of-type(1) > div.filter-wrapper:nth-of-type(1) > div.filter-field.status-filter-list:nth-of-type(1) > span.filter-item.unselected:nth-of-type(4)` |
| region | 未通过 | `div#root > div.all-content:nth-of-type(1) > div.filter-wrapper:nth-of-type(1) > div.filter-field.status-filter-list:nth-of-type(1) > span.filter-item.unselected:nth-of-type(5)` |
| region | 仅我可见 | `div#root > div.all-content:nth-of-type(1) > div.filter-wrapper:nth-of-type(1) > div.filter-field.status-filter-list:nth-of-type(1) > span.filter-item.unselected:nth-of-type(6)` |
| region | ~ | `div#root > div.all-content:nth-of-type(1) > div.filter-wrapper:nth-of-type(1) > div.filter-right-field:nth-of-type(2) > div.filter-item.time-range.mg-right:nth-of-type(2)` |
| input | 开始日期 | `input[placeholder="开始日期"]` |
| input | 结束日期 | `input[placeholder="结束日期"]` |
| input | 搜索关键词 | `input[placeholder="搜索关键词"]` |
| action | 程序员用AI，已经从尝鲜变成日常了 | `div.genre-item.genre-item-in-all-tab:nth-of-type(1) > div.article-card:nth-of-type(1) > div.article-card-wrap:nth-of-type(1) > div.article-card-bone:nth-of-type(1) > div.title-wrap:nth-of-type(1) > a.title:nth-of-type(1)` |
| action |  | `div.all-content-list:nth-of-type(2) > div:nth-of-type(5) > div.genre-item.genre-item-in-all-tab:nth-of-type(1) > div.article-card:nth-of-type(1) > div.article-card-wrap:nth-of-type(1) > a.image:nth-of-type(1)` |
| action |  | `div.all-content-list:nth-of-type(2) > div:nth-of-type(6) > div.genre-item.genre-item-in-all-tab:nth-of-type(1) > div.article-card:nth-of-type(1) > div.article-card-wrap:nth-of-type(1) > a.image:nth-of-type(1)` |
| action |  | `div.all-content-list:nth-of-type(2) > div:nth-of-type(7) > div.genre-item.genre-item-in-all-tab:nth-of-type(1) > div.article-card:nth-of-type(1) > div.article-card-wrap:nth-of-type(1) > a.image:nth-of-type(1)` |
| action |  | `div.all-content-list:nth-of-type(2) > div:nth-of-type(9) > div.genre-item.genre-item-in-all-tab:nth-of-type(1) > div.article-card:nth-of-type(1) > div.article-card-wrap:nth-of-type(1) > a.image:nth-of-type(1)` |
| action |  | `div.all-content-list:nth-of-type(2) > div:nth-of-type(10) > div.genre-item.genre-item-in-all-tab:nth-of-type(1) > div.article-card:nth-of-type(1) > div.article-card-wrap:nth-of-type(1) > a.image:nth-of-type(1)` |
| action |  | `div.all-content-list:nth-of-type(2) > div:nth-of-type(11) > div.genre-item.genre-item-in-all-tab:nth-of-type(1) > div.article-card:nth-of-type(1) > div.article-card-wrap:nth-of-type(1) > a.image:nth-of-type(1)` |
| action | 关于今日头条 | `div#masterRoot > div.pgc-wrapper.pgc-index.manage_content_all-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_about:nth-of-type(1)` |
| action | 用户协议 | `div#masterRoot > div.pgc-wrapper.pgc-index.manage_content_all-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_agreement:nth-of-type(2)` |
| action | 隐私政策 | `div#masterRoot > div.pgc-wrapper.pgc-index.manage_content_all-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_agreement:nth-of-type(3)` |
| action | 社区规范 | `div#masterRoot > div.pgc-wrapper.pgc-index.manage_content_all-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_operation:nth-of-type(4)` |
| action | 自律公约 | `div#masterRoot > div.pgc-wrapper.pgc-index.manage_content_all-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_agreement:nth-of-type(5)` |
| action | 侵权投诉 | `div.pgc-wrapper.pgc-index.manage_content_all-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > span:nth-of-type(6) > a.sfoot_agreement:nth-of-type(1)` |
| action | 联系我们 | `div#masterRoot > div.pgc-wrapper.pgc-index.manage_content_all-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_contact:nth-of-type(6)` |
| action | 常见问题 | `div.pgc-wrapper.pgc-index.manage_content_all-wrapper:nth-of-type(1) > div.pgc-feedback:nth-of-type(5) > div.fb-sidebar:nth-of-type(1) > div:nth-of-type(1) > div.feedback-container:nth-of-type(2) > a.feedback-wrapper.feedback-questions:nth-of-type(1)` |

### work_tab_article

- URL：`https://mp.toutiao.com/profile_v4/graphic/articles`
- 截图：`data/accounts/default/runs/selector-audit-20260611-131110/work_tab_article.png`

| role | text | selector |
|---|---|---|
| action | 头条号 | `div#masterRoot > div.pgc-wrapper.pgc-index.graphic_articles-wrapper:nth-of-type(1) > div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > a.shead_logo:nth-of-type(1)` |
| action | 消息 | `div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > div.shead_right:nth-of-type(1) > div.sys-msg:nth-of-type(1) > div:nth-of-type(1) > a.sys-msg-entity:nth-of-type(1)` |
| action | 不敬业的码农 | `div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > div.shead_right:nth-of-type(1) > div.user-panel:nth-of-type(3) > div.information:nth-of-type(1) > a:nth-of-type(1)` |
| action | 主页 | `div.byte-layout-sider-children:nth-of-type(1) > div.mp-menu-wrapper.f-min-scroll.f-hover-scroll:nth-of-type(1) > div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-item.主页_tab:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 文章 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.base_creation_tab:nth-of-type(2) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 视频 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.base_creation_tab:nth-of-type(2) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(2) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 微头条 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.base_creation_tab:nth-of-type(2) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 音频 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.base_creation_tab:nth-of-type(2) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(4) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 作品管理 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.management_tab:nth-of-type(3) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 评论管理 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.management_tab:nth-of-type(3) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(2) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 草稿箱 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.management_tab:nth-of-type(3) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 收益数据 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.data_helper_tab:nth-of-type(4) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 作品数据 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.data_helper_tab:nth-of-type(4) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(2) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 粉丝数据 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.data_helper_tab:nth-of-type(4) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 提现 | `div.byte-layout-sider-children:nth-of-type(1) > div.mp-menu-wrapper.f-min-scroll.f-hover-scroll:nth-of-type(1) > div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-item.提现_tab:nth-of-type(6) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 创作权益 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.guide_tab:nth-of-type(7) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(2) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 头条认证 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.guide_tab:nth-of-type(7) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 创作灵感 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.guide_tab:nth-of-type(7) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(4) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 创作训练营 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.guide_tab:nth-of-type(7) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(5) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 功能实验室 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.tools_tab:nth-of-type(8) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 创作保护 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.tools_tab:nth-of-type(8) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 图片素材 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.tools_tab:nth-of-type(8) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(4) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 设置 | `div.byte-layout-sider-children:nth-of-type(1) > div.mp-menu-wrapper.f-min-scroll.f-hover-scroll:nth-of-type(1) > div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-item.设置_tab:nth-of-type(9) > span:nth-of-type(1) > a:nth-of-type(1)` |
| region | 全部 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(1)` |
| region | 文章 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(2)` |
| region | 视频 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(3)` |
| region | 微头条 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(4)` |
| region | 小视频 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(5)` |
| region | 音频 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(6)` |
| region | 合集 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(7)` |
| region | 草稿箱 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(9)` |
| region | 全部 | `div#root > div.articles-wrapper:nth-of-type(1) > div.shared-filter-wrapper:nth-of-type(1) > div.filter-field:nth-of-type(1) > span.filter-item:nth-of-type(2)` |
| region | 已发布 | `div#root > div.articles-wrapper:nth-of-type(1) > div.shared-filter-wrapper:nth-of-type(1) > div.filter-field:nth-of-type(1) > span.filter-item.unselected:nth-of-type(3)` |
| region | 审核中 | `div#root > div.articles-wrapper:nth-of-type(1) > div.shared-filter-wrapper:nth-of-type(1) > div.filter-field:nth-of-type(1) > span.filter-item.unselected:nth-of-type(4)` |
| region | 审核未通过 | `div#root > div.articles-wrapper:nth-of-type(1) > div.shared-filter-wrapper:nth-of-type(1) > div.filter-field:nth-of-type(1) > span.filter-item.unselected:nth-of-type(5)` |
| region | 仅我可见 | `div#root > div.articles-wrapper:nth-of-type(1) > div.shared-filter-wrapper:nth-of-type(1) > div.filter-field:nth-of-type(1) > span.filter-item.unselected:nth-of-type(6)` |
| region | ~ | `div#root > div.articles-wrapper:nth-of-type(1) > div.shared-filter-wrapper:nth-of-type(1) > div.filter-right-field.right:nth-of-type(2) > div.filter-item.time-range.mg-right:nth-of-type(1)` |
| input | 开始日期 | `input[placeholder="开始日期"]` |
| input | 结束日期 | `input[placeholder="结束日期"]` |
| input | 搜索关键词 | `input[placeholder="搜索关键词"]` |
| action | 程序员用AI，已经从尝鲜变成日常了 | `div.article-list:nth-of-type(1) > div.article-card:nth-of-type(2) > div.article-card-wrap:nth-of-type(1) > div.article-card-bone:nth-of-type(1) > div.title-wrap:nth-of-type(1) > a.title:nth-of-type(1)` |
| action |  | `div.articles-wrapper:nth-of-type(1) > div.articles-contents:nth-of-type(2) > div.article-list:nth-of-type(1) > div.article-card:nth-of-type(3) > div.article-card-wrap:nth-of-type(1) > a.image:nth-of-type(1)` |
| action | AI省下的时间，为什么又被工作填满了？ | `div.article-list:nth-of-type(1) > div.article-card:nth-of-type(3) > div.article-card-wrap:nth-of-type(1) > div.article-card-bone:nth-of-type(1) > div.title-wrap:nth-of-type(1) > a.title:nth-of-type(1)` |
| action |  | `div.articles-wrapper:nth-of-type(1) > div.articles-contents:nth-of-type(2) > div.article-list:nth-of-type(1) > div.article-card:nth-of-type(4) > div.article-card-wrap:nth-of-type(1) > a.image:nth-of-type(1)` |
| action | 用AI做清单，能减少很多低级遗漏 | `div.article-list:nth-of-type(1) > div.article-card:nth-of-type(4) > div.article-card-wrap:nth-of-type(1) > div.article-card-bone:nth-of-type(1) > div.title-wrap:nth-of-type(1) > a.title:nth-of-type(1)` |
| action |  | `div.articles-wrapper:nth-of-type(1) > div.articles-contents:nth-of-type(2) > div.article-list:nth-of-type(1) > div.article-card:nth-of-type(5) > div.article-card-wrap:nth-of-type(1) > a.image:nth-of-type(1)` |
| action | 用AI做笔记，关键不是记录更多，而是整理更清楚 | `div.article-list:nth-of-type(1) > div.article-card:nth-of-type(5) > div.article-card-wrap:nth-of-type(1) > div.article-card-bone:nth-of-type(1) > div.title-wrap:nth-of-type(1) > a.title:nth-of-type(1)` |
| action | 工作赚钱与身体健康，究竟谁更重要？ | `div.article-list:nth-of-type(1) > div.article-card:nth-of-type(6) > div.article-card-wrap:nth-of-type(1) > div.article-card-bone:nth-of-type(1) > div.title-wrap:nth-of-type(1) > a.title:nth-of-type(1)` |
| action |  | `div.articles-wrapper:nth-of-type(1) > div.articles-contents:nth-of-type(2) > div.article-list:nth-of-type(1) > div.article-card:nth-of-type(7) > div.article-card-wrap:nth-of-type(1) > a.image:nth-of-type(1)` |
| action | 普通人如何用AI提升每天的工作效率 | `div.article-list:nth-of-type(1) > div.article-card:nth-of-type(7) > div.article-card-wrap:nth-of-type(1) > div.article-card-bone:nth-of-type(1) > div.title-wrap:nth-of-type(1) > a.title:nth-of-type(1)` |
| action |  | `div.articles-wrapper:nth-of-type(1) > div.articles-contents:nth-of-type(2) > div.article-list:nth-of-type(1) > div.article-card:nth-of-type(8) > div.article-card-wrap:nth-of-type(1) > a.image:nth-of-type(1)` |
| action | 京东的AI硬件选秀，究竟在“秀”什么？ | `div.article-list:nth-of-type(1) > div.article-card:nth-of-type(8) > div.article-card-wrap:nth-of-type(1) > div.article-card-bone:nth-of-type(1) > div.title-wrap:nth-of-type(1) > a.title:nth-of-type(1)` |
| action |  | `div.articles-wrapper:nth-of-type(1) > div.articles-contents:nth-of-type(2) > div.article-list:nth-of-type(1) > div.article-card:nth-of-type(9) > div.article-card-wrap:nth-of-type(1) > a.image:nth-of-type(1)` |
| action | 《程序媛：互联网稀有物种图鉴》 | `div.article-list:nth-of-type(1) > div.article-card:nth-of-type(9) > div.article-card-wrap:nth-of-type(1) > div.article-card-bone:nth-of-type(1) > div.title-wrap:nth-of-type(1) > a.title:nth-of-type(1)` |
| action |  | `div.articles-wrapper:nth-of-type(1) > div.articles-contents:nth-of-type(2) > div.article-list:nth-of-type(1) > div.article-card:nth-of-type(10) > div.article-card-wrap:nth-of-type(1) > a.image:nth-of-type(1)` |
| action | 硅谷版《延禧攻略》，到底哪位科技大佬才是真正的魏璎珞？ | `div.article-list:nth-of-type(1) > div.article-card:nth-of-type(10) > div.article-card-wrap:nth-of-type(1) > div.article-card-bone:nth-of-type(1) > div.title-wrap:nth-of-type(1) > a.title:nth-of-type(1)` |
| action |  | `div.articles-wrapper:nth-of-type(1) > div.articles-contents:nth-of-type(2) > div.article-list:nth-of-type(1) > div.article-card:nth-of-type(11) > div.article-card-wrap:nth-of-type(1) > a.image:nth-of-type(1)` |
| action | 程序员零点睡觉被领导怒批：零点睡觉的你也配在我企业工作？ | `div.article-list:nth-of-type(1) > div.article-card:nth-of-type(11) > div.article-card-wrap:nth-of-type(1) > div.article-card-bone:nth-of-type(1) > div.title-wrap:nth-of-type(1) > a.title:nth-of-type(1)` |
| action | 关于今日头条 | `div#masterRoot > div.pgc-wrapper.pgc-index.graphic_articles-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_about:nth-of-type(1)` |
| action | 用户协议 | `div#masterRoot > div.pgc-wrapper.pgc-index.graphic_articles-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_agreement:nth-of-type(2)` |
| action | 隐私政策 | `div#masterRoot > div.pgc-wrapper.pgc-index.graphic_articles-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_agreement:nth-of-type(3)` |
| action | 社区规范 | `div#masterRoot > div.pgc-wrapper.pgc-index.graphic_articles-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_operation:nth-of-type(4)` |
| action | 自律公约 | `div#masterRoot > div.pgc-wrapper.pgc-index.graphic_articles-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_agreement:nth-of-type(5)` |
| action | 侵权投诉 | `div.pgc-wrapper.pgc-index.graphic_articles-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > span:nth-of-type(6) > a.sfoot_agreement:nth-of-type(1)` |
| action | 联系我们 | `div#masterRoot > div.pgc-wrapper.pgc-index.graphic_articles-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_contact:nth-of-type(6)` |
| action | 常见问题 | `div.pgc-wrapper.pgc-index.graphic_articles-wrapper:nth-of-type(1) > div.pgc-feedback:nth-of-type(5) > div.fb-sidebar:nth-of-type(1) > div:nth-of-type(1) > div.feedback-container:nth-of-type(2) > a.feedback-wrapper.feedback-questions:nth-of-type(1)` |

### work_tab_video

- URL：`https://mp.toutiao.com/profile_v4/xigua/content-manage-v2`
- 截图：`data/accounts/default/runs/selector-audit-20260611-131110/work_tab_video.png`

| role | text | selector |
|---|---|---|
| action | 头条号 | `div#masterRoot > div.pgc-wrapper.pgc-index.xigua_content-manage-v2-wrapper:nth-of-type(1) > div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > a.shead_logo:nth-of-type(1)` |
| action | 消息 | `div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > div.shead_right:nth-of-type(1) > div.sys-msg:nth-of-type(1) > div:nth-of-type(1) > a.sys-msg-entity:nth-of-type(1)` |
| action | 不敬业的码农 | `div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > div.shead_right:nth-of-type(1) > div.user-panel:nth-of-type(3) > div.information:nth-of-type(1) > a:nth-of-type(1)` |
| action | 主页 | `div.byte-layout-sider-children:nth-of-type(1) > div.mp-menu-wrapper.f-min-scroll.f-hover-scroll:nth-of-type(1) > div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-item.主页_tab:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 文章 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.base_creation_tab:nth-of-type(2) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 视频 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.base_creation_tab:nth-of-type(2) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(2) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 微头条 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.base_creation_tab:nth-of-type(2) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 音频 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.base_creation_tab:nth-of-type(2) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(4) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 作品管理 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.management_tab:nth-of-type(3) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 评论管理 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.management_tab:nth-of-type(3) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(2) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 草稿箱 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.management_tab:nth-of-type(3) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 收益数据 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.data_helper_tab:nth-of-type(4) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 作品数据 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.data_helper_tab:nth-of-type(4) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(2) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 粉丝数据 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.data_helper_tab:nth-of-type(4) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 提现 | `div.byte-layout-sider-children:nth-of-type(1) > div.mp-menu-wrapper.f-min-scroll.f-hover-scroll:nth-of-type(1) > div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-item.提现_tab:nth-of-type(6) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 创作权益 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.guide_tab:nth-of-type(7) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(2) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 头条认证 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.guide_tab:nth-of-type(7) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 创作灵感 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.guide_tab:nth-of-type(7) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(4) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 创作训练营 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.guide_tab:nth-of-type(7) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(5) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 功能实验室 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.tools_tab:nth-of-type(8) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 创作保护 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.tools_tab:nth-of-type(8) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 图片素材 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.tools_tab:nth-of-type(8) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(4) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 设置 | `div.byte-layout-sider-children:nth-of-type(1) > div.mp-menu-wrapper.f-min-scroll.f-hover-scroll:nth-of-type(1) > div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-item.设置_tab:nth-of-type(9) > span:nth-of-type(1) > a:nth-of-type(1)` |
| region | 全部 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(1)` |
| region | 文章 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(2)` |
| region | 视频 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(3)` |
| region | 微头条 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(4)` |
| region | 小视频 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(5)` |
| region | 音频 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(6)` |
| region | 合集 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(7)` |
| region | 草稿箱 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(9)` |
| region | 全部 | `div.m-title:nth-of-type(1) > div.video-manage-filters:nth-of-type(1) > div.filter-group:nth-of-type(1) > div.large-filter:nth-of-type(1) > span.filter-items:nth-of-type(2) > span.filter-item:nth-of-type(1)` |
| region | 已发布 | `div.m-title:nth-of-type(1) > div.video-manage-filters:nth-of-type(1) > div.filter-group:nth-of-type(1) > div.large-filter:nth-of-type(1) > span.filter-items:nth-of-type(2) > span.filter-item:nth-of-type(2)` |
| region | 未通过 | `div.m-title:nth-of-type(1) > div.video-manage-filters:nth-of-type(1) > div.filter-group:nth-of-type(1) > div.large-filter:nth-of-type(1) > span.filter-items:nth-of-type(2) > span.filter-item:nth-of-type(3)` |
| region | 仅我可见 | `div.m-title:nth-of-type(1) > div.video-manage-filters:nth-of-type(1) > div.filter-group:nth-of-type(1) > div.large-filter:nth-of-type(1) > span.filter-items:nth-of-type(2) > span.filter-item:nth-of-type(4)` |
| region | ~ | `div.m-pgc-video-manage:nth-of-type(1) > div.m-title:nth-of-type(1) > div.video-manage-filters:nth-of-type(1) > div.filter-inputs:nth-of-type(2) > div.filter-group.time-filter:nth-of-type(1) > span.filter-item:nth-of-type(1)` |
| input | 开始日期 | `input[placeholder="开始日期"]` |
| input | 结束日期 | `input[placeholder="结束日期"]` |
| input | 搜索关键词 | `input[placeholder="搜索关键词"]` |
| action | 开始创作 | `div#root > div.m-pgc-video-manage:nth-of-type(1) > div.m-articles:nth-of-type(2) > div.xigua-component-video-no-content:nth-of-type(1) > button.byte-btn.byte-btn-primary.byte-btn-size-default:nth-of-type(1)` |
| action | 关于今日头条 | `div#masterRoot > div.pgc-wrapper.pgc-index.xigua_content-manage-v2-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_about:nth-of-type(1)` |
| action | 用户协议 | `div#masterRoot > div.pgc-wrapper.pgc-index.xigua_content-manage-v2-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_agreement:nth-of-type(2)` |
| action | 隐私政策 | `div#masterRoot > div.pgc-wrapper.pgc-index.xigua_content-manage-v2-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_agreement:nth-of-type(3)` |
| action | 社区规范 | `div#masterRoot > div.pgc-wrapper.pgc-index.xigua_content-manage-v2-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_operation:nth-of-type(4)` |
| action | 自律公约 | `div#masterRoot > div.pgc-wrapper.pgc-index.xigua_content-manage-v2-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_agreement:nth-of-type(5)` |
| action | 侵权投诉 | `div.pgc-wrapper.pgc-index.xigua_content-manage-v2-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > span:nth-of-type(6) > a.sfoot_agreement:nth-of-type(1)` |
| action | 联系我们 | `div#masterRoot > div.pgc-wrapper.pgc-index.xigua_content-manage-v2-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_contact:nth-of-type(6)` |
| action | 常见问题 | `div.pgc-wrapper.pgc-index.xigua_content-manage-v2-wrapper:nth-of-type(1) > div.pgc-feedback:nth-of-type(5) > div.fb-sidebar:nth-of-type(1) > div:nth-of-type(1) > div.feedback-container:nth-of-type(2) > a.feedback-wrapper.feedback-questions:nth-of-type(1)` |
| action | 我知道了 | `body:nth-of-type(1) > div.Popover.Popover-below.menu-tip-popover:nth-of-type(3) > div.Popover-body:nth-of-type(1) > div.tips-container:nth-of-type(1) > div.tips-footer:nth-of-type(2) > button.byte-btn.byte-btn-text.byte-btn-size-default:nth-of-type(1)` |

### work_tab_weitoutiao

- URL：`https://mp.toutiao.com/profile_v4/weitoutiao`
- 截图：`data/accounts/default/runs/selector-audit-20260611-131110/work_tab_weitoutiao.png`

| role | text | selector |
|---|---|---|
| action | 头条号 | `div#masterRoot > div.pgc-wrapper.pgc-index.weitoutiao-wrapper:nth-of-type(1) > div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > a.shead_logo:nth-of-type(1)` |
| action | 消息 | `div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > div.shead_right:nth-of-type(1) > div.sys-msg:nth-of-type(1) > div:nth-of-type(1) > a.sys-msg-entity:nth-of-type(1)` |
| action | 不敬业的码农 | `div.garr-header:nth-of-type(1) > div.shead_wrap:nth-of-type(1) > div.shead_right:nth-of-type(1) > div.user-panel:nth-of-type(3) > div.information:nth-of-type(1) > a:nth-of-type(1)` |
| action | 主页 | `div.byte-layout-sider-children:nth-of-type(1) > div.mp-menu-wrapper.f-min-scroll.f-hover-scroll:nth-of-type(1) > div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-item.主页_tab:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 文章 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.base_creation_tab:nth-of-type(2) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 视频 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.base_creation_tab:nth-of-type(2) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(2) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 微头条 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.base_creation_tab:nth-of-type(2) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 音频 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.base_creation_tab:nth-of-type(2) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(4) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 作品管理 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.management_tab:nth-of-type(3) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 评论管理 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.management_tab:nth-of-type(3) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(2) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 草稿箱 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.management_tab:nth-of-type(3) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 收益数据 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.data_helper_tab:nth-of-type(4) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 作品数据 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.data_helper_tab:nth-of-type(4) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(2) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 粉丝数据 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.data_helper_tab:nth-of-type(4) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 提现 | `div.byte-layout-sider-children:nth-of-type(1) > div.mp-menu-wrapper.f-min-scroll.f-hover-scroll:nth-of-type(1) > div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-item.提现_tab:nth-of-type(6) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 创作权益 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.guide_tab:nth-of-type(7) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(2) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 头条认证 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.guide_tab:nth-of-type(7) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 创作灵感 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.guide_tab:nth-of-type(7) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(4) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 创作训练营 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.guide_tab:nth-of-type(7) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(5) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 功能实验室 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.tools_tab:nth-of-type(8) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(1) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 创作保护 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.tools_tab:nth-of-type(8) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(3) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 图片素材 | `div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-inline.tools_tab:nth-of-type(8) > div.byte-menu-inline-content:nth-of-type(2) > div.byte-menu-item:nth-of-type(4) > span:nth-of-type(1) > a:nth-of-type(1)` |
| action | 设置 | `div.byte-layout-sider-children:nth-of-type(1) > div.mp-menu-wrapper.f-min-scroll.f-hover-scroll:nth-of-type(1) > div.byte-menu.garr-menu:nth-of-type(1) > div.byte-menu-item.设置_tab:nth-of-type(9) > span:nth-of-type(1) > a:nth-of-type(1)` |
| region | 全部 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(1)` |
| region | 文章 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(2)` |
| region | 视频 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(3)` |
| region | 微头条 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(4)` |
| region | 小视频 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(5)` |
| region | 音频 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(6)` |
| region | 合集 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(7)` |
| region | 草稿箱 | `div.work-manage-header.menu-tab-wrapper.sticky:nth-of-type(2) > div.byte-tabs.byte-tabs-horizontal.byte-tabs-line:nth-of-type(1) > div.byte-tabs-header-nav.byte-tabs-header-nav-horizontal.byte-tabs-header-size-default:nth-of-type(1) > div.byte-tabs-header-wrapper:nth-of-type(1) > div.byte-tabs-header:nth-of-type(1) > div.byte-tabs-header-title:nth-of-type(9)` |
| region | 全部 | `div#root > div.wtt-content:nth-of-type(1) > div.shared-filter-wrapper.wtt-filter:nth-of-type(1) > div.filter-field:nth-of-type(1) > span.filter-item:nth-of-type(2)` |
| region | 已发布 | `div#root > div.wtt-content:nth-of-type(1) > div.shared-filter-wrapper.wtt-filter:nth-of-type(1) > div.filter-field:nth-of-type(1) > span.filter-item.unselected:nth-of-type(3)` |
| region | 审核中 | `div#root > div.wtt-content:nth-of-type(1) > div.shared-filter-wrapper.wtt-filter:nth-of-type(1) > div.filter-field:nth-of-type(1) > span.filter-item.unselected:nth-of-type(4)` |
| region | 审核未通过 | `div#root > div.wtt-content:nth-of-type(1) > div.shared-filter-wrapper.wtt-filter:nth-of-type(1) > div.filter-field:nth-of-type(1) > span.filter-item.unselected:nth-of-type(5)` |
| region | 仅我可见 | `div#root > div.wtt-content:nth-of-type(1) > div.shared-filter-wrapper.wtt-filter:nth-of-type(1) > div.filter-field:nth-of-type(1) > span.filter-item.unselected:nth-of-type(6)` |
| region | ~ | `div#root > div.wtt-content:nth-of-type(1) > div.shared-filter-wrapper.wtt-filter:nth-of-type(1) > div.filter-right-field.right:nth-of-type(2) > div.filter-item.time-range.mg-right:nth-of-type(1)` |
| input | 开始日期 | `input[placeholder="开始日期"]` |
| input | 结束日期 | `input[placeholder="结束日期"]` |
| action | 关于今日头条 | `div#masterRoot > div.pgc-wrapper.pgc-index.weitoutiao-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_about:nth-of-type(1)` |
| action | 用户协议 | `div#masterRoot > div.pgc-wrapper.pgc-index.weitoutiao-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_agreement:nth-of-type(2)` |
| action | 隐私政策 | `div#masterRoot > div.pgc-wrapper.pgc-index.weitoutiao-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_agreement:nth-of-type(3)` |
| action | 社区规范 | `div#masterRoot > div.pgc-wrapper.pgc-index.weitoutiao-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_operation:nth-of-type(4)` |
| action | 自律公约 | `div#masterRoot > div.pgc-wrapper.pgc-index.weitoutiao-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_agreement:nth-of-type(5)` |
| action | 侵权投诉 | `div.pgc-wrapper.pgc-index.weitoutiao-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > span:nth-of-type(6) > a.sfoot_agreement:nth-of-type(1)` |
| action | 联系我们 | `div#masterRoot > div.pgc-wrapper.pgc-index.weitoutiao-wrapper:nth-of-type(1) > div.pgc-footer:nth-of-type(4) > div.sfoot:nth-of-type(1) > div:nth-of-type(1) > a.sfoot_contact:nth-of-type(6)` |
| action | 常见问题 | `div.pgc-wrapper.pgc-index.weitoutiao-wrapper:nth-of-type(1) > div.pgc-feedback:nth-of-type(5) > div.fb-sidebar:nth-of-type(1) > div:nth-of-type(1) > div.feedback-container:nth-of-type(2) > a.feedback-wrapper.feedback-questions:nth-of-type(1)` |
