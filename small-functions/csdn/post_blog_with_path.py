#!/usr/bin/env python
#encoding:utf-8
import os
import time

def traverse(rootDir):
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for f in files:
            path = os.path.join(root, f)
            if os.path.getmtime(path) > 1449214271 or os.path.getmtime(path) < 1449212309:
                print '>>' + path
                os.system('./post_blog.py ' + path),


if __name__ == '__main__':
    traverse('/home/hanks/kiya/blog/source/_posts')
