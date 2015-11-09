#coding:utf-8
import random

class Dice(object):

    sides = ['red','orange','yellow','green','cray','blue']

    def __init__(self,num=1,iterend=6):
        print 'init > num:%s | iterend:%s' % (num,iterend)
        self.color = self.sides[num]
        self.iterend = iterend
        print 'init > color: ',self.color

    @staticmethod
    def calcSum(color1,color2):
        return Dice.sides.index(color1) + Dice.sides.index(color2) + 2

    @classmethod
    def get_dice(cls):
        return cls(num=random.randint(0,5)) # randint(a,b) : a <= x <= b

    def __iter__(self):
        self.count = 0
        return self

    def next(self):#shit! in python3, the func name here should be __next__
        if self.count < self.iterend:
            self.count += 1
            self.color = self.sides[random.randint(0,5)]
            return self.color
        else:
            raise StopIteration

if __name__ == '__main__':
    d1 = Dice.get_dice()
    d2 = Dice.get_dice()
    print Dice.calcSum(d1.color,d2.color)
    print '——————iter——cut——————'
    for i in Dice(iterend=6):
        print i
