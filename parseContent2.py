# -*- coding: utf-8 -*-
from a import dataRequest
from bs4 import BeautifulSoup

body = dataRequest().contentRequest(newsid='20160127589986793')

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
soup = BeautifulSoup(html,'html.parser')
print soup.prettify()
print type(soup.p)
#print type(soup.p)
#soup = repr(soup)

#print soup.p
#print soup.find_all('p')

'''
p中有带br
<!-- EM_StockImg_Start --> p <!-- EM_StockImg_End -->
<p>
span
 <!--Link#1-->
</p>
'''
