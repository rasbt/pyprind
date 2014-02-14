# Sebastian Raschka 2014
#
# Progress Bar class to instantiate a progress bar object
# that is printed to the standard output screen to visualize the
# progress in a iterative Python procedure

from math import floor
from pyprind.prog_class import Prog


class ProgBar(Prog):
    """Initializes a progress bar object that allows visuzalization
        of an iterational computation in the standard output screen. 

    Keyword Arguments:
        iterations (int): number of iterations of the computation
        track_time (bool): prints elapsed time when loop has finished
        stream: takes 1 for stdout, 2 for stderr, or given stream object
    """
    def __init__(self, iterations, track_time=True, width=50, stream=2):
        Prog.__init__(self, iterations, track_time, stream)
        self.bar_width = width
        self._adjust_width()
        self.bar_interv = self.max_iter // self.bar_width
        self._print_bar()

    def _adjust_width(self):
        """Shrinks bar if number of iterations is less than the bar width"""
        if self.bar_width > self.max_iter:
            self.bar_width = int(self.max_iter) 
            # some Python 3.3.3 users specifically
            # on Linux Red Hat 4.4.7-1, GCC v. 4.4.7
            # reported that self.max_iter was converted to
            # float. Thus this fix to prevent float multiplication of chars.

    def _print_bar(self):
        progress = floor(self._calc_percent() // self.bar_width)
        remaining = self.bar_width - progress
        if self.cnt == 0:
            self._stream_out('0%% %s 100%%\n' % (' ' * (self.bar_width - 6)))
        self._stream_out('[%s%s]' % ('#' * progress, ' ' * remaining))
        if self._calc_eta():
            self._stream_out(' - ETA [sec]: %.3f' % self._calc_eta())
        self._stream_flush()
        self._stream_out('\r')

    def update(self):
        """Updates the progress bar in every iteration of the task."""
        self.cnt += 1
        self._print_bar()
        if self.cnt == self.max_iter:
            self._stream_out('\n')
            if self.track:
                self._stream_out('Total time elapsed: %.3f sec' % self._elapsed())
                self._stream_out('\n')
