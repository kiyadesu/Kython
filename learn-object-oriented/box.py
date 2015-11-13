class SideNum(object):

    def __init__(self,default = 1):
        self.default = default

    def __get__(self,instance,owner):
        return self.default

    def __set__(self, instance, val):
        if 1 <= val <= 6:
            self.default = val
        else:
            print('must between 1 and 6')

    def __delete__(self,instance):
        pass

class Box(object):
    instance_num = 0
    sideNum = SideNum()
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.__volumn = 0
        self._color = 'orange'
        self.__openFlag = False
        Box.instance_num += 1

    def info(self):
        print 'length:%d width:%d height:%d >> ' %(self.length,self.width,self.height),
        print 'volumn: %d' % self.getVolumn()

    def getVolumn(self):
        self.__volumn = self.length * self.width * self.height
        return self.__volumn

    def __call__(self):
        return self.getVolumn()

    def setColor(self,color):
        self._color = color

    def getColor(self):
        return self._color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,value):
        self._color = value

    def open(self):
        if self.__openFlag:
            print('you\'ve already opened the box!!!!')
        else:
            print('box open!')
            self.__openFlag = True

    def close(self):
        if not self.__openFlag:
            print('you\'ve already closed the box!!!!')
        else:
            print('box close!')
            self.__openFlag = False

class BoxLevel2(Box):

     def __add__(self, ab):
         return BoxLevel2(self.length+ab.length, self.width+ab.width, self.height+ab.height)

    #  def info(self):
    #      print 'length:%d width:%d height:%d >> ' %(self.length,self.width,self.height),
    #      print 'volumn: %d' % self.getVolumn()

def AddIns(b1,b2):
    return b1+b2

if __name__ == '__main__':
    b1 = BoxLevel2(1,1,1)
    b2 = BoxLevel2(2,2,2)
    b1.info()
    b2.info()
    AddIns(b1,b2).info()


# print Box.instance_num
# b = Box(1,1,1)
# print b.instance_num
# print b.getVolumn()
#
# b2 = Box(2,1,1)
# print b2.getVolumn()
# print Box.instance_num
# print b.instance_num
# Box.instance_num = 4
# print Box.instance_num
# b = Box(1,1,1)
# b.open()
# b.open()
# b.close()
# b.close()
# #print b.color
# b.color = 'blue'
# #print b.color
# b.sideNum = 7
# print(b.sideNum)
# print('as __call__:' + str(b()))
