#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import markdown2
import urllib
from bs4 import BeautifulSoup

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
    markdowncontent = markdown2.markdown(content)
    return title,content,markdowncontent
