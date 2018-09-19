from time import time


def timer(f):
    def wrapped():
        new_time = time()
        return f() - new_time

    return wrapped


@timer
def func():
    start = time()
    return start


print(func())
