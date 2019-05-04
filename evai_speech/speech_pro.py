#encoding=utf-8
from aip import AipSpeech
import requests
import base64
import os
import audioop
import wave


def wave2txt(file):
    #file = 'output.wav'
    print("111")
    TokenIp = 'https://openapi.baidu.com/oauth/2.0/token'
    url = 'http://vop.baidu.com/pro_api'
    APP_ID = '11510290'
    API_KEY = 'Sax2ejAAiY6qGHgoKSv9kGNw'
    SECRET_KEY = 'oMyegqabIjGxxXEkRztjDqoVg7xPpUVl'
     
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
     
    r = requests.post(TokenIp+'?grant_type=client_credentials&client_id='+API_KEY+'&client_secret='+SECRET_KEY)
    token = r.json()["access_token"]
     
    # print token
    length = os.path.getsize(file)
    base =base64.b64encode(get_file_content(file))
    json_data = {
        "format":"wav",
        "rate":16000,
        "dev_pid":1537,
        "channel":1,
        "token":token,
        "cuid":"haixuanfeng",
        "speech":base,
        "len":length
    }
    r = requests.post(url,json=json_data)
    if r.json()["err_no"]==0:
        print r.json()["result"]
        
    # convert json to string 
    temp=str(r.json()["result"])
     
    # remove the [u'.......'], string
    b = temp[3:-2]
     
    # convert string to unicode, the output is Chinese
    c_unicode = b.decode('unicode-escape')
    print(c_unicode)
    return c_unicode
    # determine if there is a keyword
    '''
    if c_unicode.find(u"是") != -1:
        print "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
    '''
    '''
print 'testing........'
wave2txt()
'''
if __name__=="__name__":
	file = '/home/evai/下载/16k.wav'
	gg=wave2txt(file)
	print("gg")
