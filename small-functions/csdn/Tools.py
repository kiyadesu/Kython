#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import urllib
from bs4 import BeautifulSoup
import markdown

# get lt,execution
def parse_html(data):
    bs = BeautifulSoup(data,"lxml")
    for input in bs.form.find_all('input'):
        if input.get('name') == 'lt':
            lt = input.get('value')
        if input.get('name') == 'execution':
            execution = input.get('value')
    return lt,execution

## cause i write blog with hexo...
def format_file(path):
    data = ''
    with open(path) as f:
        title = f.readline()[7:-1]
        data = f.read()

    content = data[data.find('---')+4 : ]  # 去掉hexo前面几行属性
    markdowncontent = markdown.markdown(content,extensions = ['markdown.extensions.fenced_code', 'markdown.extensions.codehilite'])
    return title,content,markdowncontent

if __name__ == '__main__':
    with open('/home/hanks/kiya/blog/source/_posts/csdn-login.md') as f:
        data = f.read()
    # print data
    content = r'''
        cookie = cookielib.MozillaCookieJar('cookie.txt')   # MozillaCookieJar可保存cookie
        cookie_handler = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(cookie_handler)
        # prepare for login
        response = opener.open('https://passport.csdn.net/account/login')
        data = response.read()
        lt = ""
        execution = ""
        bs = BeautifulSoup(response.read(),"lxml")
        for input in bs.form.find_all('input'):
            if input.get('name') == 'lt':
                lt = input.get('value')
            if input.get('name') == 'execution':
                execution = input.get('value')
    '''

    # print markdown.markdown(content)

    from pygments import highlight
    from pygments.lexers import get_lexer_by_name
    from pygments.formatters import HtmlFormatter

    lexer = get_lexer_by_name("python", stripall=True)
    formatter = HtmlFormatter(linenos=True, cssclass="source")
    print  highlight(content, lexer, formatter)
    # print highlight(content, PythonLexer(), HtmlFormatter())
