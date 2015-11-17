from ctypes import *

class barley_amount(Union):
    _fields_ = [
        ("barley_long", c_long),
        ("barley_int", c_int),
        ("barley_char", c_char * 8),
    ]

print type(barley_amount)

value = raw_input("a number:")
my_barley = barley_amount(int(value))

#print dir(my_barley)

print "as a long: %ld" % my_barley.barley_long
print 'as an int: %d' % my_barley.barley_int
print "as a char: %s" % my_barley.barley_char
