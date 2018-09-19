from time import time


def timer(func):
    def wrapped(x):
        new_time = time()
        func(x)
        return time() - new_time

    return wrapped


@timer
def square(x):
    return x * x


print(square(2))
