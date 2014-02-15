# Sebastian Raschka 2014
#
# Progress Percentage class to instantiate a percentage indicator object
# that is printed to the standard output screen to visualize the
# progress in a iterative Python procedure

from pyprind.prog_class import Prog


class ProgPercent(Prog):
    """Initializes a percentage indicator object that allows visuzalization
       of an iterational computation in the standard output screen. 

    Keyword Arguments:
        iterations (int): number of iterations of the computation
        width (int): width of the progress bar in characters
        track_time (bool): prints elapsed time and estimated time left
        stream: takes 1 for stdout, 2 for stderr, or given stream object
    """
    def __init__(self, iterations, track_time=True, stream=2):
        Prog.__init__(self, iterations, track_time, stream)
        self.perc = 0
        self._print_update()

    def _print_update(self):
        """Prints formatted integer percentage and tracked time to the screen."""
        self._stream_out('\r[%3d %%]' % (self.perc))
        if self.track:
            self._stream_out(' elapsed [sec]: {:.3f}'.format(self._elapsed()))
            if self._calc_eta():
                self._stream_out(' | ETA[sec]: {:.3f} '.format(self._calc_eta()))  
            self._stream_flush()

    def update(self):
        """Updates the percentage indicator in every iteration of the task."""
        self.cnt += 1
        next_perc = self._calc_percent()
        if next_perc > self.perc:
            self.perc = next_perc
            self._print_update()
            self._stream_flush()
        self._finish()
