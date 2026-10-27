# 第三方声明

| 组件 | 来源与许可 |
| --- | --- |
| F2 | Johnserf-Seed/f2，Apache-2.0；固定提交 f6be8c0ffba9a127075bbeafe4838716650b6325。发布包移除上游示例 Cookie/Authorization，保留许可与修改说明。 |
| FFmpeg 7.1 | GPL-2.0-or-later 独立命令行程序；固定 x264 和 LAME 源码静态构建，完整源码压缩包与构建脚本随 Release 提供。 |
| x264 / LAME | x264 GPL-2.0-or-later；LAME LGPL-2.0-or-later。详见对应源包原始许可。 |
| 共用 Python 处理环境 | 各 Python 项目按各自许可，原始 dist-info 许可仍在包中。soxr、libsndfile 等 LGPL 依赖的对应源包单独随 Release 提供。 |
| 中文语音、VAD、标点模型 | ModelScope iic 模型卡声明 Apache-2.0；包内保留模型卡和许可。 |
| YAMNet | TensorFlow / Google，Apache-2.0。 |
| TFLite C 运行库 | TensorFlow Apache-2.0；DeNA 部分 MIT。 |
| MDX Inst HQ 3 | Ultimate Vocal Remover (UVR) 模型；依照上游 README 的 MIT 模型许可声明，署名 UVR、Anjok07 及开发者。 |

模型和第三方工具不属于视频模版工作台原创内容。各包中的原始版权声明和许可文本保留；源代码或构建材料在同一 Release 的 source 附件中提供。应用通过独立进程调用 FFmpeg，不将其改名隐藏。

FFmpeg 许可来源：https://ffmpeg.org/legal.html
UVR 模型许可声明：https://github.com/Anjok07/ultimatevocalremovergui#license
F2 来源：https://github.com/Johnserf-Seed/f2/tree/f6be8c0ffba9a127075bbeafe4838716650b6325

本目录 build/ 中的 FFmpeg 构建脚本按 GPL-2.0-or-later 提供，用于重建相应开源组件；此声明不对视频模版工作台应用整体授予 GPL 许可。
