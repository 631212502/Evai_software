# coding=utf-8
import threading
import os
import time
import inspect
import ctypes
from time import ctime, sleep


# os.system("gnome-terminal -e 'xwinwrap -ni -o 1.0 -fs -s -st -sp -b -nf -- mplayer -wid WID -quiet -nosound -loop 0 /home/song/下载/M-system/evai_speech/resources/normal.mp4 -zoom -x 1920 -y 1080'") #背景
# os.system("gnome-terminal -e 'xwinwrap -ni -o 1.0 -fs -s -st -sp -a -nf -- mplayer -wid WID -quiet -nosound -loop 0 /home/song/下载/M-system/evai_speech/resources/normal.mp4 -zoom -x 1920 -y 1080'")#前景
# flag = 0
def open_xx(filename):
    os.system("aplay %s" % filename)
    # print "%s" %filename
    sleep(5)


def movie(filename):
    os.system("xwinwrap -ni -o 1.0 -fs -s -st -sp -a -nf -- mplayer -wid WID -quiet -nosound -loop 0 %s" % filename)
    # os.system("mplayer -wid WID -quiet -nosound -loop 0 %s" % filename)
    # print("movie-up")


def music(filename):
    global flag
    os.system("mplayer %s" % filename)
    print("music-up")
    # flag = 1
    os.system("pkill xwinwrap")


# print "%s" %filename
# sleep(5)
'''
threads = []
t1 = threading.Thread(target=movie,args=('/home/song/下载/M-system/evai_speech/resources/talk3.mp4 -zoom -x 1920 -y 1080',))  #表情库
threads.append(t1)
t2 = threading.Thread(target=music,args=('/home/song/下载/M-system/evai_speech/resources/huifu.mp3',))   #音源库
threads.append(t2)
'''


def playall():
    t = threading.Thread(target=movie, args=('/home/song/下载/M-system/evai_speech/resources/talk3.mp4 -zoom -x 1920 -y 1080',))  # 表情库
    t.start()
    time.sleep(0.5)
    os.system("mplayer /home/song/下载/M-system/evai_speech/resources/huifu.mp3")
    # print("main thread sleep finish")
    os.system("pkill mplayer")
    stop_thread(t)
    os.system("gnome-terminal -e 'xwinwrap -ni -o 1.0 -fs -s -st -sp -b -nf -- mplayer -wid WID -quiet -nosound -loop 0 /home/song/下载/M-system/evai_speech/resources/normal.mp4 -zoom -x 1920 -y 1080'")
    time.sleep(1)
    print("play-up")

def playMV():
    os.system("pkill mplayer")
    os.system("xwinwrap -ni -o 1.0 -fs -s -st -sp -a -nf -- mplayer -wid WID -quiet -loop 1 /home/song/下载/M-system/evai_speech/resources/heal.mp4 -zoom -x 1920 -y 1080")
    # print("main thread sleep finish")
    os.system("gnome-terminal -e 'xwinwrap -ni -o 1.0 -fs -s -st -sp -a -nf -- mplayer -wid WID -quiet -nosound -loop 0 /home/song/下载/M-system/evai_speech/resources/normal.mp4 -zoom -x 1920 -y 1080'")
    time.sleep(1)
    print("play-up")

def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


if __name__ == '__main__':
    playall()
    '''
    os.system("gnome-terminal -e 'xwinwrap -ni -o 1.0 -fs -s -st -sp -b -nf -- mplayer -wid WID -quiet -nosound -loop 0 /home/evai/下载/M-system/evai_speech/resources/normal.mp4 -zoom -x 1920 -y 1080'")
    sleep(2)
    for t in threads:
        t.setDaemon(True)
        t.start()
    #t.join()
    os.system("gnome-terminal -e 'xwinwrap -ni -o 1.0 -fs -s -st -sp -b -nf -- mplayer -wid WID -quiet -nosound -loop 0 /home/evai/下载/M-system/evai_speech/resources/normal.mp4 -zoom -x 1920 -y 1080'")
    print('i am ok')
    '''

'''
    t1 = threading.Thread(target=movie,args=('/home/evai/下载/M-system/evai_speech/resources/talk3.mp4 -zoom -x 1920 -y 1080',))  # 表情库
    t2 = threading.Thread(target=music, args=('/home/evai/下载/M-system/evai_speech/resources/huifu.mp3',))  # 音源库
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    sleep(4)
    print("main-up")
'''
