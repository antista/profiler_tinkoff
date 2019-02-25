import gc
import pstats
import time
import cProfile


class Profiler:
    def __init__(self, function, *args, **kwargs):
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.start = time.time()

    def __enter__(self, *args, **kwargs):
        return self.__time_prof(*self.args, **self.kwargs)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __call__(self, *args, **kwargs):
        return self.__time_prof(*args, **kwargs)

    def __time_prof(self, *args, **kwargs):
        pr = cProfile.Profile()
        gc.collect()
        gc.set_debug(gc.DEBUG_SAVEALL)

        pr.enable()
        tmp = self.function(*args, **kwargs)
        pr.disable()

        res = gc.get_count()[0] + gc.get_count()[1] + gc.get_count()[2]
        sortby = pstats.SortKey.CUMULATIVE
        ps = pstats.Stats(pr).sort_stats(sortby)
        ps.print_stats()

        print('Overall time of work: {} sec'.format(time.time() - self.start))
        objects = dict()
        print('Objects with circle links: {} :'.format(gc.collect()))
        for item in gc.garbage:
            if type(item) not in objects:
                objects[type(item)] = 1
            else:
                objects[type(item)] += 1
        for key in objects.keys():
            print('     {0} : {1}'.format(key, objects[key]))
        print('Count of collected objects by gc: {}'.format(res))

        return tmp
