class Lab_Mouse(object):

    def edit(self):
        print "i'll be edited.\n"

    def keep(self):
        print "no one edit me."

class Decorator(object):

    def __init__(self, clsname):    # 传类名
        self.__ins = clsname()

    def edit(self):
        print "i'm the editor."
        self.__ins.edit()

    def keep(self):
        self.__ins.keep()

if __name__ == '__main__':

    m0 = Lab_Mouse()
    m0.edit()
    m0.keep()

    m1 = Decorator(Lab_Mouse)
    print type(m1)
    m1.edit()
    m1.keep()
