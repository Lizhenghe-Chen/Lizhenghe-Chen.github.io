## MkDocs 部署到Github

> 参考：
>
> * [Publishing your site - Material for MkDocs](https://squidfunk.github.io/mkdocs-material/publishing-your-site/#with-github-actions-insiders)
> * [Mkdocs+Material+GithubPage+Github Action自动化搭建你自己的博客！_mkdocs material-CSDN博客](https://blog.csdn.net/leoalasiga/article/details/132711171)

核心是 **gh-deploy** 文件必须在GitHub page 的指向根（/root）目录

简单来说，直接使用 `mkdocs gh-deploy` 命令将站点部署到 GitHub 上，并不能直接通过 `https://<用户名>.github.io` 访问你的页面。原因如下：

1. **GitHub Pages 的默认规则** ：

   GitHub Pages 通常从仓库的 `master` 或 `main` 分支（或特定分支的 `/docs` 文件夹）构建网站内容。
2. **`mkdocs gh-deploy` 的行为** ：

   当你使用 `mkdocs gh-deploy` 命令时，MkDocs 会自动把生成的静态文件上传到线上仓库的 `gh-pages` 分支，而不是 `master` 或 `main` 分支。

   但是 GitHub Pages 默认不会从 `gh-pages` 分支构建，除非你手动指定。

因此，如果你想通过 `https://<用户名>.github.io` 直接访问部署的页面，你还需要额外步骤：

* **手动同步本地仓库到 GitHub 的默认分支** （比如 `master` 或 `main`）。
* 或者在 GitHub 仓库的设置中，指定 `gh-pages` 分支作为 GitHub Pages 的发布分支，在本地命令窗口使用 `<mkdocsgh-deploy`命令自动构建并上传 `gh-deploy` 分支。

![1733589240626](image/MkDocsNote/1733589240626.png)

## 重写覆盖页面：

[Customization - Material for MkDocs](https://squidfunk.github.io/mkdocs-material/customization/#overriding-blocks)

## 原生内置图标

如果要在文章list链接里显示图标，可以在开头增加：

```
---
icon: material/microphone-message
---
```

---

[详情请参考：Icons, Emojis - Material for MkDocs](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/?h=icon#search) 或在“maertial/“替换其它图标名：[Material Design Icons - Icon Library - Pictogrammers](https://pictogrammers.com/library/mdi/)

路径通常可以改为：`octicons/logo-github-16`的形式，**第一个分隔符前为icon的提供平台**

![1733756762076](image/MkDocsNote/1733756762076.png)

## **常用 Admonitions 类型**

mkdocs.yml中加入：

> markdown_extensions:
>
> - admonition #提供!!!标记支持
> - pymdownx.details #提供???展开功能支持

!!! note
!!! abstract
!!! info
!!! tip
!!! success
!!! question
!!! warning
!!! failure
!!! danger
!!! bug
!!! example
!!! quote

??? 点击展开
    展开的内容  
    ```
    ??? 点击展开
        展开的内容
    ```

以下是 Material for MkDocs 主题中默认支持的标记类型及用途：

|      标记类型      | 语法             | 用途说明                                           |
| :----------------: | :--------------- | :------------------------------------------------- |
|   **note**   | `!!! note`     | 一般的提示，用于强调重要信息或注释                 |
| **abstract** | `!!! abstract` | 概括内容的摘要块                                   |
|   **info**   | `!!! info`     | 信息提示块，提供额外的上下文或背景                 |
|   **tip**   | `!!! tip`      | 提供技巧、建议或最佳实践                           |
| **success** | `!!! success`  | 表示成功或正面的结果                               |
| **question** | `!!! question` | 提出问题或需要进一步思考的内容                     |
| **warning** | `!!! warning`  | 用于警告用户注意潜在问题或需要小心的操作           |
| **failure** | `!!! failure`  | 表示失败或错误                                     |
|  **danger**  | `!!! danger`   | 严重警告，表示需要特别注意或可能导致严重后果的操作 |
|   **bug**   | `!!! bug`      | 标记问题或已知的错误                               |
| **example** | `!!! example`  | 提供具体的示例说明                                 |
|  **quote**  | `!!! quote`    | 引用块，通常用于显示引用或文摘                     |
|       expand       | `??? expand`   | 提供展开功能                                       |
