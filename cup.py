from box import AddIns

class Cup(object):

    def __init__(self, capacity=10):
        self.capacity = capacity

    def __add__(self,c):
        return Cup(self.capacity + c.capacity)

    def info(self):
        print 'capacity: %s' % self.capacity

c1 = Cup()
c1.info()
c2 = Cup(3)
c2.info()
AddIns(c1,c2).info()
