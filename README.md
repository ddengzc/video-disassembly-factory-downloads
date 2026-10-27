# 视频模版工作台 · 应用与固定组件下载

Apple Silicon / macOS14.2+ 的视频模版工作台。当前版本 **3.0.28（预发布）**。

**[下载应用ZIP](https://github.com/ddengzc/video-disassembly-factory-downloads/releases/download/v3.0.28/kaizheng-mac-arm64-3.0.28.zip)** · [发布说明与全部附件](https://github.com/ddengzc/video-disassembly-factory-downloads/releases/tag/v3.0.28) · [校验摘要](https://github.com/ddengzc/video-disassembly-factory-downloads/releases/download/v3.0.28/SHA256SUMS.txt)

## 安装与升级

下载名称为`kaizheng-mac-arm64-3.0.28.zip`的附件，解压后打开包内的应用（实际 .app 文件名保持原样）。GitHub自动生成的Source code ZIP不是安装包。升级前退出旧应用；已有任务、登录凭据、固定组件和正式成果保留，同一时间运行一个版本。

首次按设置页安装8项固定组件、配置抖音登录和模型服务。组件约1.22GB，不重新安装旧标点模型。当前为ad-hoc签名，未做Developer ID公证，按macOS正常允许流程打开，不需要关闭系统安全保护。

## 3.0.28更新

- 音频、画面、字幕独立取证，成功工作复用，每个技术卡点最多自动补跑一次。
- 文案补标点与语义分段；局部疑问保留警告但不单独阻断，无文案、严重异常和处理失败仍要求处理。
- 支持生成批次暂停、继续、取消，保留成功结果。
- 素材显示名与分类分开编辑，可同步对应文件夹。
- 已完成文案可直接编辑，点击“保存文案并同步”更新原成果元数据，有备份和冲突/中断保护，不重做视频。

音色仅用于模板voiceId字段，本机不执行TTS。画面理解和文案整理使用用户配置的模型API，可能产生供应商费用。

## 下载与维护入口

| 内容 | 入口 |
| --- | --- |
| 当前应用、说明、摘要和来源 | [3.0.28 Release](https://github.com/ddengzc/video-disassembly-factory-downloads/releases/tag/v3.0.28) |
| 固定组件与必要对应源码 | [components-v2.0.0](https://github.com/ddengzc/video-disassembly-factory-downloads/releases/tag/components-v2.0.0) |
| 三条分类和三条音色 | [统一预设说明](presets/README.md) |
| 全部仓库、下载与常见问题 | [下载总览](DOWNLOADS.md) |
| 版本与保留状态 | [版本历史](releases/history.json) / [更新记录](CHANGELOG.md) |
| 本版验证 | [发布来源](releases/v3.0.28.json) / [回下载验证](releases/validation-v3.0.28.json) |
| 发布和保留规则 | [RELEASE_POLICY](RELEASE_POLICY.md) |
| 第三方许可 | [THIRD_PARTY](THIRD_PARTY.md) |
| 授权开发维护人员 | [私有源码与维护文档](https://github.com/ddengzc/video-disassembly-factory) |

分类/音色保持1.0.0/revision1，启动检查一次，支持手动更新，无定时重复请求。组件和预设独立版本，未变模型不重复上传；旧应用、标签、许可和所有仍被引用附件保留。

本版331项Python、27组UI、2组媒体回归及隔离WebKit和包检查通过，源码PR #7的GitHub CI通过。用户反馈本地整体正常。公开包已完成回下载摘要、解压、签名、版本/源码、隔离初始化与OCR检查；原生窗口完整业务、另一台Mac、全部视频准确率和外部联调仍分别验收，不能把自动测试当作全面准确率承诺。公开包不包含用户任务、私有视频、Cookie、API密钥或配置签名私钥。

问题反馈请提供版本、步骤和脱敏截图，不上传完整用户目录、凭据或私有视频，见[安全反馈](SECURITY.md)。
