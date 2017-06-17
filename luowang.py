# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/6/12 下午2:42'

import requests
import re

word = raw_input("Input key word: ")
url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+word+'&ct=201326592&v=flip'
result = requests.get(url)

html = requests.get(url).text
pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
i = 0
for each in pic_url:
    print each
    try:
        pic = requests.get(each,timeout = 10)
    except requests.exceptions.ConnectionError:
        print '错误:当前图片无法下载'
        continue
    string = 'pictures\\' + str(i) + '.jpg'
    fp = open(string, 'wb')
    fp.write(pic.content)
    fp.close()
    i += 1