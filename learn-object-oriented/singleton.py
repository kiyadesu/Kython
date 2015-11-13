class Single(object):
    def __init__(self, val=0):
        self.val = 0

s = Single()

def test():
    print s.val
    s.val = 10
    print s.val
    print '---------'

def test2():
    print s.val
    s.val = 233
    print s.val


if __name__ == '__main__':
    test()
    test2()
