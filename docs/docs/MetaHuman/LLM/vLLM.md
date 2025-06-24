# 本地部署vLLM

> vLLM 是一个高效、灵活且支持离线部署的开源框架，专为优化和运行大型语言模型（LLM）而设计，适用于自然语言处理、内容创作和企业级应用等多种场景。
>
> vLLM 和 Ollama 的核心区别在于：**vLLM 专注于高性能和高并发的生产级推理，适合企业级应用；而 Ollama 更注重用户友好性和本地化部署，适合个人开发者和小规模项目**。

[vLLM - vLLM 文档](https://docs.vllm.com.cn/en/latest/)，[vLLM - vLLM](https://docs.vllm.ai/en/stable/)

支持平台目前是只针对Linux平台的，可以在Windows的WSL中测试和运行，并在Linux服务器正式部署。

## 环境配置和安装

1. 首先需要确保显卡或者CPU的硬件驱动满足要求，所以第一步先把这些搞定：[Installation - vLLM](https://docs.vllm.ai/en/stable/getting_started/installation/index.html)
2. 这里推荐使用Conda或者miniConda来做虚拟环境的配置，因为在后续打包环境到其它设备上非常有用，然后就可以参考官方文档：[Quickstart - vLLM](https://docs.vllm.ai/en/stable/getting_started/quickstart.html)

vLLM会被安装在虚拟环境中，不需要额外安装软件，这就是为什么只需要打包迁移conda的环境即可。

迁移至离线或内网服务器：[使用conda pack进行环境迁移（步骤很详细）-CSDN博客](https://blog.csdn.net/ds1302__/article/details/120027173) （注意目标目录不一定要是conda的环境目录，只要在 `source` 命令后跟上环境的目录的激活文件地址即可，如我打包转移的vllmEnv 文件： `source vllmEnv/bin/activate`）

## 模型的安装使用：

1. 这里有两种，一种是直接用内置运行指令[Quickstart - vLLM](https://docs.vllm.ai/en/stable/getting_started/quickstart.html#openai-compatible-server)，模型会从[Hugging Face](https://huggingface.co/)被下载在默认缓存文件中，缺点是不能迁移模型且必须联网；
2. 所以另一种方法是从 [Hugging Face](https://huggingface.co/) 或者 [ModelScope](https://www.modelscope.cn/) 直接**克隆模型**，确保模型格式满足[Supported Models - vLLM](https://docs.vllm.ai/en/stable/models/supported_models.html) 即可，如：
   ```
   Qwen/Qwen2.5-1.5B-Instruct
   ├── config.json
   ├── generation_config.json
   ├── pytorch_model.bin
   ├── special_tokens_map.json
   ├── tokenizer_config.json
   ├── tokenizer.model
   └── vocab.json
   ```
3. 然后在运行时只需要将模型配置改为模型目录地址即可

### 服务运行和多卡配置

我们以[Qwen/Qwen3-32B · Hugging Face](https://huggingface.co/Qwen/Qwen3-32B?clone=true) 为例

1. 克隆到本地
2. 更改文件夹名字（可选），将克隆的文件重命名为需要的名字，之后在请求OpneAI的接口时会需要，大小写敏感，所以我这里直接改为了“qwen3-32b”
3. 将文件传输到服务器上（可选，如果本地运行就不用）
4. 指令运行服务([通过vllm部署qwen3大模型以及基于 vLLM 的 OpenAI 兼容 API 接口调用方法总结-CSDN博客](https://blog.csdn.net/m0_69966537/article/details/147766763))

   > ```
   > CUDA_VISIBLE_DEVICES=1,2,3 vllm serve --host 0.0.0.0 --port 11434 --max-model-len 18480 --tensor-parallel-size 2 ./qwen3-32b 
   > ```
   >
   > 这段命令的作用是启动 vLLM 服务，使用指定的 GPU 资源，并配置了模型的最大序列长度和张量并行大小。具体解析如下：
   >
   > 1. **`CUDA_VISIBLE_DEVICES=1,2,3`**：这行命令设置了环境变量 `CUDA_VISIBLE_DEVICES`，指定运行 vLLM 服务时只使用编号为 1、2 和 3 的 GPU。这确保了只有这些 GPU 被用于模型推理，而其他 GPU 不会被使用。（不是必须）
   > 2. **`vllm serve`**：这是 vLLM 提供的命令，用于启动推理服务。
   > 3. **`--host 0.0.0.0`**：指定服务监听的主机地址为 `0.0.0.0`，表示服务将监听所有可用的网络接口，允许从外部访问。
   > 4. **`--port 11434`**：指定服务监听的端口号为 11434，客户端可以通过这个端口与服务进行通信。（默认是8000端口）
   > 5. **`--max-model-len 18480`**：设置模型的最大序列长度为 18480。这限制了模型处理的最大输入长度，以暂时避免 `KV cache memory`内存不足等问题。
   > 6. **`--tensor-parallel-size 2`**：启用张量并行，并设置张量并行的大小为 2（一定要为偶数）。这意味着模型的张量将被分割成 2 份，分别在指定的 GPU 上进行计算，以提高推理效率。
   > 7. **`./qwen3-32b`**：指定模型的路径为当前目录下的 `qwen3-32b` 文件夹。这是模型的存储位置，vLLM 服务将从这里加载模型。
   >
   > 总结来说，这段命令启动了一个使用 GPU 1、2 和 3 的 vLLM 服务，监听所有网络接口的 11434 端口，模型的最大序列长度设置为 18480，并且启用了张量并行，大小为 2，模型路径为当前目录下的 `qwen3-32b` 文件夹。
   >
5. 用浏览器访问http://ipAddress:11434/ 如果加载出来 `{"detail":"Not Found"}` 就证明服务器能够访问了，这个时候就可以使用OpenAI的API接口了。

!!! note
    qwen3 是推理模型，要想关闭thinking功能，OpenAI的API接口是不支持的，想要禁用请参考官方文档：[Qwen/Qwen3-32B · Hugging Face](https://huggingface.co/Qwen/Qwen3-32B#switching-between-thinking-and-non-thinking-mode)

```python
   from openai import OpenAI

   client = OpenAI(
       base_url = 'http://10.120.47.138:11434/v1',
       api_key='', # required, but unused
   )

   response = client.chat.completions.create(
     model="./qwen3-32b",
     messages=[
       {"role": "system", "content": "You are a helpful assistant."},
       {"role": "user", "content": "Who won the world series in 2020?"},
       {"role": "assistant", "content": "The LA Dodgers won in 2020."},
       {"role": "user", "content": "Where was it played?"}
     ]
   )
   print(response.choices[0].message.content)
```
