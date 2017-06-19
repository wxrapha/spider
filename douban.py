# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/6/18 下午12:44'

import urllib, urllib2, cookielib

filename = 'cookiedouban.txt'
cookiedouban = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiedouban))
geturl = "https://www.douban.com/"
values = {
    'form_email': '15062255019',
    'form_password': 'xh940723'
}
data = urllib.urlencode(values)
result = opener.open(geturl, data)
cookiedouban.save(ignore_discard=True, ignore_expires=True)
gradeUrl = 'https://movie.douban.com'
result = opener.open(geturl)
print result.read()
