#coding:utf-8
class MyMeta(type):

    def __init__(self,name,bases,dicts):
        print 'init instance.'

    def __new__(cls,name,bases,dicts):
        dicts['info'] = 'hello' #why 'lambda self: print 'hello'' is not OK?
        ins = type.__new__(cls,name,bases,dicts)
        ins.company = 'hankiya'
        return ins

class Custom(): # python3: metaclass=MyMeta
    __metaclass__ = MyMeta
    pass

if __name__ == '__main__':
    c = Custom()
    print c.company
    print c.info
    print type(Custom)
