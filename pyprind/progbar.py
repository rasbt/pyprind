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
    def __init__(self, iterations, track_time=True, width=30, stream=2):
        Prog.__init__(self, iterations, track_time, stream)
        self.bar_width = width
        self._adjust_width()
        self.last_progress = 0
        self._print_labels()
        self._print_progress_bar(0)

    def _adjust_width(self):
        """Shrinks bar if number of iterations is less than the bar width"""
        if self.bar_width > self.max_iter:
            self.bar_width = int(self.max_iter) 
            # some Python 3.3.3 users specifically
            # on Linux Red Hat 4.4.7-1, GCC v. 4.4.7
            # reported that self.max_iter was converted to
            # float. Thus this fix to prevent float multiplication of chars.

    def _print_labels(self):
        self._stream_out('0% {} 100%\n'.format(' ' * (self.bar_width - 6)))
        self._stream_flush()

    def _print_progress_bar(self, progress):
        remaining = self.bar_width - progress
        self._stream_out('[{}{}]'.format('#' * int(progress), ' ' * int(remaining)))
        # int() fix for Python 2 users
        self._stream_flush()

    def _print_eta(self):
        self._stream_out(' | ETA [sec]: {:.3f} sec '.format(self._calc_eta()))
        self._stream_flush()

    def _print_bar(self):
        progress = floor(self._calc_percent() / 100 * self.bar_width)
        if progress > self.last_progress:
            self._stream_out('\r')
            self._print_progress_bar(progress)
            if self._calc_eta() and self.track:
                self._print_eta()
        self.last_progress = progress

    def update(self):
        """Updates the progress bar in every iteration of the task."""
        self.cnt += 1
        self._print_bar()
        self._finish() 
