# CosyVoce 文字转语音

## 什么是CosyVoice

CosyVoice 是阿里巴巴通义实验室开发的开源多语言语音合成模型，支持多种语言和方言，具备零样本语音克隆、实时流式合成、高自然度语音生成等功能，能够根据文本的情感和风格需求生成相应语音，适用于语音助手、智能客服等场景，具有广泛的应用前景。

**多语言支持**：涵盖中文、英文、日文、韩文、粤语等多种语言和方言。

* **零样本语音克隆**：仅需3~10秒原始音频即可快速生成特定音色的语音。
* **实时流式合成**：低延迟（150毫秒）的实时语音合成，适合即时反馈场景。
* **高自然度语音生成**：基于深度学习和预训练模型，生成语音接近真人水平。
* **情感与风格控制**：根据文本内容生成带有相应情感色彩和风格的语音。
* **开源与灵活性**：采用Apache-2.0开源许可，可自由用于商业和非商业用途，并支持定制。
* 官网：[CosyVoice2.0](https://funaudiollm.github.io/cosyvoice2/)
* Github：[FunAudioLLM/CosyVoice: Multi-lingual large voice generation model, providing inference, training and deployment full-stack ability.](https://github.com/FunAudioLLM/CosyVoice)
* 在线（modelscope）：[CosyVoice语音生成大模型2.0-0.5B · 模型库](https://www.modelscope.cn/models/iic/CosyVoice2-0.5B)
* 在线（HuggingFace）：[CosyVoice2-0.5B - a Hugging Face Space by FunAudioLLM](https://huggingface.co/spaces/FunAudioLLM/CosyVoice2-0.5B)

## 文字转语音的简单部署

由于官方的网站只提供了简单的demo场景，而且经常报错，所以想要直接使用，还是需要自己本地部署并写一个简单的服务器的，以Python为例

1. 安装部署严格按照官方文档进行：[GitHub - FunAudioLLM/CosyVoice: Multi-lingual large voice generation model, providing inference, training and deployment full-stack ability.](https://github.com/FunAudioLLM/CosyVoice)
2. 参考官方文档的脚本，已经非常简单直接的，我们只需要稍作修改就可以将其变为简单的服务器，首先根据prompt音频用几秒钟进行克隆训练，之后就可以快速响应客户端请求，且可以支持不同方言的选择：
   ```python
   from flask import Flask, request, send_file, abort
   import io
   import torchaudio
   from cosyvoice.cli.cosyvoice import CosyVoice2
   from cosyvoice.utils.file_utils import load_wav
   import sys
   sys.path.append('third_party/Matcha-TTS')
   app = Flask(__name__)

   cosyvoice = CosyVoice2('pretrained_models/CosyVoice2-0.5B', load_jit=False, load_trt=False, load_vllm=False, fp16=False)
   prompt_speech_16k = load_wav('./asset/zero_shot_prompt.wav', 16000)

   prompt = load_wav('./asset/zero_shot_prompt.wav', 16000)

   # 粤语ID示例，根据Unity语音ID进行处理
   voice_style_map = {
       0: '用普通话说这句话',
       1: '用粤语话说这句话',
       2: '用四川话说这句话',
       3: '用上海话说这句话',

       # 你可以在此添加更多 voiceID 和语音风格
   }

   @app.route('/tts')
   def tts():
       text = request.args.get("content", "").strip()
       voice_id = int(request.args.get("id", 0))

       if not text:
           return abort(400, description="Missing 'content' parameter")

       voice_instruction = voice_style_map.get(voice_id, voice_style_map[0])

       try:
           # 生成语音
           for chunk in cosyvoice.inference_instruct2(text, voice_instruction, prompt, stream=False):
               wav_tensor = chunk['tts_speech']
               sample_rate = cosyvoice.sample_rate
               break  # 只取第一个输出段
       except Exception as e:
           return abort(500, description=f"TTS generation failed: {e}")

       # 保存为 MP3 格式返回
       mp3_buffer = io.BytesIO()
       torchaudio.save(mp3_buffer, wav_tensor, sample_rate, format="mp3")
       mp3_buffer.seek(0)
       return send_file(mp3_buffer, mimetype="audio/mpeg", download_name="tts.mp3")

   if __name__ == "__main__":
       app.run(host="0.0.0.0", port=19464, threaded=True)
   ```
3. 客户端也很简单，其他平台和编程语言都可以参考WebRequest形式获取到生成的语音，生成的语音将会保存为 `output.mp3`：
   ```python
   import requests

   def test_tts_server(text, voice_id, server_url="http://10.12.17.136:19463/tts    "):
       """
       测试 TTS 服务器的函数

       :param text: 要合成语音的文本内容
       :param voice_id: 语音风格的 ID
       :param server_url: TTS 服务器的 URL，默认为本地运行的服务器
       :return: None
       """
       # 构造请求参数
       params = {
           "content": text,
           "id": voice_id
       }

       try:
           # 发送 GET 请求到 TTS 服务器
           response = requests.get(server_url, params=params, stream=True)

           # 检查响应状态码
           if response.status_code == 200:
               # 保存返回的 MP3 文件
               with open("output.mp3", "wb") as f:
                   for chunk in response.iter_content(chunk_size=1024):
                       if chunk:
                           f.write(chunk)
               print("MP3 文件已成功保存为 output.mp3")
           else:
               print(f"请求失败，状态码：{response.status_code}")
               print(f"服务器返回的错误信息：{response.text}")
       except Exception as e:
           print(f"请求过程中发生错误：{e}")

   # 示例调用
   if __name__ == "__main__":
       text_to_speak = "你好，世界,我爱你！"
       voice_id_to_use = 0  # 示例语音 ID，根据需要修改
       test_tts_server(text_to_speak, voice_id_to_use)
   ```

## 复用克隆语音

可以使用案例素材作为测试：[CosyVoice2.0](https://funaudiollm.github.io/cosyvoice2/#Zero-shot%20In-context%20Generation)

一旦克隆后并保存一次，如保存为“my_zero_shot_spk”之后就可以直接复用克隆的音色了：

```python
import sys
sys.path.append('third_party/Matcha-TTS')
from cosyvoice.cli.cosyvoice import CosyVoice, CosyVoice2
from cosyvoice.utils.file_utils import load_wav
import torchaudio

cosyvoice = CosyVoice2('pretrained_models/CosyVoice2-0.5B', load_jit=False, load_trt=False, load_vllm=False, fp16=False)
prompt_speech_16k = load_wav('./asset/ZH_6_prompt.wav', 16000)

# 1.save zero_shot spk for future usage
assert cosyvoice.add_zero_shot_spk('周日被我射熄火了，所以今天是周一', prompt_speech_16k, 'my_zero_shot_spk') is True
for i, j in enumerate(cosyvoice.inference_zero_shot('收1232', '', '', zero_shot_spk_id='my_zero_shot_spk', stream=False)):
    torchaudio.save('zero_shot_{}.wav'.format(i), j['tts_speech'], cosyvoice.sample_rate)
cosyvoice.save_spkinfo()

# 2. load and reuse zero_shot spk from spkinfo
for i, j in enumerate(cosyvoice.inference_zero_shot('收到好友从远方寄来的生日礼物，那份意外的惊喜与深深的祝福让我心中充满了甜蜜的快乐，笑容如花儿般绽放hahahah。', '', '', zero_shot_spk_id='my_zero_shot_spk', stream=False)):
    torchaudio.save('zero_shot_{}.wav'.format(i), j['tts_speech'], cosyvoice.sample_rate)
```
