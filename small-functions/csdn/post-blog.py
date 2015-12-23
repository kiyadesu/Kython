#!/usr/bin/env python
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import urllib
import markdown

from CSDN import CSDN
from pass_csdn import username,password #a file stored your username & password

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'usage: %s <article file path>' % sys.argv[0][sys.argv[0].rfind('/')+1:]
        print " before execute, touch 'pass_csdn.py' in the same folder as me and put username& password in it"
        exit(0)
    print '————CSDN-START————'
    csdn = CSDN()
    csdn.login(username,password)
    csdn.publish_article(sys.argv[1])
    print '————CSDN-END————'
