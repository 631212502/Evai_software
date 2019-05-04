#!/usr/bin/python2
#coding=utf-8
from urllib import urlopen, quote
import urllib2
import urllib
import sys
import signal
import os
import time
import collections
import wave  
import pyaudio
import snowboydetect
import re
import json


import baidu_speech as bdsp
from RFUNITrobot import UNITbigturn,unitone
from emotion_detect import get_emotion

RESOURCE_FILE = "resources/common.res"
DETECT_DING = "resources/ding.wav"
DETECT_DONG = "resources/dong.wav"
#model = 'resources/smart_mirror.umdl'
#model = 'resources/xiaobai.pmdl'
model = 'resources/jarvis.pmdl'
sensitivity = '0.3'  #敏感度
audiogain = 0.3  #增益

detector = snowboydetect.SnowboyDetect(resource_filename=RESOURCE_FILE, model_str=model)
detector.SetSensitivity(sensitivity)
detector.SetAudioGain(audiogain)

ring_buffer = collections.deque(maxlen=(detector.NumChannels() * detector.SampleRate()*5))

def audio_callback(in_data, frame_count, time_info, status):
    ring_buffer.extend(in_data)
    play_data = chr(0) * len(in_data)
    return play_data, pyaudio.paContinue

audio = pyaudio.PyAudio()
stream_in = audio.open(
            input=True, output=False,
            format=audio.get_format_from_width(detector.BitsPerSample()/8),
            channels=detector.NumChannels(),
            rate=detector.SampleRate(),
            frames_per_buffer=2048,
            stream_callback=audio_callback)

print('format = %d' % audio.get_format_from_width(detector.BitsPerSample()/8))
print('channels = %d' %detector.NumChannels())
print('rate = %d' % detector.SampleRate())


def save_wave_file(filename, data):    #存放
    wf = wave.open(filename, 'wb')  
    wf.setnchannels(1)  
    wf.setsampwidth(2)  
    wf.setframerate(16000)  
    wf.writeframes("".join(data))  
    wf.close() 

def play_audio_file(fname=DETECT_DING):   #播放
    ding_wav = wave.open(fname, 'rb')
    ding_data = ding_wav.readframes(ding_wav.getnframes())
    audio = pyaudio.PyAudio()
    stream_out = audio.open(
        format=audio.get_format_from_width(ding_wav.getsampwidth()),
        channels=ding_wav.getnchannels(),
        rate=ding_wav.getframerate(), input=False, output=True)
    stream_out.start_stream()
    stream_out.write(ding_data)
    time.sleep(0.2)
    stream_out.stop_stream()
    stream_out.close()
    audio.terminate()

def detected_callback():
    global gender
    global text
    face_emotion=0
    text='1'
    rec_count = 0
    sil_count = 0
    save_buffer = [] 
    waite_count = 0
    face_count=0
    human=get_emotion()
    face=human[0]
    gender=human[1]
    #global gender
    #gender="default"
    #age="default"
    #face = 1
    sessiontemp1=""# 多轮对话每轮对话标识位，初值为空
    while True:
        try:
            data = bytes(bytearray(ring_buffer))
            ring_buffer.clear()
            #data = stream_in.read(4000)
            
            if len(data) == 0:
                time.sleep(0.1)
                if  rec_count == 0:
                    face_count+=1
                    #print(face_count)
                if face_count==130:
                    print ('emotion detect')
                    print(face_count)
		    human=get_emotion()
                    face=human[0]
		    gender=human[1]
                    face_emotion=unitone(face,gender)
                    if face_emotion==1:
                        print('face_emotion='+str(face_emotion))
                        rec_count = 1
                    face_count=0
                
                waite_count +=1
                #print'sleeping'
                continue
    
            ans = detector.RunDetection(data)
            if ans is 1:
                print('hotword dectect')
                play_audio_file('resources/ding.wav')
                #save_buffer = []  #触发唤醒词清空录音
                rec_count = 1
                
                #data = stream_in.read(800)
                data = bytes(bytearray(ring_buffer))
                ring_buffer.clear()
            elif ans is 0:      
                if rec_count > 0:
                    print('voice')
                    save_buffer.append(data)
                    rec_count += 1 
                    sil_count = 0
            elif ans is -2 or hangout_count>150:    
                if rec_count > 0:
                    save_buffer.append(data)
                    sil_count += 1
                    print('silence')
                if (sil_count > 2 and rec_count > 2):
                    filename = "resources/rec.wav"  
                    save_wave_file(filename, save_buffer) 
                    text = bdsp.baidu_asr(filename)
		    text = text.encode("utf-8")  #将unicode转化为utf-8编码
		    print(type(text))
                    #play_audio_file('resources/dong.wav')
                    print('rec asr %s' % text)                
                    if text.find('识别错误')==-1:
                        sessiontemp1=UNITbigturn(face,text,sessiontemp1,gender)
                        #ring_buffer.clear()
                    ring_buffer.clear()  #防止存到BOT的声音
                    #select bot
                    '''
                    bot=UNITbigturn(face)
                    if bot == 0 :
                        sessiontemp1=unitnatural(text,sessiontemp1)
                    elif bot == 1 :
                        sessiontemp1=unitwarm(text,sessiontemp1)
                    '''
                    #UNITbigturn(face,text)
                    #print('type text: %s' % type(text))
                    rec_count = 1
                    sil_count = 0
                    save_buffer = []
            if text.find('退')!=-1 and text.find('出')!=-1:
                rec_count=0
                text='1'
                print('Listening...')
        except KeyboardInterrupt:
            break
    print("end")

if __name__ == "__main__":
    print('Listening...')
    detected_callback()


