# M-system

Install process for Ubuntu 16.04 LTS

##安装系统运行依赖，完成语音唤醒

参考https://developer.baidu.com/forum/topic/show/244631?pageNo=1 和 https://developer.baidu.com/forum/topic/show/244881


    sudo apt-get update
    
    sudo apt-get install python-dateutil

    sudo apt-get install gir1.2-gstreamer-1.0

    sudo apt-get install python-pyaudio

    sudo apt-get install libatlas-base-dev

    sudo apt-get install python-dev

##新系统在此可以先安装pip（以下是针对Ubuntu16自带的python2.7.12安装pip）

    sudo apt-get install python-setuptools python-dev build-essential
    
    sudo  easy_install pip

    sudo pip install baidu-aip

    sudo pip install tornado

    sudo pip install hyper


如果有安装不上的建议到https://pypi.python.org/pypi找相应的二进制包安装，或者更换国内的源。

##安装python机器学习依赖

1.安装numpy：

    sudo pip install numpy

2.安装scipy：

    sudo apt-get install libblas-dev liblapack-dev libatlas-base-dev gfortran
    
    sudo pip install scipy

3.安装pandas：

    sudo pip install -i  https://pypi.mirrors.ustc.edu.cn/simple pytz
    
    sudo pip install -i  https://pypi.mirrors.ustc.edu.cn/simple pandas
    
4.安装scikit-learn

    sudo pip install sklearn


##安装界面播放软件

参考：https://www.jianshu.com/p/d6ff45e983ce
使用方法和参数表：https://forum.ubuntu.org.cn/viewtopic.php?t=39270

xwinwrap + mplayer

首先安装 mplayer 播放器：

    sudo apt install mplayer

然后下载 xwinwrap，我上传到百度云https://pan.baidu.com/s/1eSp8QJo 了，安装包只有 8KB，非常简单的代码。
解压提取后，接下来安装 xwinwrap64.deb：

    sudo dpkg -i xwinwrap64.deb

我只传 64 位的到百度云，需要 32位程序的去 Google Code 找吧。
那个 anibg 的安装包是一个前端界面，需要就装上吧。前端界面真的很多，我随便找一个的，就算不装前端界面也可以用。

    sudo dpkg -i anibg_v0.2.0.deb

安装有依赖问题通过 sudo apt install -f 修复即可。
因为我没装前端界面，所以我是在终端执行的：

    xwinwrap -ni -o 1.0 -fs -s -st -sp -b -nf -- mplayer -wid WID -quiet -nosound -loop 0 /视频/路径/文件.mov


