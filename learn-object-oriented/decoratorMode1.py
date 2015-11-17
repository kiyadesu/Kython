class Water(object):

    def __init__(self):
        self.name = 'water'

    def info(self):
        print self.name

class Decorator(object):    # what use???? no necessary(可能是为了避免子类们没有实现Info方法从而调用出错)

    def info(self):
    #    print "i'm Decorator"
        print self.name

class Apple(Decorator):

    def __init__(self,ins):
        self.name = 'Apple'
        self.__ins = ins

    def info(self):
        print self.name,
        print self.__ins.name


class Orange(Decorator):

    def __init__(self,ins):     # 传实例名
        self.name = 'Orange'
        self.__ins = ins

    def info(self):
        print self.name,
        print self.__ins.name

if __name__ == '__main__':
    wate = Water()

    appl = Apple(wate)
    appl.info()

    oran = Orange(wate)
    oran.info()
