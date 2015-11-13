class NonNegative():

    def __init__(self,default=0):
        self.default = default

    def __get__(self,instance,owner):
        return self.default

    def __set__(self,instance,val):
        if val > 0 :
            self.default = val
        else:
            print('value must >= 0')

    def __delete__(self, instance):
        pass

class Movie(object):
    score = NonNegative()
    rate = NonNegative()

if __name__ == '__main__':
    m = Movie()
    print(m.score)
    m.score = 99
    print(m.score)
    m.rate = -1
    print(m.rate)
