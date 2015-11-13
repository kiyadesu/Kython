class c1(object):
    pass

class c2(object):
    pass

class Factory(object):

    def get_instance(self,cls):
        return cls()

if __name__ == '__main__':
    fact = Factory()
    print fact.get_instance(c1)
    print fact.get_instance(c2)
