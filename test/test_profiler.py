import time

from profiler import Profiler


def test_simple():
    with Profiler() as prof:
        simple_function(1, 2)
    assert prof.curcle_links == 1
    assert len(prof.collected_objects)
    assert prof.work_time > 2
    assert prof.work_time < 3


def test_empty():
    with Profiler() as prof:
        empty_function()
    assert not prof.curcle_links
    assert prof.work_time < 1


def test_curcle_links():
    with Profiler() as prof:
        circle_list_function()
    assert prof.curcle_links == 2


def test_complicated():
    with Profiler() as prof:
        complicated_function()
    assert not prof.curcle_links
    assert prof.work_time < 1
    assert prof.ps.total_calls


def simple_function(foo, bar):
    print(foo)
    print(bar)
    lst = []
    lst.append(lst)
    t = (1, 3, 'dfghjkl')
    time.sleep(2)
    return 123456


def complicated_function():
    h = ('rewwqq', 76543567)
    t = second_function()
    return 32123


def second_function():
    s = []
    g = 1234321
    u = 'fghjklkj'
    return {'jhgf', 'poiuy', 98765456}


def empty_function():
    pass


def circle_list_function():
    lst = []
    k = [lst]
    lst.append(k)
