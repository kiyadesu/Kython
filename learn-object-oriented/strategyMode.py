#coding:utf-8

class Moveable(object):
    def move(self):
        print 'move slowly.'

class MoveInCar(Moveable):  # 继承了Moveable
    def move(self):
        print 'move in car.'

class MoveOnFoot(object):   #没有继承Moveable,只要实现了move方法可以调用就可以了，所以没有接口
    def move(self):
        print 'move one bye one.'

#----------------------------------------------------

def movea():
    print 'move aa'

def moveb():
    print 'move bb'

#----------------------------------------------------

class MoveObj(object):
    def set_move_way(self, method):    # set_move_way 导致了本类 move方法可以动态改变
        # self.__move_way = cls() #类作参数
        self.__move_way = method    #函数作参数
    def move(self):
        # self.__move_way.move()
        self.__move_way()

if __name__ == '__main__':
    m = MoveObj()
    # m.set_move_way(Moveable)
    # m.move()
    # m.set_move_way(MoveInCar)
    # m.move()
    # m.set_move_way(MoveOnFoot)
    # m.move()

    m.set_move_way(movea)
    m.move()
    m.set_move_way(moveb)
    m.move()
