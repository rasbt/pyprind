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
        track_time (bool): prints elapsed time

    """
    def __init__(self, iterations, track_time=True):
        self.cnt = 1
        self.max_iter = float(iterations) # accommodation for Python 2.x users
        self.perc = 0
        self.time = [time.clock(), 0]
        self.track = track_time
        self.__print_update()

    def __calc_percent(self):
        """Calculates the rel. progress in percent and rounds it to an integer."""
        return round(self.cnt/self.max_iter * 100)

    def __print_update(self):
        """Prints formatted integer percentage and tracked time to the screen."""
        sys.stdout.write('\r[%3d %%]' % (self.perc))
        if self.track:
            self.time[1] = time.clock()
            sys.stdout.write('   elapsed: %.3f sec' % self.time[1])

    def update(self):
        """Updates the percentage indicator in every iteration of the task."""
        next_perc = self.__calc_percent()
        if next_perc > self.perc:
            self.perc = next_perc
            self.__print_update()
            sys.stdout.flush()
        self.cnt += 1
        if self.cnt == self.max_iter:
            sys.stdout.write('\n') 
 
