class MyRange:
    def __init__(self, a, b=None, c=None):
        if c is not None:
            self.start = a
            self.end = b
            self.step = c
        elif b is not None:
            self.start = a
            self.end = b
            self.step = 1
        else:
            self.start = 0
            self.end = a
            self.step = 1

    def __iter__(self):
        self.cursor = self.start - self.step
        return self

    def __next__(self):
        self.cursor += self.step
        if self.cursor >= self.end:
            raise StopIteration
        return self.cursor


def my_range(start, end, step):
    while start < end:
        yield start
        start += step


# for i in my_range(1, 15, 3):
#     print(i)