# 在无法联网的远程服务器上手动安装 VS Code Server 开发文档

## 一、背景

在开发过程中，使用 VS Code 的远程开发功能可以方便地连接到远程服务器进行开发工作。然而，当远程服务器无法连接到互联网时，VS Code Server 的远程组件无法自动下载和安装。本文档将详细介绍如何在这种情况下手动安装 VS Code Server。

## 二、前提条件

1. 本地开发环境已安装 VS Code。
2. 远程服务器已配置好 SSH 访问权限。
3. 知道远程服务器的操作系统架构（如 Linux x64）。
4. 本地开发环境可以访问互联网。

## 三、操作步骤

### 获取 VS Code Server 的提交 ID

1. 打开 VS Code，进入“关于”页面。
2. 找到“Commit”字段对应的值，例如：
   ```
   Version: 1.101.2 (user setup)
   Commit: 2901c5ac6db8a986a5666c3af51ff804d05af0d4
   Date: 2025-06-24T20:27:15.391Z
   Electron: 35.5.1
   ElectronBuildId: 11727614
   Chromium: 134.0.6998.205
   Node.js: 22.15.1
   V8: 13.4.114.21-electron.0
   OS: Windows_NT x64 10.0.26100
   ```

### 在本地下载 VS Code Server

1. 根据远程服务器的操作系统架构（如 Linux x64），使用以下链接格式：

   ```
   https://update.code.visualstudio.com/commit:${commit_id}/server-linux-x64/stable
   ```

   将 `${commit_id}` 替换为 VS Code 的提交 ID，例如：

   ```
   https://update.code.visualstudio.com/commit:2901c5ac6db8a986a5666c3af51ff804d05af0d4/server-linux-x64/stable
   ```
2. 在浏览器中访问上述链接，下载文件（通常是一个 `.tar.gz` 压缩包，例如命名为 `vscode-server-linux-x64.tar.gz`。

### 将文件上传到远程服务器

1. 打开终端或命令行工具，使用 SCP 命令或者其它文件传输工具（WinScp，FileZilla等）将下载的文件上传到远程服务器的 `~/.vscode-server/bin` 目录下：
   ```bash
   scp vscode-server-linux-x64.tar.gz user@IpAddress:~/.vscode-server/bin/
   ```
2. 如果远程服务器的 `~/.vscode-server/bin` 目录不存在，可以先在远程服务器上创建：
   ```bash
   ssh user@IpAddress
   mkdir -p ~/.vscode-server/bin
   exit
   ```
3. 查看绝对路径是否正确：
   ```bash
   ls -ld ~/.vscode-server/bin
   ```

### 在远程服务器上解压并设置

1. 登录到远程服务器：
   ```bash
   ssh user@IpAddress
   ```

```

2. 进入 `~/.vscode-server/bin` 目录：
   ```bash
   cd ~/.vscode-server/bin
```

3. 解压下载的文件：
   ```bash
   tar xzvf vscode-server-linux-x64.tar.gz
   ```
4. 将解压后的目录重命名为对应的提交 ID：
   ```bash
   mv vscode-server-linux-x64 2901c5ac6db8a986a5666c3af51ff804d05af0d4
   ```

### 重新连接 VS Code

1. 关闭 VS Code。
2. 重新打开 VS Code，进入远程资源管理器，尝试重新连接到远程服务器。

## 四、注意事项

1. **权限问题**：如果遇到权限问题，可以尝试使用 `sudo` 或修改文件权限：
   ```bash
   sudo chown -R user:user ~/.vscode-server
   ```
2. **日志检查**：如果连接仍然失败，可以查看 VS Code 的日志文件（通常在 `~/.vscode-server/logs` 目录下）以获取更多错误信息。

## 五、参考链接

[VS Code Server的离线安装过程 - 知乎](https://zhuanlan.zhihu.com/p/294933020)
