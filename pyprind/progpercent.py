# Sebastian Raschka 2014
#
# Progress Percentage class to instantiate a percentage indicator object
# that is printed to the standard output screen to visualize the
# progress in a iterative Python procedure

import sys
import time

class ProgPercent():
    """Initializes a percentage indicator object that allows visuzalization
       of an iterational computation in the standard output screen. 

    Keyword Arguments:
        iterations (int): number of iterations of the computation

    """
    def __init__(self, iterations):
        self.cnt = 0
        self.max_iter = float(iterations) # accommodation for Python 2.x users
        self.perc = 0
        self.time = [time.clock(), None, None]
        self.__print_percent()

    def __calc_percent(self):
        """Calculates the rel. progress in percent and rounds it to an integer."""
        return round(self.cnt/self.max_iter * 100)

    def __print_percent(self):
        """Prints formatted integer percentage to the screen."""
        sys.stdout.write('\r[%3d %%]' % (self.perc))

    def update(self):
        """Updates the percentage indicator in every iteration of the task."""
        self.cnt += 1
        next_perc = self.__calc_percent()
        if next_perc > self.perc:
            self.perc = next_perc
            self.__print_percent()
            sys.stdout.flush()

    def finish(self, cpu_time=True):
        """Ends the progress tracking and prints the CPU time."""
        self.time[1] = time.clock()
        self.time[2] = self.time[1] - self.time[0]
        sys.stdout.write('\n')
        if cpu_time:
            print('Time elapsed: {0:.4f} sec'.format(self.time[2]))
