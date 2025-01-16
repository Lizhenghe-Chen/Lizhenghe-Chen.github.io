## Run In Background for Linux

要在Linux系统上开机自动运行并后台运行上述命令，可以创建一个systemd服务。以下是步骤：

1. 创建一个新的systemd服务文件，例如 `sherpa-onnx.service`：

```bash
sudo nano /etc/systemd/system/sherpa-onnx.service
```

2. 在文件中添加以下内容：

```ini
[Unit]
Description=Sherpa ONNX Online WebSocket Server
After=network.target

[Service]
ExecStart=/path/to/build/bin/Release/sherpa-onnx-online-websocket-server \
  --port=6006 \
  --num-work-threads=3 \
  --num-io-threads=2 \
  --tokens=/path/to/sherpa-onnx-streaming-zipformer-bilingual-zh-en-2023-02-20/tokens.txt \
  --encoder=/path/to/sherpa-onnx-streaming-zipformer-bilingual-zh-en-2023-02-20/encoder-epoch-99-avg-1.onnx \
  --decoder=/path/to/sherpa-onnx-streaming-zipformer-bilingual-zh-en-2023-02-20/decoder-epoch-99-avg-1.onnx \
  --joiner=/path/to/sherpa-onnx-streaming-zipformer-bilingual-zh-en-2023-02-20/joiner-epoch-99-avg-1.onnx \
  --log-file=/path/to/log.txt \
  --max-batch-size=5 \
  --loop-interval-ms=20
WorkingDirectory=/path/to/working/directory
Restart=always
User=your-username
Group=your-groupname

[Install]
WantedBy=multi-user.target
```

请将 `/path/to/`替换为实际路径，并将 `your-username`和 `your-groupname`替换为实际的用户名和用户组名。

3. 保存并关闭文件。
4. 重新加载systemd配置：

```bash
sudo systemctl daemon-reload
```

5. 启动并启用服务：

```bash
sudo systemctl start sherpa-onnx.service
sudo systemctl enable sherpa-onnx.service
```

这样，服务将在后台运行，并且在系统启动时自动启动。
