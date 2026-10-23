# 视频拆解工厂 · 开整

Apple Silicon / macOS 14.2+ 的本地视频模板工作台。

## 3.0.11 下载验收

- [下载开整 3.0.11](https://github.com/ddengzc/video-disassembly-factory-downloads/releases/tag/v3.0.11)
- [固定运行组件与模型](https://github.com/ddengzc/video-disassembly-factory-downloads/releases/tag/components-v2.0.0)

3.0.11 按预发布提供。解压后打开“开整.app”。已有用户复用共享工作目录和已安装组件，升级前退出旧应用；不删除任务或成果目录。首次使用安装 8 项固定组件约 1.22 GB，不再下载本地标点模型。

本次累计包含全局 UI、日期/批次/任务历史、素材确认及导出、文案有效性/完整性保护、组件状态、凭据授权和配置跳转，并修复带 modal_id 的抖音链接截断。

统一分类/音色预设 **1.0.0** 已发布：模板分类和音色各三条，详见 [统一预设库](presets/README.md)。3.0.11 启动时检查一次，也可在对应页面点击“检查更新”；通过签名验证后更新本地缓存，失败继续使用原配置。已开始任务保留原配置，变化的旧选项须重新选择。本次不需要重新下载应用。

源码及两份维护交接文档保存在私有维护仓库。公开包不含任务、视频、Cookie、API 密钥或配置签名私钥；不向用户要求 GitHub Token。音色只是模板导出字段，不在本机执行 TTS。

验证：156 项 Python、21 组 UI、108 分镜导出/原视频还原、切片画面和音轨等价检查、GitHub CI 与隔离工作目录核心启动通过。另一台 Mac、当前包原生窗口完整业务、真实视频全面准确率、远端预设和外部系统联调仍待验收。ad-hoc 签名，未做 Developer ID 公证。

源码提交：69aec1a0adf0a1e483952e263147ec115530597a。

应用 ZIP SHA-256：`9f6759fc8a87015704034c7a9beb7574842d4b502dd07a75ac0731d96b36458c`。

## 版本与组件管理

应用、组件和预设独立管理。8 项组件内容未变，继续复用 components-v2.0.0 的固定 URL、SHA-256 和文件清单，不重复上传模型。旧应用、标签、组件及历史草稿全部保留，旧版标点附件仍供回退引用，不在本次清理。

见 [发布与保留规则](RELEASE_POLICY.md)、[版本历史](releases/history.json)、[3.0.11 验证记录](releases/validation-v3.0.11.json) 和 [组件基线](releases/components-baseline-2.0.0.json)。
