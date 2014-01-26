import sys
import time

class ProgBar():
    """ Initializes a progress bar object that allows visuzalization
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
        if self.bar_width > self.max_iter:
            self.bar_width = self.max_iter

    def __init_bar(self):
        sys.stdout.write('0%% %s 100%%\n' %(' ' * (self.bar_width - 6)))
        sys.stdout.write('[%s]' % (' ' * self.bar_width))
        sys.stdout.flush()
        sys.stdout.write('\b' * (self.bar_width + 1))

    def update(self):
        """Updates the progress bar in every iteration of the task."""
        self.cnt += 1
        if self.cnt % self.bar_interv == 0:
            sys.stdout.write("#")
            sys.stdout.flush()

    def finish(self, cpu_time=True):
        """Ends the progress tracking and prints the CPU time."""
        self.time[1] = time.clock()
        self.time[2] = self.time[1] - self.time[0]
        sys.stdout.write('\n')
        if cpu_time:
            print('Time elapsed: {0:.4f} sec'.format(self.time[2]))
