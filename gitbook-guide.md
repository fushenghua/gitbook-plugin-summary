# gitbook 环境安装

## 一、安装 Node.js

由于 GitBook 是基于 Node.js 开发的，所以依赖 Node.js 环境。如果您的系统中还未安装 Node.js，请点击下面的链接，根据你所使用的系统下载对应的版本。如果已安装则略过本步骤。

Node.js 下载页面：https://nodejs.org/en/download/stable/

Windows 版和 Mac 版的 Node.js 都是常规的安装包，连续下一步安装即可。Lunix 版可以参照官方文档通过 yum、apt-get 之类的工具安装，也可以通过源码包安装，如下所示：

```
$ wget https://nodejs.org/dist/v5.4.1/node-v5.4.1.tar.gz
$ tar zxvf node-v5.4.1.tar.gz
$ cd node-v5.4.1
$ ./configure
$ make
$ make install
```
## 二、安装 GitBook

打开“命令提示符”（Mac 系统打开“终端”）输入以下命令安装 GitBook：


```
$ npm install gitbook-cli -g
```
由于网络的原因，安装的时间可能会较长一些，请耐心等待直到安装完成。安装完成后可以输入以下命令，以查看 GitBook 版本的方式检查是否安装成功：


```
$ gitbook -V
```
## 三、创建电子书项目

新建一个目录，并进入该目录使用 gitbook 命令初始化电子书项目。举个例子，现在要创建一个名为“MyFirstBook”的空白电子书项目，如下所示：

```
$ mkdir MyFirstBook
$ cd MyFirstBook
$ gitbook init
```

## 四、编辑电子书内容

初始化后的目录中会出现“README.md（电子书简介文件）”和“SUMMARY.md（导航目录文件）”两个基本文件。除此之外还可以手动新建其它“Glossary.md（书尾的词汇表）”、“book.json（电子书配置文件）”。电子书的正文内容可以根据自己的喜好创建新的后缀为 .md 文件，如“chapter01.md”，然后用 MarkDown 编写具体的文本内容即可。下面对这些文件分别做详细介绍。

### 1、README.md

此文件是简单的电子书介绍，可以把您所制作的电子书做一下简单的描述：

```
# 简介

这是我的第一本使用 GitBook 制作的电子书。
```

### 2、SUMMARY.md

此为电子书的导航目录文件，每当新增一个章节文件就需要向此文件中添加一条记录。对于 Kindle 电子书来说，此文件所呈现的目录结构就是开头的目录内容和“前往”的目录导航。

```
# Summary

* [简介](README.md)
* [第一章](section1/README.md)
* [第二章](section2/README.md)
```

如果需要“子章节”可以使用 `Tab` 缩进来实现（最多支持三级标题），如下所示：

```
# Summary

* [第一章](section1/README.md)
    * [第一节](section1/example1.md)
    * [第二节](section1/example2.md)
* [第二章](section2/README.md)
    * [第一节](section2/example1.md)
```

### 3、Glossary.md

对于电子书内容中需要解释的词汇可在此文件中定义。词汇表会被放在电子书末尾。其格式如下所示：

```
# 电子书
电子书是指将文字、图片、声音、影像等讯息内容数字化的出版物和植入或下载数字化文字、图片、声音、影像等讯息内容的集存储和显示终端于一体的手持阅读器。

# Kindle
Amazon Kindle 是由 Amazon 设计和销售的电子书阅读器（以及软件平台）。用户可以通过无线网络使用 Amazon Kindle 购买、下载和阅读电子书、报纸、杂志、博客及其他电子媒体。
```

### 4、book.json

