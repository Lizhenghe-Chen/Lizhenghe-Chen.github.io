# Sherpa Onnx ASR 多平台语音转文字STT实战

## 前言

本项目期望使用自己的语音识别模块（STT）项目和Sherpa大模型框架实现通讯，从而进一步提高项目的解耦能力以及响应速度。由于原项目的[开发文档](https://k2-fsa.github.io/sherpa/onnx/tutorials/index.html "开发文档")比较进阶，所以这里用更直白简洁且清晰的方式对某几个Demo和功能实现做进一步的阐述。

## 流程阐述

整个流程主要分为6步，按照下图的顺序，一步一步实现项目的对接。

项目仓库：[https://github.com/k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx "https://github.com/k2-fsa/sherpa-onnx")

1. ## 拉取项目
2. ## 运行构建（Build）
3. ## 下载模型和导入
4. ## 运行测试程序
5. ## 启动API程序
6. ## 客户端程序对接
