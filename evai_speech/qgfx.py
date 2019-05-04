# -*- coding: utf-8 -*-
import urllib2
import urllib
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#says=input('你想说的话：')
def IQ(says):   
	access_token = '24.89c0ed35a0be3a5ac3738a29bce0dc38.2592000.1559529608.282335-14587585'
	url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/emotion?access_token=' + access_token
	post_data = '{\"text\":\"'+says+'\"}'
	unicodeData = post_data.decode("UTF-8")
	gbkData = unicodeData.encode("GBK")
	request = urllib2.Request(url, gbkData)
	request.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(request)
	content = response.read()
	#print(content)
	result=str(content)
	g=(eval(result))
	#print(g)
	qx=g['items'][0]['label']
	zx=g['items'][0]['prob']
	#qgc=qx*zx
	if qx=='optimistic':
		qgc=1*zx
	if qx=='pessimistic':
		qgc=-1*zx
	if qx=='neutral':
		qgc=0
	print('情感倾向：'+str(qx)+'置信度'+str(zx))
	print('情绪分析反馈的影响值：'+str(qgc))
	return qgc
if __name__=="__main__":
	says=raw_input('你想说的话：')
	IQ(says)

