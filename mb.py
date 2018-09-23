class Second(object):
    pass


class Parent(object):
    pass


class B(Second, Parent):
    def __init__(self, i):
        self.i = i
        self.isSecond = 1

    def fnc(self, x, y):
        return x * y * 5

    def isFirst(self):
        return False
