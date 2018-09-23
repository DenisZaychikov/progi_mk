class First(object):
    pass


class Second(object):
    pass


class Parent(object):
    pass


class MyError(Exception):
    pass


class A(First, Parent):

    def __init__(self):
        self.i = 3
        self.isSecond = 0

    def __setattr__(self, attr, value):
        if attr == 'isSecond' and value != 0:
            raise AttributeError
        else:
            self.__dict__[attr] = value

    def fnc(self, x):
        if x == 7:
            raise MyError('Error text')
        return x * 2 * 3

    def isFirst(self):
        return True


class B(Second, Parent):
    def __init__(self, i):
        self.i = i
        self.isSecond = 1

    def fnc(self, x, y):
        return x * y * 5

    def isFirst(self):
        return False
