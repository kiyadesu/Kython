#!/usr/bin/env python
#coding:utf-8

import urllib
import urllib2
import cookielib
from login_helper import getvalue

cookie = cookielib.MozillaCookieJar('cookie.txt')
cookie_handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(cookie_handler)


def login():

    # prepare for login
    response = opener.open('https://passport.csdn.net/account/login')
    data = response.read()
    #lt,execution
    lt,execution = getvalue(data)
    #cookie jsessionid
    for c in cookie:
        print c.name,c.value
        if c.name == 'JSESSIONID':
            jsessionid = c.value
            break
    cookie.save(ignore_discard=True,ignore_expires=True)

#---------------------------------------------------

    post_data = urllib.urlencode({
        'username' : '1143123897@qq.com',
        'password' : 'han15903067415',
        'lt' : lt,
        'execution' : execution,
        '_eventId' : 'submit'
    })

    login_url_with_jsession = 'https://passport.csdn.net/account/login;jsessionid=' + jsessionid
    request = urllib2.Request(url = login_url_with_jsession,data=post_data)
    try:
        response = opener.open(request)
    except urllib2.HTTPError as e:
        print e.read()

    print response.info()

    try:
#        ret = opener.open('http://write.blog.csdn.net/article/UploadImgMarkdown?parenthost=write.blog.csdn.net')
        ret = opener.open('http://blog.csdn.net/attach_114')
        print ret.read()
        print ret.geturl()
    except urllib2.HTTPError as e:
        print e.read()

if __name__ == '__main__':
    login()
