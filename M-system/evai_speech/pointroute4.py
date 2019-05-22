# -*- coding: utf-8 -*-

import random
import json
import urllib
import re
import urllib2
import csv
# from urllib.request import urlopen, quote
from urllib import urlopen, quote
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def findroute(a, b):
    origin = a
    destination = b
    #    ak=GySjGjcNwh0TtNDPlOHr6E5kv9zTzs0L
    url = 'http://api.map.baidu.com/directionlite/v1/transit?' + 'origin=' + origin + '&destination=' + destination + '&ak=GySjGjcNwh0TtNDPlOHr6E5kv9zTzs0L'
    # data = json.dumps(post_data).encode('utf-8')
    # headers = {'Content-Type': 'application/json'}

    # req = ul_re.request.urlopen(url)#JSON格式的返回数据
    response = urllib.urlopen(url)
    content = response.read()
    result = str(content).encode('utf-8')
    # result = str(content,'utf-8')
    # result1 = hjson["routes"]["steps"]["schemes"]["instructions"]
    #print(result)
    m = json.loads(result)
    step = m["result"]['routes'][0]['steps']
    #print(step)
    count=len(step)
    #print(count)
    distance = '距离大概' + str(m["result"]['routes'][0]['distance']) + '米'
    h = str(round(m["result"]['routes'][0]['duration'] / 3600, 2)) + '个小时'
    minues = str(round((m["result"]['routes'][0]['duration'] % 3600) / 60)) + '分钟'
    #s = str((m["result"]['routes'][0]['duration'] % 3600) % 60) + '秒。'
    time = ',预计耗时' + h + minues
    i=0
    repeat = ""
    while i<count:
        step[i] = "第"+str(i+1)+"步："+m["result"]['routes'][0]['steps'][i][0]['instruction']+"；"
        repeat = repeat + step[i]
        i=i+1
    tt='嘿黑，最佳出行路线！'+distance+time+'路线有'+str(count)+"步："+repeat
    #print(tt)
    return tt

def findrouteshort(a, b):
    origin = a
    destination = b
    #    ak=GySjGjcNwh0TtNDPlOHr6E5kv9zTzs0L
    url = 'http://api.map.baidu.com/direction/v2/riding?' + 'origin=' + origin + '&destination=' + destination + '&ak=GySjGjcNwh0TtNDPlOHr6E5kv9zTzs0L'
    '''
    post_data  = {
                "request": {
                        "origin":"东莞理工学院",
                        "destination":"华南理工大学",
                        "coord_type":'bd09ll',
                        'tactics_incity':0,
                        "tactics_intercity":0,
                        'trans_type_intercity':0,
                        'ret_coordtype':0,
                        'output':json,
                        'page_size':3,
                        'page_index':1,
                        'ak':'GySjGjcNwh0TtNDPlOHr6E5kv9zTzs0L',
        }
    '''
    # data = json.dumps(post_data).encode('utf-8')
    # headers = {'Content-Type': 'application/json'}

    # req = ul_re.request.urlopen(url)#JSON格式的返回数据
    response = urllib.urlopen(url)
    content = response.read()
    result = str(content).encode("utf-8")
    # result = str(content,'utf-8')
    # result1 = hjson["routes"]["steps"]["schemes"]["instructions"]
    print(result)
    #m = json.loads(result)


    #tt = ('为您推荐以下方案：' + '从' + instructions + distance + time + '，祝您出行愉快。')
    #return tt


def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    #    ak = 'GySjGjcNwh0TtNDPlOHr6E5kv9zTzs0L'
    add = quote(address)  # 由于本文城市变量为中文，为防止乱码，先用quote进行编码
    uri = url + '?' + 'address=' + add + '&output=' + output + '&ak=' + 'GySjGjcNwh0TtNDPlOHr6E5kv9zTzs0L'
    req = urlopen(uri)
    res = req.read().decode()  # 将其他编码的字符串解码成unicode temp = json.loads(res) #对json数据进行解析 return temp
    # print(req)
    temp = json.loads(res)  # 对json数据进行解析
    # print(temp)

    return temp


def Navigation(g, k):
    b = g  # 将第一列city读取出来并清除不需要字符
    c = k  # 将第二列price读取出来并清除不需要字符
    lng = getlnglat(b)['result']['location']['lng']  # 采用构造的函数来获取经度
    lat = getlnglat(b)['result']['location']['lat']  # 获取纬度
    lng2 = getlnglat(c)['result']['location']['lng']  # 采用构造的函数来获取经度
    lat2 = getlnglat(c)['result']['location']['lat']  # 获取纬度
    str_temp = '{"count":' + str(b) + '，"lat":' + str(lat) + ',"lng":' + str(lng) + '},'
    str_temp2 = '{"count":' + str(c) + '，"lat":' + str(lat2) + ',"lng":' + str(lng2) + '},'
    # print(str_temp)
    # print(str_temp2)
    a = str(lat) + ',' + str(lng)
    b = str(lat2) + ',' + str(lng2)
    # print(a)
    # print(b)
    gg = findroute(a, b)
    #gg = findrouteshort(a, b)
    return gg

if __name__=="__main__":
	g = raw_input('出发地：')
	k = raw_input('目的地：')
	tt=Navigation(g, k)
	print(tt)
