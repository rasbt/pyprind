# Sebastian Raschka 2014
#
# Progress Bar class to instantiate a progress bar object
# that is printed to the standard output screen to visualize the
# progress in a iterative Python procedure

from math import floor
from pyprind.prog_class import Prog
import time


class ProgBar(Prog):
    """
    Initializes a progress bar object that allows visuzalization
    of an iterational computation in the standard output screen.

    Parameters
    ----------
    iterations : `int`
      Number of iterations for the iterative computation.

    track_time : `bool` (default = `True`)
      Prints elapsed time when loop has finished.

    width : `int` (default = 30)
      Sets the progress bar width in characters.

    stream : `int` (default = 2).
      Setting the output stream.
      Takes `1` for stdout, `2` for stderr, or a custom stream object

    title : `str` (default = `''`).
      Setting a title for the progress bar.

    monitor : `bool` (default = False)
      Monitors CPU and memory usage if `True` (requires `psutil` package).

    """
    def __init__(self, iterations, track_time=True, width=30, bar_char='#',
                 stream=2, title='', monitor=False):
        Prog.__init__(self, iterations, track_time, stream, title, monitor)
        self.bar_width = width
        self._adjust_width()
        self.bar_char = bar_char
        self.last_progress = 0
        self._print_labels()
        self._print_progress_bar(0)
        if monitor:
            try:
                self.process.cpu_percent()
                self.process.memory_percent()
            except AttributeError:  # old version of psutil
                self.process.get_cpu_percent()
                self.process.get_memory_percent()
        if self.item_id:
            self._print_item_id()

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
        self._stream_out('[{}{}]'.format(self.bar_char * int(progress),
                                         ' ' * int(remaining)))
        # int() fix for Python 2 users
        self._stream_flush()

    def _print(self):
        progress = floor(self._calc_percent() / 100 * self.bar_width)
        if progress > self.last_progress and self.active:
            self._stream_out('\r')
            self._print_progress_bar(progress)
            if self.track:
                self._print_eta()
            if self.item_id:
                self._print_item_id()
        self.last_progress = progress
