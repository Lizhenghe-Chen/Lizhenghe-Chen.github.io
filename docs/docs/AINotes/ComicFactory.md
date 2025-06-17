
## 介绍

> 开源项目

**AI Comic Factory** 是一个由 Hugging Face 提供支持的开源项目，旨在通过结合大型语言模型（LLM）和 Stable Diffusion XL（SDXL）技术，帮助用户轻松生成漫画面板。以下是其主要功能和特点：

1. **一键生成漫画面板**
   用户只需输入一个简单的提示（prompt），AI Comic Factory 就能利用 LLM 和 SDXL 技术生成高质量的漫画面板。这种自动化生成方式大大降低了创作门槛，即使是没有任何绘画技能的用户，也能快速创作出属于自己的漫画。
2. **灵活的语言模型选择**
   AI Comic Factory 支持多种语言模型（LLM），包括 Hugging Face Inference API 提供的模型（如 Zephyr-7B-Beta）、OpenAI 的 GPT-4 Turbo、Groq 的 Mixtral-8x7B、Anthropic 的 Claude 等。用户可以根据自己的需求和偏好选择合适的 LLM 引擎。
3. **强大的渲染引擎支持**
   项目提供了多种渲染引擎选项，包括 Hugging Face Inference API、Replicate、VideoChain 等。用户可以根据自己的硬件条件和性能需求选择合适的渲染工具，以生成高质量的漫画图像。
4. **高度可定制化**
   AI Comic Factory 提供了丰富的配置选项，用户可以通过修改 `.env` 文件中的变量来调整项目的运行方式。例如，用户可以指定使用本地模型、云托管模型或私有模型，甚至可以自定义模型版本和参数。
5. **开源且易于扩展**
   该项目完全开源，用户可以自由查看和修改代码。如果默认的 LLM 或渲染引擎无法满足需求，用户可以自行扩展或替换为其他模型或技术，例如使用 DALL·E 或其他 Stable Diffusion 变体。
6. **社区支持与分享**
   虽然社区分享功能主要面向 Hugging Face 官方应用，但用户仍然可以通过开源社区获取支持和灵感。此外，项目开发者也计划在未来推出更友好的文档和更简化的部署方式。

![1742093474881](image/ComicFactory/1742093474881.png)

## 链接

* Github：[jbilcke-hf/ai-comic-factory: Generate comic panels using a LLM + SDXL. Powered by Hugging Face 🤗](https://github.com/jbilcke-hf/ai-comic-factory)
* 在线（官方网站应用）：[AI Comic Factory: generate your own comics! Powered by Hugging Face 🤗](https://aicomicfactory.app/)
* 在线（Hugging Face）：[AI Comic Factory - a Hugging Face Space by jbilcke-hf](https://huggingface.co/spaces/jbilcke-hf/ai-comic-factory)
