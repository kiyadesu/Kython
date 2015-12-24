#!/usr/bin/env python
#encoding:utf-8
import os
import time

def traverse(rootDir):
    count = 0
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for f in files:
            path = os.path.join(root, f)
            if count > 9:   # 达到十次csdn就会限制登录了
                time.sleep(60)
            print '>>' + path
            count += 1
            os.system('./post_blog.py ' + path),

if __name__ == '__main__':
    print '********start********'
    traverse('/home/hanks/kiya/blog/source/_posts')
