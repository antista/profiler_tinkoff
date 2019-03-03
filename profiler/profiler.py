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

        self.collected = gc.get_count()[0] + gc.get_count()[1] + gc.get_count()[2]
        self.work_time = time.time() - self.start
        self.curcle_links = gc.collect()
        sortby = pstats.SortKey.CUMULATIVE
        self.ps = pstats.Stats(self.pr).sort_stats(sortby)

        self.garbage = gc.garbage
        self.collected_objects = dict()
        for item in self.garbage:
            if type(item) not in self.collected_objects:
                self.collected_objects[type(item)] = 1
            else:
                self.collected_objects[type(item)] += 1
        self.print_res()
        return self

    def print_res(self):
        self.ps.print_stats()
        print('Overall time of work: {} sec'.format(self.work_time))
        print('Count of collected objects by gc: {}'.format(self.collected))
        print('Objects with circle links: {} :'.format(self.curcle_links))
        for key in self.collected_objects.keys():
            print('     {0} : {1}'.format(key, self.collected_objects[key]))
