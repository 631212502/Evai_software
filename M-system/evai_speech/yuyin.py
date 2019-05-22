# -*- coding: utf-8 -*- 
from aip import AipSpeech

""" 你的 APPID AK SK """
def synthesis(res,filepath):
    APP_ID = '11634694'
    API_KEY = 'qeDBC3emeshA7perzgil4b5r'
    SECRET_KEY = 'FRBV3VDyomDwmvPPMNcNkZVqkHiWLarI'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


    result  = client.synthesis(res, 'zh', 1, {
        'vol': 1,'per':4,'aue':6,})#还没弄懂怎么发送文件类的请求

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open(filepath, 'wb') as f:
            f.write(result)

def synthesis_boy(res,filepath):
    APP_ID = '11634694'
    API_KEY = 'qeDBC3emeshA7perzgil4b5r'
    SECRET_KEY = 'FRBV3VDyomDwmvPPMNcNkZVqkHiWLarI'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


    result  = client.synthesis(res, 'zh', 1, {
        'vol': 1,'per':3,'aue':6,})#还没弄懂怎么发送文件类的请求

    print("male_voice")

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open(filepath, 'wb') as f:
            f.write(result)

if __name__=="__main__":
	synthesis('我在','/home/evai/下载/M-system/evai_speech/resources/wozai.mp3')
