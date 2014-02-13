import time
import sys
import os


class Prog():
    def __init__(self, iterations, track_time, stream):
        self.cnt = 0
        self.max_iter = iterations
        self.track = track_time
        self.start = time.clock()
        self.stream = stream
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
            self._stream_out = self._no_stream
            self._stream_flush = self._no_stream

    def _elapsed(self):
        return time.clock() - self.start

    def _no_stream(self, text=None):
        pass
