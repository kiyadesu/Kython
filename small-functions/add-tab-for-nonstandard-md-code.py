#!/usr/bin/env python
#encoding:utf-8
import os
import time

def add_tab(path):
    with open(path,'r') as f:
        flag = False
        data = ''
        tmp = '111'
        count = 0
        while tmp != '':
            tmp = f.readline()

            if tmp == '```\n':
                if flag:
                    flag = False
                else:
                    flag = True
                data += tmp
                continue

            if flag:
                if tmp != '\n':
                    data += '    ' + tmp
                    # data += tmp[4:]
                    count += 1
            else:
                data += tmp

    with open(path,'w') as f:
        f.write(data)

    return count

def traverse(rootDir):
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for d in dirs:
            print os.path.join(root, d)
        for f in files:
            path = os.path.join(root, f)
            if os.path.getmtime(path) > 1449214271 or os.path.getmtime(path) < 1449212309:
                print '>>' + path + '\n  modified ',
                print add_tab(path),
                print 'lines'

if __name__ == '__main__':
    # traverse('/home/hanks/kiya/blog/source/_posts')
    add_tab('/home/hanks/kiya/blog/source/_posts/ida-dynamic-debug-so.md')
