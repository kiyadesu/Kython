#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import urllib
import urllib2
import cookielib
from Tools import format_file,parse_html
import os.path

class CSDN:

    def __init__(self):
        self.cookie = cookielib.MozillaCookieJar('cookie.txt')
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        self.login_url = 'https://passport.csdn.net/account/login'
        self.publish_article_url = 'http://write.blog.csdn.net/mdeditor/setArticle'


    # GET or POST
    def RequestInOne(self,req_url,post_data=None):
        headers_data = {
            'User-Agent' :	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36'
        }

        request = urllib2.Request(url=req_url,data=post_data,headers=headers_data)
        try:
            return self.opener.open(request)
        except urllib2.HTTPError as e:
            print e.read()


    def login(self,username,password):

        print '| start loging in'
        # prepare for login
        lt, execution = parse_html(self.RequestInOne(self.login_url).read())
        post_data = urllib.urlencode({
            'username' : username,
            'password' : password,
            'lt' : lt,
            'execution' : execution,
            '_eventId' : 'submit'
        })
        response = self.RequestInOne(req_url=self.login_url,post_data=post_data)
        if response.read().find('该参数可以理解成') != -1:
            print '| login failed'
            return False

        return True

    def publish_article(self,article_path):
        title,content,markdowncontent = format_file(article_path)
        print '| start publishing:' + title
        post_data = urllib.urlencode({
            'title' : title,
            'markdowncontent' : content,
            'content' : markdowncontent,
            'id' : '',
            'tags' : '',
            'description' : content[:100],
            'status' : '0',
            'level' : '0',
            'categories' : '',
            'channel' :	'1',
            'type' : 'original',
            'articleedittype' :	'1'
        })

        response = self.RequestInOne(req_url=self.publish_article_url,post_data=post_data)
        print '| return :' + response.read()[:-2]
