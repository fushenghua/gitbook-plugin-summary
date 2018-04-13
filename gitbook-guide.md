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


