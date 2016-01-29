# -*- coding: utf-8 -*-
import requests
import json
import os

class dataRequest:
    #请求列表,并打印每条新闻
    def listRequest(self):
        baseUrl = 'http://newsapi.eastmoney.com/kuaixun/v2/api/yw'
        page = 1  #请求的页数
        limit = page*20  #请求的条数
        params = {'encode':'ywjh','source':'app','sys':'ios','version':'6000'}
        params['limit'] = limit
        response = requests.get(url=baseUrl,params=params)
        listJson = json.loads(response.text)
        for i in range(limit):  #打印每条新闻
            print listJson['news'][i]['id']
            print listJson['news'][i]['newsid']
            print listJson['news'][i]['simtitle']
            print listJson['news'][i]['newstype']
            print listJson['news'][i]['commentnum']
            print
        return listJson

    #请求正文，返回news body节点里的内容
    def contentRequest(self,newsid):
        baseUrl= 'http://newsapi.eastmoney.com/kuaixun/v2/api/content'
        params = {'newstype':'1','source':'app','sys':'ios','version':'6000'}
        params['newsid']=newsid
        response = requests.get(url=baseUrl,params=params).text
        contentJson = json.loads(response)
        body = contentJson['news']['body']
        return body
    #列表元素
    def parseList(self,listRequest):
        pass

#a = dataRequest()
#a.listRequest()
'''
contentData = a.contentRequest(newsid='20160127589986793').text
contentJson = json.loads(contentData)
body = contentJson['news']['body']
print contentData
print type(contentData)
print body
'''


'''
1.取最新5页,共100条新闻,请求5次.
2.每次列表请求,生成20个id的news.
3.每个news取newsid,正文.
'''

class news:
    def news(self):
        data = dataRequest()
        listData = data.listRequest().text
        s = json.loads(listData)
        id = s['news'][0]['id']
        newsid = s['news'][0]['newsid']
        newsType = s['news'][0]['newstype']
        simtitle = s['news'][0]['simtitle']
        newNumber = len(s['news'])   #新闻数量
        print 'newsid\'s type:',type(newsid)
        print 'newsid = ',newsid
        print type(s['news'])  #每条新闻组合是一个list
        print 'newsNumber:%d'%newNumber
        pass







