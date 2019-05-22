# -*- coding: utf-8 -*-

# unit的模型调用代码（evai版本）
# import urllib2 as ul_re
from urllib import urlopen, quote
import urllib2
#import urllib.request as ul_re
import urllib
import json
import random
import sys
import time
import chardet
import re
import os
import threading
from time import ctime,sleep
from qgfx import *
from accesstoken import *
from pointroute4 import *
from yuyin import synthesis,synthesis_boy
from FBrf import Training,Training2
from playthread import playall,playMV

#from BaiduTest import wave2txt
#from zht_speech import detected_asr
# accesstoken的获取
# access_token =accesstoken()#重新从API中获取
global access_token
access_token = '24.0a8fca54650892dcc14c46c5db82cf86.2592000.1559531713.282335-11634694'
# print(access_token)
global state
state = random.uniform(30, 50)  # 状态参数每次交互重新在40和60之间随机生成
gender="default"
feedback = 1
sessiontemp1="" 

def unitwarm(says,sessiontemp1,gender):   #使用warmBOT进行交互
    #global rel  #rel代表时间保持
    #global state   #state代表即时感知
    print(says)
    #sessiontemp1 = ""  # 多轮对话每轮对话标识位，初值为空
    intent = ''         #意图标识位，用于多轮对话退出
    #print('M=' + str(state))
    #print("R=" + str(rel))     
    #says = raw_input("May i help you?")
    print('In-warmBOT')
    global access_token
    #print(sessiontemp1)
    '''
    #UNIT的对话层
    '''

    url = 'https://aip.baidubce.com/rpc/2.0/unit/bot/chat?access_token=' + access_token
    post_data = {
        "bot_session": sessiontemp1,
        "log_id": "7758521",
        "request": {
            "bernard_level": 0,
            "client_session": "{\"client_results\":\"\", \"candidate_options\":[]}",
            "query": says,
            "query_info": {
                "asr_candidates": [],
                "source": "KEYBOARD",
                "type": "TEXT"
            },
            "updates": "",
            "user_id": "88888"
        },
        "bot_id": "8651",
        "version": "2.0"
    }
    # print(post_data)
    post_data = json.dumps(post_data, ensure_ascii=False, encoding='utf-8')
    request = urllib2.Request(url, post_data)
    request.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(request)
    content = response.read()
    result = str(content)
    #print(result)     #json数据输出
    g = json.loads(result)
    a = str(g)
    repeat = g['result']['response']['action_list'][0]['say']
    print(type(repeat))
    custom_reply =g['result']['response']['action_list'][0]['custom_reply']
    print(custom_reply)
    # w = g['result']['bot_session']
    # print(w)
    ty = g['result']['response']['action_list'][0]['type']
    print(ty)   #ty为BOT的理解状态    # for key,value in d.items():
    # 多轮对话传参
    if a.find("bot_session") != -1:#（老方法待更新）
        #           print(key)
        c = (a[a.find("session_id"):a.find("session_id") + 10000])
        x = c.find(",")
        c = (c[0:x - 5])
        sessiontemp1 = '{' + '"' + c + '"' + '}'
        #print('多轮对话传递参数：'+sessiontemp1)
    if ty.find("failure") != -1: #备选交互BOT
        print('调用备选BOT')
        repeat=unitchat(says)
    if a.find("font-size") != -1: #处理格式问题（老方法待更新）
        f = (a[a.find("font-size"):a.find("font-size") + 1000])
        x = f.find(",")
        f = (f[16:x - 9])
        repeat = f
    if repeat.find(u'以下哪个问题')!=-1:
        print('调用备选BOT')
        repeat=unitchat(says)
        
    '''
    UNIT的应用调用层（采用if分支形式）
    '''
    if custom_reply.find("SONG") != -1 or (says.find("唱") != -1 and says.find("首") != -1 and says.find("歌") != -1):  # 歌曲功能
        repeat="我想想，好吧，唱给你听吧"
    if custom_reply.find("Healing") != -1 :  # 视频功能
        repeat="看样子你是真的伤心了呢"
        synthesis(repeat,'/home/song/下载/M-system/evai_speech/resources/huifu.mp3')
        os.system("mplayer /home/song/下载/M-system/evai_speech/resources/huifu.mp3")
        print("video")
        repeat="感觉好点了吗"
        os.system("mplayer -o local /home/evai/下载/M-system/evai_speech/resources/heal.mp4")
    if custom_reply.find("Navigation") != -1:  #导航功能
        synthesis('emmm让我想一下','/home/song/下载/M-system/evai_speech/resources/huifu.mp3')
        os.system("mplayer /home/song/下载/M-system/evai_speech/resources/huifu.mp3")
        zhongdian = g['result']['response']['schema']['slots'][0]['normalized_word']
        qidian = g['result']['response']['schema']['slots'][2]['normalized_word']
        # print(qidian)
        # print(zhongdian)
        qidian = str(qidian)
        zhongdian = str(zhongdian)
        repeat = Navigation(qidian, zhongdian)
    
    # IQ(repeat)
    #play
    print(repeat)
    print(gender)
    if gender=="default" or gender=="male":
        synthesis(repeat,'/home/song/下载/M-system/evai_speech/resources/huifu.mp3')
    if gender=="female":
        synthesis_boy(repeat,'/home/song/下载/M-system/evai_speech/resources/huifu.mp3')
    #synthesis(repeat,'/home/pi/ASR_speech/huifu.mp3')
    #os.system("aplay /home/evai/下载/M-system/evai_speech/resources/huifu.mp3")
    playall()
    if custom_reply.find("SONG") != -1 or (says.find("唱") != -1 and says.find("首") != -1 and says.find("歌") != -1):  # 歌曲功能
        print("sing")
        playMV()
    if repeat.find(u'唤')!=-1 and repeat.find(u'醒')!=-1 and repeat.find(u'我')!=-1:
        #os.system("/home/pi/ASR_speech/wakeup_trigger_start.sh")
        os.system("/home/song/下载/M-system/evai_speech/enter_trigger_start.sh")
    '''
    if g['result']['response']['schema']['intent'] != intent :
        sessiontemp1="" # 多轮对话每轮对话标识位，初值为空
    '''
    return sessiontemp1          
        
