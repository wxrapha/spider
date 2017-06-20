# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/6/20 下午1:40'

import urllib
import urllib2
import re
import cookielib


class SJXY:
    def getVIEW(Page):
        view = r'name="__VIEWSTATE" value="(.+)" '
        view = re.compile(view)
        return view.findall(Page)[0]

    def __init__(self):
        self.loginUrl = 'http://218.94.104.201:85/default6.aspx'
        self.cookies = cookielib.CookieJar()
        self.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.76 Safari/537.36'
        self.headers = {'User-Agent': self.user_agent}
        page = urllib2.urlopen(self.loginUrl).read()
        self.postdata = urllib.urlencode({
            '__VIEWSTATE': 'dDwtMTQxNDAwNjgwODt0PDtsPGk8MD47PjtsPHQ8O2w8aTwyMT47aTwyMz47aTwyNT47aTwyNz47PjtsPHQ8cDxsPGlubmVyaHRtbDs + O2w8Oz4 + Ozs + O3Q8cDxsPGlubmVyaHRtbDs + O2w8Oz4 + Ozs + O3Q8cDxsPGlubmVyaHRtbDs + O2w8Oz4 + Ozs + O3Q8cDxsPGlubmVyaHRtbDs + O2w8Oz4 + Ozs + Oz4 + Oz4 + Oz59envE1UwQehRVvzVOfsZyW7fzvQ ==',
            'txtYhm':'12014052014',
            'txtMm':'wang951012',
            'rblJs': '学生',
            'btnDl': '登录'
        })
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))

    def getPage(self):
        request = urllib2.Request(
            url = self.loginUrl,
            data= self.postdata,
            headers= self.headers
        )
        result = self.opener.open(request)

        print result.read().decode('gbk')

sjxy = SJXY()
sjxy.getPage()