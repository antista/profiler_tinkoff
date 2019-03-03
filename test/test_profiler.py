from profiler import Profiler


def test_simple(guu):
    f = Profiler()
    f.__enter__()
    guu(1, 2)
    f.__exit__()
    assert f.curcle_links == 1
    assert len(f.collected_objects)
    assert f.work_time > 2
    assert f.work_time < 3


def test_empty(foo):
    f = Profiler()
    f.__enter__()
    foo()
    f.__exit__()
    assert not f.curcle_links
    assert f.work_time < 1


def test_curcle_links(bar):
    f = Profiler()
    f.__enter__()
    bar()
    f.__exit__()
    assert f.curcle_links == 2


def test_complicated(uu):
    f = Profiler()
    f.__enter__()
    uu()
    f.__exit__()
    assert not f.curcle_links
    assert f.work_time < 1
    assert f.ps.total_calls
