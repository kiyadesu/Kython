#coding:utf-8

# import pdb
#
# pdb.set_trace()

class SingleClass(object):

     def __new__(cls, *args, **kw):
         if not hasattr(cls, '_ns'):   # hasattr 不是类的方法，所以总是访问不到 __ns 成员
             cls._ns = super(SingleClass, cls).__new__(cls, *args, **kw)
             print cls._SingleClass__ns
         return cls._ns

if __name__ == '__main__':
    s1 = SingleClass()
    print hex(id(s1))
    s2 = SingleClass()
    print hex(id(s2))

# why aren't they the same value
# 0x7f340252de50
# 0x7f340252de90
