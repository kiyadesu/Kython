class SingleClass(object):

     def __new__(cls, *args, **kw):
         if not hasattr(cls, '__ins'):
             cls.__ins = super(SingleClass, cls).__new__(cls, *args, **kw)
         return cls.__ins

if __name__ == '__main__':
    s1 = SingleClass()
    print hex(id(s1))
    s2 = SingleClass()
    print hex(id(s2))

# why aren't they the same value
# 0x7f340252de50
# 0x7f340252de90
