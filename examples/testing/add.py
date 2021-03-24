import unittest


def add(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x + y
    raise TypeError('Can only add integer arguments')
