# gitbook-plugin-summary

auto generated summary.md，output mobi

## Case

This is the Kindle . ***two level directory:***

![screenshot](/img/screenshot-1.png)

## Usage

* **output mobi**

```	
1. $ python gitbook-mobi.py dirPath
2.The generated Mobi file is in the /docs folder
```

**generated summary.md**


```
1. $ python gitbook-plugin-summary.py dirPath
2. The generated SUMMARY-GitBook-auto-summary.md file is in the root folder 
```

## Rules

### [](https://www.npmjs.com/package/gitbook-plugin-summary#names)Names

* **README.md**: Taken from their directory name
* **File**: Taken from the first first-header (ex: `# title`) of the file
* **Directory**: Name of the directory

### [](https://www.npmjs.com/package/gitbook-plugin-summary#entry-types)Entry Types

#### [](https://www.npmjs.com/package/gitbook-plugin-summary#directory-at-the-root-of-the-gitbook)Directory at the root of the gitbook

* With a README first level in it, it will be shown as a normal link
* If it doesn't, it will be shown as a section

#### [](https://www.npmjs.com/package/gitbook-plugin-summary#nested-directories)Nested Directories

* With a README first level in it, it will be shown as a normal link
* If it doesn't, it will be shown as a label (or disabled link, if you will)

#### [](https://www.npmjs.com/package/gitbook-plugin-summary#files)Files

* Only markdown files are shown

## [](https://www.npmjs.com/package/gitbook-plugin-summary#example)Example

Let's assume that your source tree is done like this way:

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

your **SUMMARY.md** file will look like this:


``` markdown
# Summary

* [Getting Started](1-Getting Started/0-README.md)

    * [Test](1-Getting Started/1-TEST.md)

* [Reference](2-Reference/0-README.md)
```

![](/img/15236115896762.jpg)


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


