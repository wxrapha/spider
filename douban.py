# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/6/18 下午12:44'


import urllib
import urllib2
import cookielib
import re


class DouBan:
    def __init__(self):

        self.loginUrl = 'https://www.douban.com/accounts/login'

        self.cookies = cookielib.CookieJar()

        self.postdata = urllib.urlencode({
            'form_email': '15062255019',
            'form_password': 'xh940723'
        })

        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))

    def getPage(self):
        request = urllib2.Request(
            url=self.loginUrl,
            data=self.postdata)
        result = self.opener.open(request)
        print result.read()

douban = DouBan()
douban.getPage()
