# Run In Background for Linux

要实现系统启动后自动挂载外置机械硬盘，并运行指定的 `sherpa-onnx-online-websocket-server` 命令，可以通过以下步骤实现：

### 1. **自动挂载硬盘（如有）**

首先，确保硬盘在系统启动时自动挂载。可以通过 `/etc/fstab` 文件或 systemd 的 `.mount` 文件来实现。

#### 方法一：使用 `/etc/fstab` 自动挂载

1. **编辑 `/etc/fstab` 文件**
   打开 `/etc/fstab` 文件：

   ```bash
   sudo nano /etc/fstab
   ```

   在文件末尾添加以下内容：

   ```
   UUID=d8afb4b8-396d-45db-be45-9d299e998695 /mnt/sda1 ext4 defaults 0 2
   ```

   - `UUID` 是硬盘的唯一标识符。
   - `/mnt/sda1` 是挂载点。
   - `ext4` 是文件系统类型（根据实际情况调整）。
   - `defaults` 是默认挂载选项。
   - `0` 表示不备份。
   - `2` 表示在启动时检查文件系统。
2. **测试挂载**
   执行以下命令，测试挂载是否成功：

   ```bash
   sudo mount -a
   ```

   如果没有报错，说明挂载成功。

#### 方法二：使用 systemd 的 `.mount` 文件

1. **创建 `.mount` 文件**
   创建一个文件 `/etc/systemd/system/mnt-sda1.mount`，内容如下：

   ```ini
   [Unit]
   Description=Mount external hard drive
   Before=local-fs.target

   [Mount]
   What=/dev/disk/by-uuid/d8afb4b8-396d-45db-be45-9d299e998695
   Where=/mnt/sda1
   Type=ext4
   Options=defaults

   [Install]
   WantedBy=local-fs.target
   ```
2. **启用并启动挂载单元**

   ```bash
   sudo systemctl enable mnt-sda1.mount
   sudo systemctl start mnt-sda1.mount
   ```

### 2. **创建 systemd 服务文件**

接下来，创建一个 systemd 服务文件，确保硬盘挂载后运行 `sherpa-onnx-online-websocket-server` 命令。

1. **创建服务文件**
   创建一个文件 `/etc/systemd/system/sherpa-onnx.service`，内容如下：

   ```ini
   [Unit]
   Description=Sherpa ONNX Online WebSocket Server
   After=network.target mnt-sda1.mount
   Requires=mnt-sda1.mount

   [Service]
   Type=simple
   WorkingDirectory=/mnt/sda1/GitProjects/sherpa-onnx
   ExecStart=/mnt/sda1/GitProjects/sherpa-onnx/build/bin/sherpa-onnx-online-websocket-server \
     --port=6006 \
     --num-work-threads=3 \
     --num-io-threads=2 \
     --tokens=./sherpa-onnx-streaming-zipformer-bilingual-zh-en-2023-02-20/tokens.txt \
     --encoder=./sherpa-onnx-streaming-zipformer-bilingual-zh-en-2023-02-20/encoder-epoch-99-avg-1.onnx \
     --decoder=./sherpa-onnx-streaming-zipformer-bilingual-zh-en-2023-02-20/decoder-epoch-99-avg-1.onnx \
     --joiner=./sherpa-onnx-streaming-zipformer-bilingual-zh-en-2023-02-20/joiner-epoch-99-avg-1.onnx \
     --log-file=./log.txt \
     --max-batch-size=5 \
     --loop-interval-ms=20
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```
2. **重新加载 systemd 配置**

   ```bash
   sudo systemctl daemon-reload
   ```
3. **启用并启动服务**

   ```bash
   sudo systemctl enable sherpa-onnx.service
   sudo systemctl start sherpa-onnx.service
   ```

### 3. **检查服务状态**

运行以下命令，检查服务是否正常运行：

```bash
sudo systemctl status sherpa-onnx.service
```

如果服务正常运行，你会看到类似以下的输出：

```
● sherpa-onnx.service - Sherpa ONNX Online WebSocket Server
     Loaded: loaded (/etc/systemd/system/sherpa-onnx.service; enabled; vendor preset: enabled)
     Active: active (running) since ...
```

### 4. **查看日志**

如果服务启动失败，可以通过以下命令查看日志：

```bash
sudo journalctl -u sherpa-onnx.service
```

### 总结

通过上述步骤，你可以确保系统启动后：

1. 外置机械硬盘自动挂载到 `/mnt/sda1`。
2. `sherpa-onnx-online-websocket-server` 在硬盘挂载后自动启动，并在后台运行。
