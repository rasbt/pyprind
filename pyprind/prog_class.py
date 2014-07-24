import time
import sys
import os
from io import UnsupportedOperation

class Prog():
    def __init__(self, iterations, track_time, stream, title, monitor):
        """ Initializes tracking object. """
        self.cnt = 0
        self.title = title
        self.max_iter = float(iterations) # to support Python 2.x
        self.track = track_time
        self.start = time.time()
        self.end = None
        self.total_time = 0.0
        self.monitor = monitor
        self.stream = stream
        self._stream_out = self._no_stream
        self._stream_flush = self._no_stream
        self._check_stream()
        self._print_title()
        
        if self.monitor:
            import psutil
            self.process = psutil.Process()

    def _check_stream(self):
        """ Determines which output stream (stdout, stderr, or custom) to use. """
        if self.stream:
            try:
                if self.stream == 1 and os.isatty(sys.stdout.fileno()):
                    self._stream_out = sys.stdout.write
                    self._stream_flush = sys.stdout.flush
                elif self.stream == 2 and os.isatty(sys.stderr.fileno()):
                    self._stream_out = sys.stderr.write
                    self._stream_flush = sys.stderr.flush
            except UnsupportedOperation:  # a fix for IPython notebook "IOStream has no fileno."
                if self.stream == 1:
                    self._stream_out = sys.stdout.write
                    self._stream_flush = sys.stdout.flush
                elif self.stream == 2:
                    self._stream_out = sys.stderr.write
                    self._stream_flush = sys.stderr.flush
            else:
                if self.stream is not None and hasattr(self.stream, 'write'):
                    self._stream_out = self.stream.write
                    self._stream_flush = self.stream.flush
        else:
            print('Warning: No valid output stream.')



    def _elapsed(self):
        """ Returns elapsed time at update. """
        return time.time() - self.start

    def _calc_eta(self):
        """ Calculates estimated time left until completion. """
        elapsed = self._elapsed()
        if self.cnt == 0 or elapsed < 0.001:
            return None
        rate = float(self.cnt) / elapsed
        return (float(self.max_iter) - float(self.cnt)) / rate

    def _calc_percent(self):
        """Calculates the rel. progress in percent with 2 decimal points."""
        return round(self.cnt / self.max_iter * 100, 2)

    def _no_stream(self, text=None):
        """ Called when no valid output stream is available. """
        pass

    def _finish(self):
        """ Determines if maximum number of iterations (seed) is reached. """
        if self.cnt == self.max_iter:
            self.total_time = self._elapsed()
            self.end = time.time()
            if self.track:
                self._stream_out('\nTotal time elapsed: {:.3f} sec'.format(self.total_time))
            self._stream_out('\n')

    def _print_title(self):
        """ Prints tracking title at initialization. """
        if self.title:
            self._stream_out('{}\n'.format(self.title))
            self._stream_flush()

    def __repr__(self):
        str_start = time.strftime('%m/%d/%Y %H:%M:%S', time.localtime(self.start))
        str_end = time.strftime('%m/%d/%Y %H:%M:%S', time.localtime(self.end))
        if not self.monitor:
            return """Title: {}
                      Started: {}
                      Finished: {}
                      Total time elapsed: {:.3f} sec""".format(self.title, str_start, 
                                                               str_end, self.total_time)
        else:
            try:
                cpu_total = self.process.get_cpu_percent()
                mem_total = self.process.get_memory_percent()
            except AttributeError: # old version of psutil
                cpu_total = self.process.cpu_percent()
                mem_total = self.process.memory_percent()    

            return """Title: {}
                      Started: {}
                      Finished: {}
                      Total time elapsed: {:.3f} sec
                      CPU %: {:2f}
                      Memory %: {:2f}""".format(self.title, str_start, str_end, self.total_time, cpu_total, mem_total)

    def __str__(self):
        return self.__repr__()
