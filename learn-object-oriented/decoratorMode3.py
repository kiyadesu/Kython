def decorate(cls):
    class WrappedClass(object):

        def __init__(self, age, name):
            self.name = name
            self._realIns = cls(age)

        def info(self):
            print  self.name
            self._realIns.info()
            # print self.__realIns.age

    return WrappedClass

@decorate
class doge(object):

    def __init__(self, age):
        self.age = age

    def info(self):
        print self.age

if __name__ == '__main__':
    d = doge(2,'wangwang')
    d.info()
