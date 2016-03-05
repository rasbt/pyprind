# PyPrind
# Author: Sebastian Raschka <mail@sebastianraschka.com>
# Contributors: https://github.com/rasbt/pyprind/graphs/contributors
# License: BSD 3 clause
# Code Repository: https://github.com/rasbt/pyprind
# PyPI: https://pypi.python.org/pypi/PyPrind

from pyprind.prog_class import Prog


class ProgPercent(Prog):
    """
    Initializes a progress bar object that allows visuzalization
    of an iterational computation in the standard output screen.

    Parameters
    ----------
    iterations : `int`
      Number of iterations for the iterative computation.

    track_time : `bool` (default = `True`)
      Prints elapsed time when loop has finished.

    stream : `int` (default = 2).
      Setting the output stream.
      Takes `1` for stdout, `2` for stderr, or a custom stream object

    title : `str` (default = `''`).
      Setting a title for the percentage indicator.

    monitor : `bool` (default = False)
      Monitors CPU and memory usage if `True` (requires `psutil` package).

    """
    def __init__(self, iterations, track_time=True,
                 stream=2, title='', monitor=False):
        Prog.__init__(self, iterations, track_time, stream, title, monitor)
        self.last_progress = 0
        self._print()
        if monitor:
            try:
                self.process.cpu_percent()
                self.process.memory_percent()
            except AttributeError:  # old version of psutil
                self.process.get_cpu_percent()
                self.process.get_memory_percent()

    def _print(self):
        """ Prints formatted percentage and tracked time to the screen."""
        next_perc = self._calc_percent()
        if (next_perc > self.last_progress or
                self.force_flush) and self.active:
            self.last_progress = next_perc
            self._stream_out('\r[%3d %%]' % (self.last_progress))
            if self.track:
                self._stream_out(' Time elapsed: ' +
                                 self._get_time(self._elapsed()))
                self._print_eta()
            if self.item_id:
                self._print_item_id()
