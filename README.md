# gitbook-plugin-summary

[怎样在Kindle电子书中显示出有层次感的二级目录？](https://www.zhihu.com/question/27390534)


用calibre做成的二级目录以及gitbook 导出mobi文件，在kindle电子书上，一律会变成一级目录，当文件非常多的时候阅读就不方便了。`gitbook-plugin-summary `就是来解决这个问题的。

前提环境是要安装gitbook ，安装方法[GitBook 制作 Kindle 电子书详细教程](gitbook-guide.md)

## Case

这就是转换的Kindle效果图，**注意是二级目录**：

![screenshot](/img/screenshot-1.png)

## Usage

* **生成mobi**

```	
1. $ python gitbook-mobi.py dirPath
2. 生成的mobi文件在docs文件夹中
```

**如果只需要自动生成summary.md目录文件**


```
1. 运行$ python gitbook-plugin-summary.py dirPath
2. 脚本将自动在同一个目录生成 SUMMARY-GitBook-auto-summary.md
```

## Rules

### Names

* **README.md**: 这个是你的gitbook的介绍，
* **File**: 每一个*.md 文件是一个二级Title
* **Directory**: 每一个目录是一级Title，链接到自动创建**`0-README.md`**

### Files

* 只支持Markdown文件显示

## Example

假设目录是这样子：

```
$ tree .
```
```.
├── 1-Getting Started
│   ├── 0-README.md
│   └── 1-TEST.md
├── 2-Reference
│   └── 0-README.md
├── README.md
└── SUMMARY.md
```

 生成后的**SUMMARY.md** 文件是这样的:

```
- [Getting Started](1-Getting Started/0-README.md)
	 - [Test](1-Getting Started/1-TEST.md)
- [Reference](2-Reference/0-README.md)
```

**tips:** 其中自动创建`0-README.md`是链接到一级文件目录的


Gitbook 效果图:

![](/img/15236115708950.jpg)

## License

```
MIT License

Copyright (c) 2018 fushenghua

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

