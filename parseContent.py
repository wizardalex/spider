# -*- coding: utf-8 -*-
from a import dataRequest
import BeautifulSoup

body = dataRequest().contentRequest(newsid='20160127589986793')
print body
print type(body)