def unitnatural(says,sessiontemp1,gender):   #使用warmBOT进行交互
    #global rel  #rel代表时间保持
    #global state   #state代表即时感知
    sessiontemp1 = ""  # 多轮对话每轮对话标识位，初值为空
    intent = ''
    #print("R=" + str(rel))
    #says = raw_input("May i help you?")
    print('In-naturalBOT')
    #参数调整
    #rel = rel + fix  # rel表征交互人的影响
    #print(sessiontemp1)

    '''
    #UNIT的对话层
    '''
    global access_token
    url = 'https://aip.baidubce.com/rpc/2.0/unit/bot/chat?access_token=' + access_token
    post_data = {
        "bot_session": sessiontemp1,
        "log_id": "7758521",
        "request": {
            "bernard_level": 0,
            "client_session": "{\"client_results\":\"\", \"candidate_options\":[]}",
            "query": says,
            "query_info": {
                "asr_candidates": [],
                "source": "KEYBOARD",
                "type": "TEXT"
            },
            "updates": "",
            "user_id": "88888"
        },
        "bot_id": "8744",
        "version": "2.0"
    }
    # print(post_data)
    post_data = json.dumps(post_data, ensure_ascii=False, encoding='utf-8')
    request = urllib2.Request(url, post_data)
    request.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(request)
    content = response.read()
    result = str(content)
    #print(result)     #json数据输出
    g = json.loads(result)
    a = str(g)
    repeat = g['result']['response']['action_list'][0]['say']
    #print(type(repeat))
    custom_reply = g['result']['response']['action_list'][0]['custom_reply']
    # w = g['result']['bot_session']
    # print(w)
    print(custom_reply)
    ty = g['result']['response']['action_list'][0]['type']
    print(ty)   #ty为BOT的理解状态
    # for key,value in d.items():
    # 多轮对话传参
    if a.find("bot_session") != -1:
        #           print(key)
        c = (a[a.find("session_id"):a.find("session_id") + 10000])
        x = c.find(",")
        c = (c[0:x - 5])
        sessiontemp1 = '{' + '"' + c + '"' + '}'
        #print('多轮对话传递参数：'+sessiontemp1)
    if ty.find("failure") != -1: #备选交互BOT
        print('调用备选BOT')
        repeat=unitchat(says)
    if a.find("font-size") != -1: #处理格式问题
        f = (a[a.find("font-size"):a.find("font-size") + 1000])
        x = f.find(",")
        f = (f[16:x - 9])
        repeat = f
    if repeat.find(u'以下哪个问题')!=-1:
        print('调用备选BOT')
        repeat=unitchat(says)

    '''
    UNIT的应用调用层（采用if分支形式）
    '''
    if custom_reply.find("SONG") != -1 or (says.find("唱") != -1 and says.find("首") != -1 and says.find("歌") != -1):  # 歌曲功能
        repeat="我想想，好吧，唱给你听吧"
    if custom_reply.find("Navigation") != -1:  #导航功能
        zhongdian = g['result']['response']['schema']['slots'][0]['normalized_word']
        qidian = g['result']['response']['schema']['slots'][2]['normalized_word']
        # print(qidian)
        # print(zhongdian)
        qidian = str(qidian)
        zhongdian = str(zhongdian)
        repeat = Navigation(qidian, zhongdian)
    if custom_reply.find("Healing") != -1:  # 视频功能
        repeat="看样子你是真的伤心了呢"
        synthesis(repeat,'/home/song/下载/M-system/evai_speech/resources/huifu.mp3')
        os.system("aplay /home/song/下载/M-system/evai_speech/resources/huifu.mp3")
        print("video")
        repeat="感觉好点了吗"
        os.system("mplauer /home/song/下载/M-system/evai_speech/resources/heal.mp4")
    
    # IQ(repeat)
    print(repeat)
    print(gender)
    if gender=="default" or gender=="male":
        synthesis(repeat,'/home/song/下载/M-system/evai_speech/resources/huifu.mp3')
    if gender=="female":
        synthesis_boy(repeat,'/home/song/下载/M-system/evai_speech/resources/huifu.mp3')
    #synthesis(repeat,'/home/pi/ASR_speech/huifu.mp3')
    #os.system("aplay /home/evai/下载/M-system/evai_speech/resources/huifu.mp3")
    playall()
    if custom_reply.find("SONG") != -1 or (says.find("唱") != -1 and says.find("首") != -1 and says.find("歌") != -1):  # 歌曲功能
        print("sing")
        playMV()
    if repeat.find(u'唤')!=-1 and repeat.find(u'醒')!=-1 and repeat.find(u'我')!=-1:
        print "enter module"
        #os.system("/home/pi/ASR_speech/wakeup_trigger_start.sh")
        #os.system("/home/evai/下载/M-system/evai_speech/resources/enter_trigger_start.sh")
    if g['result']['response']['schema']['intent'] != intent :
        sessiontemp1="" # 多轮对话每轮对话标识位，初值为空
