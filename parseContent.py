# -*- coding: utf-8 -*-
from a import dataRequest
from bs4 import BeautifulSoup

#body = dataRequest().contentRequest(newsid='20160127589986793')
#print body
#print type(body)

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html,"html.parser")
print soup.prettify()
print type(soup.prettify())
'''
print soup.title
print type(soup.title)
print soup.title.name
print soup.title.attrs
'''
#获取标签值
#print soup.p['class']
#print soup.p.get('class')
#删除标签
#del soup.p['class']
#print soup.p
#获取标签内的文字
#print soup.p.string
#print type(soup.p.string)
#处理comment
#print soup.a
#print soup.a.string
#print type(soup.a.string)
'''
if type(soup.a.string)==bs4.element.Comment:
    print soup.a.string
'''
#直接访问子节点

#print soup.head.contents[0]
#遍历子节点
'''
print soup.body.children
for child in soup.body.children:
    print child
'''
#所有子孙内容
'''
for child in soup.body.descendants:
    print child
'''
#多个内容
