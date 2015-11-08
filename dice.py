import random

class Dice(object):

    sides = ['red','orange','yellow','green','cray','blue']

    def __init__(self,num):
        self.color = self.sides[num]
        print self.color

    @staticmethod
    def calcSum(color1,color2):
        return Dice.sides.index(color1) + Dice.sides.index(color2) + 2

    @classmethod
    def get_dice(cls):
        return cls(random.randint(0,6))

if __name__ == '__main__':
    d1 = Dice.get_dice()
    d2 = Dice.get_dice()
    print Dice.calcSum(d1.color,d2.color)