#    if repeat.find('唤醒我')!=1:
#	print "enter module"
#        os.system("python /home/pi/ASR_speech/dueros/DuerOS-Python-Client/app/wakeup_trigger_main.py")
    return sessiontemp1  

def unitchat(says):   #使用自建chat/闲聊BOT进行交互
    global access_token
    url = 'https://aip.baidubce.com/rpc/2.0/unit/bot/chat?access_token=' + access_token
    post_data = {
        "bot_session": '',
        "log_id": "7758521",
        "request": {
            "bernard_level": 0,
            "client_session": "{\"client_results\":\"\", \"candidate_options\":[]}",
            "query": says,
            "query_info": {
                "asr_candidates": [],
                "source": "KEYBOARD",
                "type": "TEXT"
            },
            "updates": "",
            "user_id": "88888"
        },
        "bot_id": "13707",
        "version": "2.0"
    }
    post_data= json.dumps(post_data, ensure_ascii=False, encoding='utf-8')
    request = urllib2.Request(url, post_data)
    request.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(request)
    content = response.read()
    result = str(content)
    # print(result)     #json数据输出
    g = json.loads(result)
    a = str(g)
    repeat = g['result']['response']['action_list'][0]['say']
    print(repeat)
    return repeat

def unitone(face,gender):#使用warmBOT进行zhudong交互
    #global rel  #rel代表时间保持
    Initiative = random.uniform(0, 100)#主动性
    if face == 50 :
        says = "喜转哀"
    elif face == 10:
        says = "喜转怒"
    else:
        return 0
    '''
    #UNIT的对话层
    '''
    global access_token
    url = 'https://aip.baidubce.com/rpc/2.0/unit/bot/chat?access_token=' + access_token
    post_data = {
        "bot_session": '',
        "log_id": "7758521",
        "request": {
            "bernard_level": 0,
            "client_session": "{\"client_results\":\"\", \"candidate_options\":[]}",
            "query": says,
            "query_info": {
                "asr_candidates": [],
                "source": "KEYBOARD",
                "type": "TEXT"
            },
            "updates": "",
            "user_id": "88888"
        },
        "bot_id": "8651",
        "version": "2.0"
    }
    # print(post_data)
    post_data = json.dumps(post_data, ensure_ascii=False, encoding='utf-8')
    request = urllib2.Request(url, post_data)
    request.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(request)
    content = response.read()
    result = str(content)
    #print(result)     #json数据输出
    g = json.loads(result)
    a = str(g)
    repeat = g['result']['response']['action_list'][0]['say']
    #synthesis(repeat,'/home/pi/ASR_speech/huifu.mp3')
    print(gender)
    if gender=="default" or gender=="male":
        synthesis(repeat,'/home/evai/下载/M-system/evai_speech/resources/huifu.mp3')
    if gender=="female":
        synthesis_boy(repeat,'/home/pi/ASR_speech/huifu.mp3')
    #os.system("aplay/home/evai/下载/M-system/evai_speech/resources/huifu.mp3")
    #playall()
    return 1



        
