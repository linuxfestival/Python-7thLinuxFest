# In The Name Of God
# ========================================
# [] File Name : iterators.py
#
# [] Creation Date : 14-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'


class YRange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


y = YRange(3)
print(next(y))
print(next(y))
print(next(y))


class ZRange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return ZRangeIter(self.n)


class ZRangeIter:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        # Iterators are iterables too.
        # Adding this functions to make them so.
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


y = YRange(5)
print(list(y))
print(list(y))

z = ZRange(5)
print(list(z))
print(list(z))