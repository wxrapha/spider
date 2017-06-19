import urllib2
import cookielib

cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open('http://www.baidu.com')
print cookie
for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value

filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)

cookie = cookielib.MozillaCookieJar()
cookie.load('cookie.txt',ignore_expires=True,ignore_discard=True)
req = urllib2.Request('http://www.baidu.com')
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()