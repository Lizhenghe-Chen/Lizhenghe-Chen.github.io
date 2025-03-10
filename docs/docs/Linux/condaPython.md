# Ubuntu 配置Conda和Pytorch

## Miniconda和Anaconda

Miniconda和Anaconda都是由Anaconda, Inc.开发的用于管理Python环境和包的工具，但它们有一些关键的区别：

[Anaconda | The Operating System for AI](https://www.anaconda.com/) 是一个包含预装科学计算和数据分析库的完整Python发行版，适合需要快速开始工作的初学者；

而[Miniconda](https://docs.anaconda.com/miniconda/)是一个轻量级的conda发行版，只包含基本的包管理器和Python解释器，适合需要自定义环境和节省空间的高级用户。

Anaconda和Miniconda的主要区别在于：

1. **预装内容**：Anaconda预装了许多常用的数据科学和机器学习库，而Miniconda则只安装了conda和Python本身，用户需要自行安装所需的库。
2. **安装大小**：由于预装的库，Anaconda的安装包比Miniconda大得多，后者提供了一个更轻量级的安装选项。
3. **灵活性**：Miniconda因其轻量级和简洁性提供了更高的灵活性，允许用户根据具体需求定制环境，而Anaconda则提供了一个即装即用的解决方案。
4. **适用场景**：Anaconda适合那些需要一个完整、预配置好的科学计算环境的用户，而Miniconda则适合那些希望从最小环境开始，根据需要构建环境的用户。
5. **用户界面**：Anaconda提供了一个图形用户界面（Anaconda Navigator），而Miniconda主要通过命令行进行操作。

简而言之，Anaconda是一个一站式的科学计算平台，而Miniconda是一个更灵活、更轻量级的conda环境管理工具。

## 安装Miniconda

[Installing Miniconda — Anaconda documentation](https://docs.anaconda.com/miniconda/install/)

## 配置Cuda和Pytorch

!!! warning
    注意Python版本不得高于3.12！，否则可能会导致无法找到对应的CUDA版本下载。
    较老版本的Python版本支持可以在[Previous PyTorch Versions | PyTorch](https://pytorch.org/get-started/previous-versions/) 中找到  

[Start Locally | PyTorch](https://pytorch.org/get-started/locally/)
