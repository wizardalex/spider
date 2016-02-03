#coding: utf-8
"""
项目地址： https://github.com/zhaowz/huaban_crawler
下载花瓣网某子网址下num张图片
homeUrl = "http://huaban.com/explore/banmiansheji/"
num = 200
"""
import urllib,os,requests,json,re,datetime
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
from lxml import etree

class huabanCrawler():
    def __init__(self):
        self.imgs=[]       #每张图片的id,url
        self.homeUrl="http://huaban.com/favorite/beauty/"     #花瓣首页
        self.times=[]
    def load_homePage(self):
        response = requests.get(url=self.homeUrl).content
        #print response
        return response
    def extrac_img_url(self):
        '''
        soup = BeautifulSoup(self.load_homePage(),'html.parser')
        #print soup.prettify()
        #content = soup.find_all(name='a',attrs={'class':'img x layer-view loaded'})
        print soup.body.contents[8]
        '''
        d = pq(self.load_homePage())
        d1 = d('body').find('div').eq(0)
        print d1('div')
        print d('.pin wfc wft')
        pass


a = huabanCrawler().extrac_img_url()



'''
img x layer-view loaded
'''