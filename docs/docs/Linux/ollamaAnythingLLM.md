# Ubuntu安装Olama和AnythigLLM

## 安装Ollama

1. [Download Ollama on Linux](https://ollama.com/download/linux)
2. 安装模型：[library](https://ollama.com/library)
3. 对外网开放：[Linux/Windows 系统 ollama 配置允许外网访问－Windows 日常故障－瓦力技术小记](https://www.walimao.com/archives/675.html)

## 安装AnythingLLM

[Linux Installation ~ AnythingLLM](https://docs.anythingllm.com/installation-desktop/linux#install-using-the-installer-script)

运行指令后可能出现 `The SUID sandbox helper binary was found, but is not configured correctly. Rather than run without sandboxing I'm aborting now.` 错误，目前可以通以下方法避免：

问题出在 `chrome-sandbox` 文件的权限和所有权配置不正确。你可以通过以下步骤来解决这个问题：

1. 打开终端，进入 `chrome-sandbox` 文件所在的目录：

    ```bash
    cd /home/david/AnythingLLMDesktop/anythingllm-desktop
    ```

2. 修改 `chrome-sandbox` 文件的所有者为 `root` 并设置正确的权限：

    ```bash
    sudo chown root chrome-sandbox
    sudo chmod 4755 chrome-sandbox
    ```

这两个命令会将 `chrome-sandbox` 文件的所有者更改为 `root` 并设置权限为 `4755`，这通常是解决此类错误的标准方法。如果你不想修改文件权限，也可以在启动程序时加上 `--no-sandbox` 参数来暂时绕过这个问题，但这不是一个长期的解决方案。
