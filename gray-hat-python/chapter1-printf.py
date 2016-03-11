#!/usr/bin/env python
#coding:utf-8
from ctypes import *
libc = CDLL("libc.so.6")    //CDLL -> 加载遵循cdecl标准函数调用约定的链接库

message_string = ""
libc.scanf("%s",message_string);
libc.printf("Hello %s\n", message_string)
