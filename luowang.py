# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/6/12 下午2:42'

import requests
import re

url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E6%9A%B4%E8%B5%B0%E6%BC%AB%E7%94%BB&ct=201326592&ic=0&lm=-1&width=&height=&v=flip'

html = requests.get(url).text
pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
i = 0
for each in pic_url:
    print each
    try:
        pic = requests.get(each,timeout = 10)
    except requests.exceptions.ConnectionError:
        print '错误'
        continue
    string = 'pictures\\' + str(i) + '.jpg'
    fp = open(string, 'wb')
    fp.write(pic.content)
    fp.close()
    i += 1