# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/6/19 下午3:08'

import urllib2
import urllib
import re
import thread
import time


class QSBK:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        self.headers = { 'User-Agent' : self.user_agent }
        self.stories = []
        self.enable = False

    def getPage(self,pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            request = urllib2.Request(url, headers= self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError,e:
            if hasattr(e,'reason'):
                print u'链接糗事百科失败，错误原因：',e.reason
                return None

    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "页面加载失败。。。"
            return None
        pattern = re.compile(
            '<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?</div>.*?<i class="number">(.*?)</i>',
            re.S)
        items = re.findall(pattern,pageCode)
        pageStories = []
        for item in items:
            #haveImg = re.search("img", item[3])
            #if not haveImg:
             #   replaceBR = re.compile('<br/>')
              #  text = re.sub(replaceBR, "\n", item[1])
            pageStories.append([item[0].strip(),item[1].strip(),item[2].strip()])
        return pageStories

    def loadPge(self):
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1

    def getOneStory(self,pageStories,page):
        for story in pageStories:
            input = raw_input()
            self.loadPge()
            if input == 'Q':
                self.enable =False
                return
            print (u"'第{}页\t发布人:{}\t赞:{}\t{}'".format(page,story[0],story[2],story[1]))

    def start(self):
        print u"正在读取糗事百科,按回车查看新段子，Q退出"
        self.enable = True
        self.loadPge()
        nowpage = 0
        while self.enable:
            if len(self.stories)>0:
                pageStories = self.stories[0]
                nowpage += 1
                del self.stories[0]
                self.getOneStory(pageStories,nowpage)

spider = QSBK()
spider.start()

