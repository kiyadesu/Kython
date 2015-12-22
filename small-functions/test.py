# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time
import os
from bs4 import BeautifulSoup as bs
from cookielib import LWPCookieJar


def toJson(str):
    '''
    提取lt流水号，将数据化为一个字典
    '''
    soup = bs(str)
    tt = {}
    for inp in soup.form.find_all('input'):
        if inp.get('name') != None:
            tt[inp.get('name')] =inp.get('value')
    return tt


s = requests.Session()
s.cookies = LWPCookieJar('cookiejar')
header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0'}

r = s.get("http://passport.csdn.net/account/login")
soup = toJson(r.text)
payload ={'username':'2267161320@qq.com','password':'handk1314','lt':soup["lt"],'execution':soup["execution"],'_eventId':'submit'}

print payload
r = s.post("http://passport.csdn.net/account/login",data=payload,headers=header)

print r.text


# r = s.get("https://passport.csdn.net/content/loginbox/loginapi.js")
r = s.get("http://write.blog.csdn.net/postlist",headers=header)
print r.text
