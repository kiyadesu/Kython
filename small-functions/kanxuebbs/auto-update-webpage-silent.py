#!/usr/bin/env python
#coding:utf-8

import urllib
import urllib2
import cookielib
import threading
from sys import exit

import pass_kx  # a python file stored post_data used below(get this from capturing data when loging in)

def login():
    '''
    post data to the login page and save cookie
    '''
    log_url = 'http://bbs.pediy.com/login.php?do=login'

    cookie_filename = 'cookie.txt'
    cookie = cookielib.MozillaCookieJar(cookie_filename)
    cookie_handler = urllib2.HTTPCookieProcessor(cookie)

    post_data = urllib.urlencode({
        'vb_login_username' : pass_kx.vb_login_username,
        'vb_login_password' : pass_kx.vb_login_password,
        's' : pass_kx.s,
        'securitytoken' : pass_kx.securitytoken,
        'do' : pass_kx.do,
        'vb_login_md5password' : pass_kx.vb_login_md5password,
        'vb_login_md5password_utf' : pass_kx.vb_login_md5password_utf
    })

    opener = urllib2.build_opener(cookie_handler)

    request = urllib2.Request(url = log_url,data=post_data)
    response = opener.open(request)
    cookie.save(ignore_discard=True,ignore_expires=True)

    #print opener.open('http://bbs.pediy.com/member.php?u=663974').read()


def updateKX():
    '''
    open a page every 5min
    '''
    global opener
    ret = opener.open('http://bbs.pediy.com').read()
    print ret.find('kiya')

    global t        #Notice: use global variable!
    t = threading.Timer(300.0, updateKX)
    t.start()

    global i
    i += 1
    print i
    if i > 15:
        print 'exit'
        t.cancel()


if __name__ == '__main__':
    login()     #login and save cookie

    # load saved cookie to open another page
    cookie = cookielib.MozillaCookieJar()
    cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

    i = 0
    t = threading.Timer(300.0, updateKX)
    t.start()
