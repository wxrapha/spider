# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/6/18 下午12:44'


import urllib
import urllib2
import cookielib
import re


class DouBan:
    def __init__(self):
        #登陆URL
        self.loginUrl = 'https://www.douban.com/accounts/login'
        #CookieJar对象
        self.cookies = cookielib.CookieJar()
        #表单数据
        self.postdata = urllib.urlencode({
            'form_email': '账号',
            'form_password': '密码'
        })
        #构建opener
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
    #获取页面
    def getPage(self):
        request = urllib2.Request(
            url=self.loginUrl,
            data=self.postdata)
        result = self.opener.open(request)
        print result.read()

douban = DouBan()
douban.getPage()
