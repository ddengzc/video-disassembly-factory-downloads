# 视频拆解工厂 · 开整

Apple Silicon / macOS 14.2+ 的本地视频模板工作台。

## V2.0 下载验收

- [下载开整 V2.0](https://github.com/ddengzc/video-disassembly-factory-downloads/releases/tag/v2.0.0)
- [固定运行组件与模型](https://github.com/ddengzc/video-disassembly-factory-downloads/releases/tag/components-v2.0.0)

V2.0 先按预发布提供下载与实际使用验收。原应用、旧标签和旧组件保留，等用户确认 V2.0 下载、打开和实际处理正常后再处理旧版本；仍被保留版本引用的组件不删除。

解压后打开“开整.app”。已有用户会复用原工作目录、组件与任务资料；首次使用需在设置中安装固定组件（约 2.2 GB），程序按 SHA-256 和逐文件清单校验。保留旧应用可用于回退，不删除工作目录。

本版本整合语义文案编辑、素材分类与动态预览、侧边播放器、工作区独立取消、并行生成和口播歌词分流。源码和自动化检查记录保存在项目维护仓库，下载包不包含用户任务、Cookie 或 API 密钥。

本地 ad-hoc 签名，未做 Developer ID 公证。新 Mac 首次启动可能需要通过 macOS 的正常允许流程；用户仍需验收真实视频处理和外部后台导入。问题反馈请附操作步骤及脱敏截图，不上传凭据或私有视频。

## 版本与组件管理

应用升级不会要求模型、插件和工具同步升版。固定组件内容未变时复用原 URL 与 SHA-256；当前完整组件基线供后续应用版本继续引用。见[发布与保留规则](RELEASE_POLICY.md)、[版本历史](releases/history.json)和[组件锁定索引](releases/components-baseline-2.0.0.json)。新版本实际验收通过前不删除旧版；仍被保留版本引用的组件持续保留。
