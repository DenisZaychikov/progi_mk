class Objiterator(object):
    def __init__(self, string):
        self.string = string
        self.i = 1

    def __str__(self):
        return self.string

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= len(self.string):
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration


obj = Objiterator('abc')
print(obj)
for i in obj:
    print(i)


