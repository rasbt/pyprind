# Sebastian Raschka 01/26/2014
#
# Progress Bar class to instantiate a progress bar object
# that is printed to the standard output screen to visualize the
# progress in a iterative Python procedure

import sys
import time

class ProgBar():
    """Initializes a progress bar object that allows visuzalization
        of an iterational computation in the standard output screen. 

    Keyword Arguments:
        iterations (int): number of iterations of the computation
        width (int): width of the progress bar in characters
    """
    def __init__(self, iterations, width=50):
        self.cnt = 0
        self.max_iter = iterations
        self.bar_width = width
        self.__adjust_width()
        self.bar_interv = self.max_iter // self.bar_width
        self.time = [time.clock(), None, None]
        self.__init_bar()

    def __adjust_width(self):
        """Shrinks bar if number of iterations is less than the bar width"""
        if self.bar_width > self.max_iter:
            self.bar_width = self.max_iter

    def __init_bar(self):
        """Writes the initial bar frames to the output screen"""
        sys.stdout.write('0%% %s 100%%\n' %(' ' * (self.bar_width - 6)))
        sys.stdout.write('[%s]' % (' ' * self.bar_width))
        sys.stdout.flush()
        sys.stdout.write('\b' * (self.bar_width + 1))

    def update(self):
        """Updates the progress bar in every iteration of the task."""
        self.cnt += 1
        if self.cnt % self.bar_interv == 0 and self.cnt <= self.max_iter:
            sys.stdout.write("#")
            sys.stdout.flush()

    def finish(self, cpu_time=True):
        """Ends the progress tracking and prints the CPU time."""
        self.time[1] = time.clock()
        self.time[2] = self.time[1] - self.time[0]
        sys.stdout.write('\n')
        if self.cnt > self.max_iter:
            print("WARNING: Number of iterations exceeded the the ProgBar() seed.")
        if cpu_time:
            print('Time elapsed: {0:.4f} sec'.format(self.time[2]))
