from time import time


def timer(func):
    def wrapped(x):
        new_time = time()

        func(x)

        new_time1 = time()

        return new_time1 - new_time

    return wrapped


@timer
def square(x):
    return x * x


print(square(2))
