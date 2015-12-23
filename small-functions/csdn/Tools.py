#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import markdown2
import markdown
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
        # 正常情况直接 f.read 就可以,这里是因为字节写markdown格式不规范造成的（哭
        # tmp = f.readline()
        # while tmp != '':
        #     tmp = f.readline()
        #     if len(tmp) > 20:
        #         data += tmp[:-1] + '<br/>' + '\n'
        #     else:
        #         data += tmp
        data = f.read()

    content = data[data.find('---')+4 : ]  # 去掉hexo前面几行属性
    # title = urllib.quote(title)
    markdowncontent = markdown2.markdown(content)
    return title,content,markdowncontent

if __name__ == '__main__':
    s = '''

测试程序:

```
    #include<stdio.h>
    #include<stdlib.h>
    #include<sys/ptrace.h>
    int main(int argc, char* argv[])
    {
        ptrace(PTRACE_TRACEME);
        while(1){
            printf("Hello Ptrace!\n");
            sleep(1);
        }
        return 0;
    }
```

编译:`gcc -g -o hello-ptrace hello-ptrace.c`

    '''

    print markdown.markdown(s)
