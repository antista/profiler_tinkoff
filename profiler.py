import gc
import pstats
import time
import cProfile
from contextlib import ContextDecorator


class Profiler(ContextDecorator):
    def __enter__(self):
        self.start = time.time()
        self.pr = cProfile.Profile()
        gc.collect()
        gc.set_debug(gc.DEBUG_SAVEALL)

        self.pr.enable()
        return self

    def __exit__(self, *exc):
        self.pr.disable()

        res = gc.get_count()[0] + gc.get_count()[1] + gc.get_count()[2]
        sortby = pstats.SortKey.CUMULATIVE
        ps = pstats.Stats(self.pr).sort_stats(sortby)
        ps.print_stats()
        print(ps.fcn_list)
        print(ps.stats)
        print(ps.total_calls)

        print('Overall time of work: {} sec'.format(time.time() - self.start))
        objects = dict()
        print('Objects with circle links: {} :'.format(gc.collect()))
        garb = gc.garbage
        for item in garb:
            if type(item) not in objects:
                objects[type(item)] = 1
            else:
                objects[type(item)] += 1
        for key in objects.keys():
            print('     {0} : {1}'.format(key, objects[key]))
        print('Count of collected objects by gc: {}'.format(res))
        return


# @Profiler()
def guu(foo, bar):
    print(foo)
    print(bar)
    lst = []
    lst.append(lst)
    t = (1, 3, 'dfghjkl')
    return 123456


# print(guu(1,2))

with Profiler():
    f = Profiler
    print(f.pr)
    print(guu(1, 2))
