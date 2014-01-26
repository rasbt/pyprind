import sys
import time

class ProgPercent():
    """ Prints a progress of an computation as percentage to the standard output."""

    def __init__(self, iterations):
        self.cnt = 0
        self.max_iter = float(iterations) # accommodation for Python 2.x users
        self.perc = 0
        self.time = [time.clock(), None, None]
        self.__print_percent()

    def __calc_percent(self):
        return round(self.cnt/self.max_iter * 100)

    def __print_percent(self):
        sys.stdout.write('\r[%3d %%]' % (self.perc))

    def update(self):
        self.cnt += 1
        next_perc = self.__calc_percent()
        if next_perc > self.perc:
            self.perc = next_perc
            self.__print_percent()
            sys.stdout.flush()

    def finish(self, cpu_time=True):
        self.time[1] = time.clock()
        self.time[2] = self.time[1] - self.time[0]
        sys.stdout.write('\n')
        if cpu_time:
            print('Time elapsed: {0:.4f} sec'.format(self.time[2]))


