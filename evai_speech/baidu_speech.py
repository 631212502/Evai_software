#!/usr/bin/python2
# -*- coding: utf-8 -*- 
# 引入Speech SDK
from aip import AipSpeech
import re
# 定义常量
'''
APP_ID = '11634694'
API_KEY = 'qeDBC3emeshA7perzgil4b5r'
SECRET_KEY = "FRBV3VDyomDwmvPPMNcNkZVqkHiWLarI"
'''
APP_ID = '11510290'
API_KEY = 'Sax2ejAAiY6qGHgoKSv9kGNw'
SECRET_KEY = "oMyegqabIjGxxXEkRztjDqoVg7xPpUVl"
# 初始化AipSpeech对象
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
def baidu_asr(file_name):
    res = aipSpeech.asr(get_file_content(file_name), 'wav', 16000, {'lan': 'zh',})
    if 'result' in res.keys():
        return res['result'][0]
	text = text.decode('utf-8')
        text=re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode("utf8"), "".decode("utf8"),text)
        text=text.encode('utf-8')
        return text
    else:
        return '识别错误！'
        text=text.decode('utf-8')
        return text

def baidu_tts(text, file_name):#语音合成
    result  = aipSpeech.synthesis(text, 'zh', 1, {'vol': 5,})
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open(file_name, 'wb') as f:
            f.write(result)    

if __name__ == "__main__":
    pass

