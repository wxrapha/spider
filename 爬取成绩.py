# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/6/20 下午2:37'


import urllib
import urllib2
import re
import cookielib



def getVIEW(Page):
    view = r'name="__VIEWSTATE" value="(.+)" '
    view = re.compile(view)
    return view.findall(Page)[0]

def Print(Score_html):
    str = r"<td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.?)</td><td>(.*)</td><td>(.*)</td><td>(.*)</td><td>(.?)</td><td>(.?)</td>"
    str = re.compile(str)
    result = {}
    subject = []
    a = str.findall(Score_html)
    for i in a:
        for j in range(15):
            subject.append(i[j])
        result[subject[3]] = subject
        subject = []

    for i in result.keys():
        j = result[i]
        print '%-10s%-2s%-10s%-8s%6s%8s%10s%6s%6s%5s%10s%-10s%-15s%s%s' % tuple(j)
        print " "


def main():
    loginUrl = 'http://218.94.104.201:85/default6.aspx'
    cookies = cookielib.CookieJar()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.76 Safari/537.36'
    headers = {'User-Agent': user_agent}
    page = urllib2.urlopen(loginUrl).read()
    postdata = urllib.urlencode({
        '__VIEWSTATE': getVIEW(page),
        'txtYhm':'账号',
        'txtMm':'密码',
        'rblJs': '学生',
        'btnDl': '登录'
    })
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))

    request = urllib2.Request(
        url = loginUrl,
        data= postdata,
        headers= headers
    )
    myRequest = urllib2.Request(loginUrl, postdata, headers)
    loginPage = opener.open(myRequest).read()
    page = unicode(loginPage, 'gb2312').encode("utf-8")

    for i in cookies:
        Cookie1 = i.name + "=" + i.value

    head = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Cookie':'ASP.NET_SessionId=njrz02aebwnd0tjqmftkboil',
    'Host':'218.94.104.201:85',
    'Referer':'http://218.94.104.201:85/xscj.aspx?xh=12014052014&xm=%CD%F5%D4%CF%D6%C2&gnmkdm=N121605',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    getdata = urllib.urlencode({
        'xh':'账号',
        'xm':'名字',
        'gnmkdm': 'N121605'
    })
    MyRequest = urllib2.Request('http://222.24.19.201/xscjcx.aspx?' + getdata, None, head)
    loginPage = unicode(opener.open(MyRequest).read(), 'gb2312').encode("utf-8")
    data = urllib.urlencode({
        "__VIEWSTATE": getVIEW(loginPage),
        'Button2': '在校学习成绩查询'
    })
    MyRequest = urllib2.Request('http://222.24.19.201/xscjcx.aspx?' + getdata, data, head)  # Score's page
    html = opener.open(MyRequest)
    result = unicode(html.read(), 'gb2312').encode("utf-8")

    print result

if __name__ == '__main__':
    main()
