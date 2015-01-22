# Sebastian Raschka 01/27/2014
# PyPrind - Python Progress Indicator module

""" The PyPrind (Python Progress Indicator) module lets you visualize the
progress of a programming task in Python via a progress bar or a
percentage indicator.
Progress bars are visualized via a `ProgBar()` object, and
alternatively, the progress can be shown as an percentage via the
`ProgPercent()` object.

Example - Progress Bar
-------------------------------
   ```import pyprind

   n = 10000000
   my_prbar = pyprind.ProgBar(n)
   for i in range(n):
       # do some computation
       my_prbar.update()

   for i in pyprind.prog_bar(range(n)):
       # do something
       pass
   ```

Example - Percentage Indicator
-------------------------------
   ```import pyprind

   n = 1000000
   my_perc = pyprind.ProgPercent(n)
   for i in range(n):
       # do some computation
       my_perc.update()

   for i in pyprind.prog_percent(range(n)):
       # do something
       pass
   ```

"""

from .progbar import ProgBar
from .progpercent import ProgPercent
from .generator_factory import prog_percent
from .generator_factory import prog_bar




__version__ = '2.9.1'
