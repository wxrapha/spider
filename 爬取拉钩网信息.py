# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/6/28 下午2:04'


from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re


page = 1
neirong = []
url = 'https://www.lagou.com/'
#自动打开浏览器
browser = webdriver.Chrome()
#自动登陆设置的URL地址
browser.get(url)
#设置睡眠时间
time.sleep(2)
#模拟点击
browser.find_element_by_link_text('全国站').click()
time.sleep(1)
#模拟输入搜索框文本
browser.find_element_by_id('search_input').send_keys(u'爬虫')
time.sleep(1)
#模拟点击搜索
browser.find_element_by_id('search_button').click()
#获得页面代码
getpage = browser.page_source
#创建Beautifulsoup对象
soup = BeautifulSoup(getpage, 'lxml')
#查找所需要的信息
pay = soup.find_all("span", class_="money")
releasetime = soup.find_all("span", class_="format-time")
industry = soup.find_all("div", class_="industry")
synopsis = soup.find_all("div", class_="li_b_r")
jobs = soup.find_all(['h2', 'em'])
name = soup.find_all(attrs={"data-lg-tj-id": "8F00"})
yaoqiu = soup.find_all("div", class_="p_bot")
for a, b, c, d, e in zip(name, jobs, pay, synopsis, releasetime):
    print u'公司名:'+a.string, u'      工作地点:'+b.string, u'      薪资:'+c.string, u'      简介:'+d.string, u'      '+e.string