# 大循  UNIT的智能交互调用逻辑/决策树   # 函数体外的参数初值;还差离散数据线性化以及概率化
def UNITbigturn(face,says,gender):  
    global state
    global feedback
    global sessiontemp1
    #print("inRF")
    #global rebase
    #rebase = 50.0  # 情绪平和基线
    #global rel
    fix = IQ(says)
    state = state + 10 * fix
    print ('emotion-state='+str(state))
    #检验反馈学习
    if fix >=0 :
        feedback = 1
    else:
        feedback = 0
        print("您对我的表现不满意么，我改，让我想想该怎么答复你")
        #os.system("aplay /home/pi/ASR_speech/resources/FB.mp3")  #播放展示学习过程
    print("feedback"+str(feedback))
    bot=Training2(face,state,feedback)
    print('rfbot:'+str(bot))
    #print("botselect:"+str(bot))
    #print(type(says))
    if bot == 1:
        sessiontemp1=unitwarm(says,sessiontemp1,gender)
    elif bot == 0:
        sessiontemp1=unitnatural(says,sessiontemp1,gender)
        #sessiontemp1=unitwarm(says,sessiontemp1,gender)
    #return sessiontemp1


def unittest():
    global state
    global qgc
    global rebase
    global gender
    # 函数体外的参数初值                还差离散数据线性化以及概率化
    # 全局均为柔性参数
    state = random.uniform(40, 60)  # 状态参数每次交互重新在40和60之间随机生成
    rebase = 50.0  # 情绪平和基线
    sessiontemp1=""
    global rel
    global sessiontemp
    sessiontemp = 0  # 对话轮数标记
    #face = raw_input("your face")
    while True:
        says = raw_input("How do you do?")
        #print(type(says))
        gender='default'
        #sessiontemp1=unitwarm(says,sessiontemp1,gender)
	sessiontemp1=unitnatural(says,sessiontemp1,gender)


if __name__=="__main__":
	unittest()#3.19,check out


