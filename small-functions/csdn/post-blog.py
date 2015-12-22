#!/usr/bin/env python
#coding:utf-8
import urllib
import urllib2
import cookielib
from bs4 import BeautifulSoup
#a file stord your username & password
from pass_csdn import username,password

cookie = cookielib.MozillaCookieJar('cookie.txt')
cookie_handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(cookie_handler)

def login():
    # prepare for login
    response = opener.open('https://passport.csdn.net/account/login')
    lt = ""
    execution = ""
    bs = BeautifulSoup(response.read(),"lxml")
    for input in bs.form.find_all('input'):
        if input.get('name') == 'lt':
            lt = input.get('value')
        if input.get('name') == 'execution':
            execution = input.get('value')

#---------------------------------------------------

    post_data = urllib.urlencode({
        'username' : username,
        'password' : password,
        'lt' : lt,
        'execution' : execution,
        '_eventId' : 'submit'
    })

    headers_data = {
        'User-Agent' :	'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0'
    }

    login_url_with_jsession = 'https://passport.csdn.net/account/login'
    request = urllib2.Request(url = login_url_with_jsession,data=post_data)
    try:
        response = opener.open(request)
        cookie.save()
    except urllib2.HTTPError as e:
        print e.read()

if __name__ == '__main__':
    login()
