from box import AddIns

class Cup(object):

    def __init__(self, capacity=10):
        self.capacity = capacity

    def __add__(self,c):
        return Cup(self.capacity + c.capacity)

    def info(self):
        print 'capacity: %s' % self.capacity

    def water(self):
        print 'water no param'

    # def water(self,ml): # no polymorphism
    #     print 'water %s' % ml

c1 = Cup()
c1.info()
c1.water()
# c1.water(1)
c2 = Cup(3)
c2.info()
AddIns(c1,c2).info()
