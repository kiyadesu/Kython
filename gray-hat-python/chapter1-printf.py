from ctypes import *
libc = CDLL("libc.so.6")
message_string = "Hello world!\n"
libc.printf("test: %s", message_string)
