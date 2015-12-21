#coding:utf-8
import webbrowser
import threading
from sys import exit

def updateKX():

        webbrowser.open('http://bbs.pediy.com',new=0)
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
    i = 0
    t = threading.Timer(300.0, updateKX)
    t.start()
