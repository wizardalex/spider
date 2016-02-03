# -*- coding: utf-8 -*-
from a import dataRequest
from pyquery import PyQuery as pq
from lxml import etree

body = dataRequest(page='1').contentRequest(newsid='20160202591903597')

fakeHead = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Fake Title</title>
<body>
"""

fakeTail = """
</body>
</head>
</html>
"""
html = fakeHead+body+fakeTail

d = pq(body)
print d('div').find('p').eq(1).text()