# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/6/28 下午2:04'


from selenium import webdriver
import time
import re
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get('https://www.lagou.com/')
time.sleep(2)
browser.find_element_by_link_text('全国站').click()
time.sleep(1)
browser.find_element_by_id('search_input').send_keys(u'爬虫')
time.sleep(1)
browser.find_element_by_id('search_button').click()
getpage = browser.page_source
soup = BeautifulSoup(getpage,'lxml')
pay = soup.find_all("span", class_="money")
releasetime = soup.find_all("span", class_="format-time")
industry = soup.find_all("div",class_="industry")
synopsis = soup.find_all("div", class_="li_b_r")
jobs = soup.find_all(['h2', 'em'])
name = soup.find_all(attrs={"data-lg-tj-id":"8F00"})
yaoqiu = soup.find_all("div",class_="p_bot")
