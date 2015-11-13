#coding:utf-8

class Moveable(object):
    def move(self):
        print 'move slowly.'

class MoveInCar(Moveable):  # 继承了Moveable
    def move(self):
        print 'move in car.'

class MoveOnFoot(object):   #没有继承Moveable
    def move(self):
        print 'move one bye one.'

class MoveObj(object):
    def set_move_way(self, cls):
        self.__move_way = cls() #实例

    def move(self):
        self.__move_way.move()

if __name__ == '__main__':
    m = MoveObj()
    m.set_move_way(Moveable)
    m.move()
    m.set_move_way(MoveInCar)
    m.move()
    m.set_move_way(MoveOnFoot)
    m.move()
