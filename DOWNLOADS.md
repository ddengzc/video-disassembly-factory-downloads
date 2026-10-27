# 视频模版工作台 仓库与下载总览

核对日期：2026-10-27。当前应用3.0.28（预发布）、组件基线components-v2.0.0、签名预设1.0.0 / revision 1；三者独立。

- [当前应用直接下载](https://github.com/ddengzc/video-disassembly-factory-downloads/releases/download/v3.0.28/kaizheng-mac-arm64-3.0.28.zip)
- [发布说明与SHA256SUMS](https://github.com/ddengzc/video-disassembly-factory-downloads/releases/tag/v3.0.28)
- [固定组件、许可及对应源码](https://github.com/ddengzc/video-disassembly-factory-downloads/releases/tag/components-v2.0.0)
- [全部公开版本](https://github.com/ddengzc/video-disassembly-factory-downloads/releases)
- [旧版3.0.11回退入口](https://github.com/ddengzc/video-disassembly-factory-downloads/releases/tag/v3.0.11)
- [分类/音色配置原文](presets/catalog.source.json)、[客户端签名配置](presets/catalog.json)、[预设维护说明](presets/README.md)
- [私有源码仓库](https://github.com/ddengzc/video-disassembly-factory)：需授权；源码、产品架构与代码维护文档在其中。旧jingxu-components为历史重定向，不是第三套业务仓库。

普通使用者只下载应用ZIP。Source code ZIP为GitHub仓库快照，不是可安装应用。源码仓库不放安装包；下载仓库不承载完整维护源码。冻结来源以release-info.json的source_commit和source_id为准，两个仓库的同名标签不是同一提交。

升级保留共享目录、组件和凭据；先退出旧应用。原成果目录被移走时，软件无法按旧位置打开，请保留原位置。不要为了升级删除钥匙串、模型或成果。

应用未做Developer ID公证，首次运行按macOS正常允许流程。Cookie和模型密钥由使用者在本机设置，不要向GitHub或维护者公开提交。真实模型调用可能计费。

## 维护交接文档

以下文档在私有源码库中，需获授权账号访问：

- [项目完整流程图与设计说明](https://github.com/ddengzc/video-disassembly-factory/blob/main/docs/项目流程与设计说明-3.0.28.md)
- [产品逻辑与架构](https://github.com/ddengzc/video-disassembly-factory/blob/main/docs/产品逻辑与架构.md)
- [后端维护与代码结构](https://github.com/ddengzc/video-disassembly-factory/blob/main/docs/后端维护与代码结构.md)
- [完整仓库与下载地址总览](https://github.com/ddengzc/video-disassembly-factory/blob/main/docs/GitHub仓库与下载地址总览.md)

3.0.28公开包已完成摘要、解压、签名、版本/源码、隔离初始化和OCR回下载验证，详见[验证记录](releases/validation-v3.0.28.json)；完整业务、跨设备和广泛视频准确率仍分开验收。文档更新不代表重新发布应用。
