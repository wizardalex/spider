# -*- coding: utf-8 -*-
'''
获取全国31省当天油价
所用的API来自  http://apistore.baidu.com/apiworks/servicedetail/710.html
apikey = '4bc4576897aef37459145efe5d19c4b8'
'''

import requests
from urllib import urlencode,quote
from bs4 import BeautifulSoup

class dataRequest:
    def __init__(self,prov):
        #self.apikey = '4bc4576897aef37459145efe5d19c4b8'
        self.prov = quote(prov)
    def oilPrice(self):
        baseUrl = 'http://apis.baidu.com/showapi_open_bus/oil_price/find'
        headers = {'apikey' : '4bc4576897aef37459145efe5d19c4b8'}
        params = self.prov
        response = requests.get(url=baseUrl,params = params,headers=headers)
        return response

#全国31省油价
price = dataRequest(prov='').oilPrice().text
print price

'''
soup = BeautifulSoup(price,'html.parser')
if (price):
    print soup.prettify()
'''