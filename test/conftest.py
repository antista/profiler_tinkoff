import time

import pytest


@pytest.fixture()
def guu(foo, bar):
    def guu(foo, bar):
        print(foo)
        print(bar)
        lst = []
        lst.append(lst)
        t = (1, 3, 'dfghjkl')
        time.sleep(2)
        return 123456

    return guu


@pytest.fixture()
def uu():
    def uu():
        h = ('rewwqq', 76543567)
        t = uuu()
        return 32123

    return uu


def uuu():
    s = []
    g = 1234321
    u = 'fghjklkj'
    return {'jhgf', 'poiuy', 98765456}


@pytest.fixture()
def foo():
    def foo():
        pass

    return foo


@pytest.fixture()
def bar():
    def bar():
        lst = []
        k = [lst]
        lst.append(k)

    return bar