“book.json”是电子书的配置文件，可以看作是电子书的“原数据”，比如 title、description、isbn、language、direction、styles 等，更多[点击这里](http://help.gitbook.com/format/configuration.html)查看。它的基本结构如下所示：

```
{
    "title": "我的第一本電子書",
    "description": "用 GitBook 制作的第一本電子書！",
    "isbn": "978-3-16-148410-0",
    "language": "zh-tw",
    "direction": "ltr"
}
```

### 5、普通章节.md 文件

普通章节.md 文件可以使用您感觉顺手的文本编辑器编写。MarkDown 的写法可以[点击这里](http://help.gitbook.com/format/markdown.html)查看相关示例。每编写一个 .md 文件，不要忘了在“SUMMARY.md”文件中添加一条记录哦。

### 6、电子书封面图片

[GitBook 帮助文档](http://help.gitbook.com/format/cover.html)建议封面图片的尺寸为 1800*2360 像素并且遵循建议：

* 没有边框
* 清晰可见的书本标题
* 任何重要的文字在小版本中应该可见

图片的格式为 jpg 格式。把图片重命名为“cover.jpg”放到电子书项目文件夹即可。

## 五、预览电子书内容

电子书内容编写完毕后可以使用浏览器预览一下。先输入下面的命令据 .md 文件生成 HTML 文档：

```
$ gitbook build
```

生成完毕后，会在电子书项目目录中出现一个名为“_book”的文件夹。进入该文件夹，直接用浏览器打开“index.html”，或先输入下面的命令：

```
$ gitbook serve
```

然后在浏览器中输入“[http://localhost:4000](http://localhost:4000/)”即可预览电子书内容，预览完毕后按 `Ctrl + C` 结束。

## 六、生成电子书文件

确定电子书没有问题后，可以通过输入以下命令生成 mobi 电子书：

```
$ gitbook mobi ./ ./MyFirstBook.mobi
```

如果出现以下错误提示，说明您还未安装 Calibre。由于 GitBook 生成 mobi 格式电子书依赖 Calibre 的 ebook-convert，所以请先[点击这里](https://bookfere.com/tools#calibre)下载安装 Calibre。

```
Error: Need to install ebook-convert from Calibre
```

Calibre 安装完毕后，对于 Mac OS X 系统，还需要先设置一下软链接：

```
$ ln -s /Applications/calibre.app/Contents/MacOS/ebook-convert /usr/local/bin
```

再次运行转换命令，即可生成 mobi 格式电子书。

## 七、把项目托管到 GitBook.com

以上所有的步骤都是在本地进行的，如果需要实现电子书的版本管理，或者把电子书发布到网络上，还可以通过 Git 命令将本地的项目托管到 GitBook.com 上。

### 1、注册 GitBook.com 账号

首先进入 [GitBook.com](https://www.gitbook.com/) 注册一个账号，并新建一个项目。在“**Setting**（设置）”页面获取到“**Git URL**（Git 链接）”，链接的样子如下所示：

```
https://git.gitbook.com/kindlefere/myfirstbook.git
```

### 2、安装 Git 软件

在开始下面的步骤之前请先确保您的系统中已经安装了 Git。一般 Mac 和 Linux 自带 Git 功能，可以在终端运行 `git --version` 查看 Git 版本。Windows 一般不会自带 Git 功能，请[点击这里](https://git-scm.com/downloads)下载先安装。

在安装 Windows 版的 Git 时，会看到“**Use Git from Git Bash only**”和“**Use Git from the Windows Command prompt**”两个选项。前者指的在程序自带的独立终端中使用 Git。后者是指可以通过系统自带的“命令提示符”使用 Git 命令。可以根据自己的喜好选择，个人推荐使用后者。

### 3、上传已有的电子书项目

在本地新建一个文件夹，并通过 Git 命令把刚才新建的远程项目抓取到本地，如下所示：

```
$ mkdir MyFirstBook-Git
$ cd MyFirstBook-Git
$ git init
$ git pull https://git.gitbook.com/kindlefere/myfirstbook.git

```

然后把本地项目“MyFirstBook”中的所有内容拷贝到刚才新建的文件夹中，如上面的“MyFirstBook-Git”。然后使用 Git 命令把本地的项目上传到远程，如下所示：

```
$ git add -A
$ git commit -m "提交说明"
$ git remote add gitbook https://git.gitbook.com/kindlefere/myfirstbook.git
$ git push -u gitbook master

```

期间需要输入你的 GitBook 注册邮箱和密码。今后修改内容后只需要输入以下 Git 命令即可：

```
$ git add [修改的文件]
$ git commit -m "提交说明"
$ git push -u gitbook master

```

## 八、把项目关联到 GitHub 帐户

如果你喜欢使用 GitHub 管理项目。还可以把您的 GitBook 帐户和 GitHub 帐户关联起来，这样两者的修改内容就可以互相同步了。

### 1、关联 GitBook 和 GitHub 帐户

关联设置也很简单，首先进入 GitBook 的“**Account Settings**（帐户设置）”页面，在“**Profile**（个人资料）”标签页找到“**GitHub**”选项卡，点击【Connect to GitHub】按钮会转向 GitHub 的“**Authorize application**”页面，点击【Authorize application】按钮即可完成关联。

### 2、把 GitBook 项目导入到 GitHub

完成关联后即可设置同步电子书项目了。以电子书项目“MyFirstBook”为例，首先需要把项目导入到 GitHub 中一份。进入某个电子书项目的设置页面，切换到“GitHub”选项卡。在“GitHub Repository”中，点击【Export to GitHub】按钮，按照向导所示步骤将项目导入 GitHub 中。

### 3、设置 GitBook 和 GitHuB 同步

导出成功后，再回到 GitBook 项目设置页面的“GitHub”选项卡，在“GitHub Repository”中的输入框中填入 GitHub 的 Repository 名，如“GitHub用户名/myfirstbook”，点击【Save】按钮保存。

保存后当前页面会出现一个名为“Integration”的选项卡，点击里面的【Add webhook】按钮，允许 GitBook 接收 Github 的内容更新。这样就把 GitBook 上的项目和 GitHub 相对应的项目关联上了。

此后即可用 GitHub 管理电子书项目，在 GitBook 上对电子书内容修改也会自动同步到 GitHub 中。


