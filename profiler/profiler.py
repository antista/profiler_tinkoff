import gc
import pstats
import time
import cProfile
from collections import defaultdict
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
        self.work_time = time.time() - self.start
        self.collect_gc_stat()
        self.collect_profile_stat()
        self.print_report()

        return self

    def collect_gc_stat(self):
        self.collected = 0
        for generation in gc.get_stats():
            self.collected += generation['collected']
        self.curcle_links = gc.collect()

        self.collected_objects = defaultdict(int)
        for item in gc.garbage:
            self.collected_objects[type(item)] += 1

    def collect_profile_stat(self):
        sortby = pstats.SortKey.CUMULATIVE
        self.ps = pstats.Stats(self.pr).sort_stats(sortby)

    def print_report(self):
        print('------------------  Report start  -------------------')
        self.ps.print_stats()
        print(f'Overall time of work: {self.work_time} sec')
        print(f'Count of collected objects by gc: {self.collected}')
        print(f'Objects with circle links: {self.curcle_links} :')
        for type_, count in self.collected_objects.items():
            print(f'\t{type_} : {count}')
        print('-------------------  Report end  --------------------')
