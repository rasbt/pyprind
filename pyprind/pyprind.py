import sys
import time

class ProgBar()
    """ Prints a progress bar to the standard output."""

    def __init__(self, iterations, width=50):
        self.cnt = 0
        self.max_iter = iterations
        self.bar_width = width
        self.__adjust_width()
        self.bar_interv = self.max_iter // self.bar_width
        self.time = [time.clock(), None, None]
        self.__init_bar()

    def __adjust_width(self):
        if self.bar_width > self.max_iter:
            self.bar_width = self.max_iter

    def __init_bar(self):
        sys.stdout.write('0%% %s 100%%\n' %(' ' * (self.bar_width - 6)))
        sys.stdout.write('[%s]' % (' ' * self.bar_width))
        sys.stdout.flush()
        sys.stdout.write('\b' * (self.bar_width + 1))

    def update(self):
        self.cnt += 1
        if self.cnt % self.bar_interv == 0:
            sys.stdout.write("#")
            sys.stdout.flush()

    def finish(self, cpu_time=True):
        self.time[1] = time.clock()
        self.time[2] = self.time[1] - self.time[0]
        sys.stdout.write('\n')
        if cpu_time:
            print('Time elapsed: {0:.4f} sec'.format(self.time[2]))


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


