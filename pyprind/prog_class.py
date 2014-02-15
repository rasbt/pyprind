import time
import sys
import os


class Prog():
    def __init__(self, iterations, track_time, stream):
        self.cnt = 0
        self.max_iter = float(iterations) # to support Python 2.x
        self.track = track_time
        self.start = time.time()
        self.stream = stream
        self._stream_out = self._no_stream
        self._stream_flush = self._no_stream
        self._check_stream()

    def _check_stream(self):
        if self.stream == 1 and os.isatty(sys.stdout.fileno()):
            self._stream_out = sys.stdout.write
            self._stream_flush = sys.stdout.flush
        elif self.stream == 2 and os.isatty(sys.stderr.fileno()):
            self._stream_out = sys.stderr.write
            self._stream_flush = sys.stderr.flush
        elif self.stream is not None and hasattr(self.stream, 'write'):
            self._stream_out = self.stream.write
            self._stream_flush = self.stream.flush
        else:
            print('Warning: No valid output stream.')

    def _elapsed(self):
        return time.time() - self.start

    def _calc_eta(self):
        elapsed = self._elapsed()
        if self.cnt == 0 or elapsed < 0.001:
            return None
        rate = float(self.cnt) / elapsed
        return (float(self.max_iter) - float(self.cnt)) / rate

    def _calc_percent(self):
        """Calculates the rel. progress in percent with 2 decimal points."""
        return round(self.cnt / self.max_iter * 100, 2)

    def _no_stream(self, text=None):
        pass

    def _finish(self):
        if self.cnt == self.max_iter:
            if self.track:
                self._stream_out('\nTotal time elapsed: {:.3f} sec'.format(self._elapsed()))
            self._stream_out('\n')
