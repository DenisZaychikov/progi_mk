def even_nums(n):
    i = 0
    while i < n:
        i += 2
        yield i


for i in even_nums(100):
    print(i)
