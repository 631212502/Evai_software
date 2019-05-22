# -*- coding: utf-8 -*-

#import urllib2 as ul_re
import urllib, urllib2, sys
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
#情绪分析的AK、SK
#AK='tliBsr6tzMKMgGencDCfGVLe'
#SK='t9ldoMGE4xFxPIfV6usGBI9kRL99GZp0'
#UNIT的AK、SK
#AK='qeDBC3emeshA7perzgil4b5r'
#SK='FRBV3VDyomDwmvPPMNcNkZVqkHiWLarI'
def accesstoken():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=qeDBC3emeshA7perzgil4b5r&client_secret=FRBV3VDyomDwmvPPMNcNkZVqkHiWLarI'#unit的AK和SK
    #host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=tliBsr6tzMKMgGencDCfGVLe&client_secret=t9ldoMGE4xFxPIfV6usGBI9kRL99GZp0'#自然语言处理（情绪倾向）的AK和SK
    request = urllib2.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib2.urlopen(request)
    content = response.read()
    #if (content):
        #print(content)
    a=str(content)
    #print(a)
    if a.find("access_token") !=-1:
    #           print(key)
        c=(a[a.find("access_token"):a.find("access_token")+1000])
        x=c.find(",")
        c=(c[0:x-1])
        content_str='{'+'"'+c+'"'+'}'
    ###eval将字符串转换成字典
    content_dir = eval(content_str)
    #print(content_dir )
    access_token =content_dir['access_token']
    print(access_token)
    return access_token
if __name__=="__main__":
	accesstoken()
