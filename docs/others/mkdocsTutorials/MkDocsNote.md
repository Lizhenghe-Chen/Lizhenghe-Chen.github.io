# MkDocs 部署到Github

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

# 原生内置图标

如果要在文章list链接里显示图标，可以在开头增加：

```
---
icon: material/microphone-message
---
```

---

[详情请参考：Icons, Emojis - Material for MkDocs](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/?h=icon#search) 或在“maertial/“替换其它图标名：[Material Design Icons - Icon Library - Pictogrammers](https://pictogrammers.com/library/mdi/)
