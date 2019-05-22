#coding=utf-8
import threading
import time
import inspect
import ctypes
import os

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


def movie(filename):
    os.system("xwinwrap -ni -o 1.0 -fs -s -st -sp -a -nf -- mplayer -wid WID -quiet -nosound -loop 0 %s" %filename)
    #os.system("mplayer  -quiet -nosound -loop 0 %s" % filename)
    print("movie-up")


def music(filename):
    os.system("mplayer %s" %filename)
    print("music-up")
    #flag = 1
    os.system("pkill xwinwrap")
   	#print "%s" %filename
   	#sleep(5)


if __name__ == "__main__":
    os.system("gnome-terminal -e 'xwinwrap -ni -o 1.0 -fs -s -st -sp -a -nf -- mplayer -wid WID -quiet -nosound -loop 0 /home/evai/下载/M-system/evai_speech/resources/normal.mp4 -zoom -x 1920 -y 1080'")
    time.sleep(3)
    t = threading.Thread(target=movie,args=('/home/evai/下载/M-system/evai_speech/resources/talk3.mp4 -zoom -x 1920 -y 1080',))  # 表情库
    t.start()
    #time.sleep(5)
    os.system("mplayer /home/evai/下载/M-system/evai_speech/resources/wake1.mp3")
    #print("main thread sleep finish")
    os.system("pkill mplayer")
    stop_thread(t)
    os.system("gnome-terminal -e 'xwinwrap -ni -o 1.0 -fs -s -st -sp -b -nf -- mplayer -wid WID -quiet -nosound -loop 0 /home/evai/下载/M-system/evai_speech/resources/normal.mp4 -zoom -x 1920 -y 1080'")
    time.sleep(1)
    #print("main thread sleep finish2")
