# Sebastian Raschka 2014
#
# Progress Percentage class to instantiate a percentage indicator object
# that is printed to the standard output screen to visualize the
# progress in a iterative Python procedure

from pyprind.prog_class import Prog


class ProgPercent(Prog):
    """
    Initializes a percentage indicator object that allows visuzalization
    of an iterational computation in the standard output screen. 

    Keyword Arguments:
        iterations (int): number of iterations of the computation
        track_time (bool): default True. Prints elapsed time when loop has finished
        stream (int): default 2. Takes 1 for stdout, 2 for stderr, or given stream object
        title (str): default ''. A title for the progress bar
        monitor (bool): default False. Monitors CPU and memory usage if True 
            (requires 'psutil' package).

    """
    def __init__(self, iterations, track_time=True, stream=2, title='', monitor=False):
        Prog.__init__(self, iterations, track_time, stream, title, monitor)
        self.last_progress = 0
        self._print()
        if monitor:
            try:
                self.process.get_cpu_percent()
                self.process.get_memory_percent()
            except AttributeError: # old version of psutil
                cpu_total = self.process.cpu_percent()
                mem_total = self.process.memory_percent()   


    def _print(self):
        """ Prints formatted integer percentage and tracked time to the screen."""
        next_perc = self._calc_percent()
        if next_perc > self.last_progress and self.active:
            self.last_progress = next_perc
            self._stream_out('\r[%3d %%]' % (self.last_progress))
            if self.track:
                self._stream_out(' elapsed[sec]: {:.3f}'.format(self._elapsed()))
                self._print_eta()
            if self.item_id:
                self._print_item_id()

