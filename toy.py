# -*- coding: utf-8 -*-

import requests

url = 'http://apis.baidu.com/apistore/mobilenumber/mobilenumber'
payload = {"phone":"15802137109"}
headers = {"apikey":"4bc4576897aef37459145efe5d19c4b8"}

r = requests.get(url=url, params=payload, headers=headers)
#r.encoding = 'utf-8'

print r.text.decode('unicode_escape')
print
