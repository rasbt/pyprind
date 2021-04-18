Version 2.11.3
================

- Fixes and issue where newlines appeared everywhere on certain machines.

Version 2.11.2
================

- Fixes issue where new lines are printed upon iterating over a completed progress bar object.

Version 2.11.1
================
- Flushes both `stdout` and `stderr` prior to `ProgressBar` initialization to avoid cluttering environments with previously cached print statements.

Version 2.11.0
================
- Use only 1 line to print the progress bar (instead of the previous too lines)


Version 2.10.0
================
- Fixes an issue with Jupyter Notebook 4.3.1 when the `ETA` got printed on new lines


Version 2.9.9
================
- added PyCharm support


Version 2.9.8
================
- raise `ValueError` if `monitor` is set to `True` and `psutils` is not installed


Version 2.9.7
================
- requirements.txt for `psutil`, now supports `pip install pyprind -r requirements.txt`


Version 2.9.5
================
- new `update_interval` parameter to control the update frequency in seconds
- new `force_flush` parameter to print the progress after every iteration


Version 2.9.4
================
- new time formatting in hh:mm:ss format (by Divyanshu Sharma, https://github.com/Div44)
- permissive new BSD license


VERSION 2.9.3
================
- some PEP8 adjustments and code cleanup
- new `bar` argument for ProgressBar to use
  your favorite bar style (by Konstantin Tolstikhin)


VERSION 2.9.2
================
- support for psutil >= 2.0 and < 2.0.
- removed psutil from the setup requirements and made it's installation
  optional via "pip install pyprind -r requirements.txt"


VERSION 2.9.1
================
- Minor reorganization of the generator interface.
- Minor changes to the code documentation.
- Added new test files.


VERSION 2.9.0
================
- New generator functions for progress bar and percentage indicators via:

    for i in pyprind.prog_bar(range(n)):
        # do something
        pass

    for i in pyprind.prog_percent(range(n)):
        # do something
        pass

(by Olaf Gladis, https://github.com/hwmrocker)


VERSION 2.8.0
================
- A new `.stop()` method to stop the progress bar / percentage indicator early.
- `.update()` method accepts an `item_id` argument now in order to display
  which item is currently processed next to the progress bar / percentage indicator.
  E.g.,
	Job1
	0%                100%
	[####################] | ETA[sec]: 0.000 | Item ID: file_xyz.csv


VERSION 2.7.0
================
- Version intentionally skipped to not cause confusion that
  this is a tool exclusively for Python 2.7.


VERSION 2.6.2
================
- Fixed bug that the report was squeezed after the bar and before the "time elapsed" string if printed immediately after the progress bar has reached 100%.


VERSION 2.6.1
================
- Small bugfix on some system a warning was printed although
  a valid output string was provided.


VERSION 2.6.0
================
- Added IPython Notebook support
- Fixed to work with most recent psutil v. 0.6 for monitoring CPU and memory usage


VERSION 2.5.0
================
- New default argument `monitor=False` was added to `ProgBar()` and `ProgPercent()` objects to monitor memory and CPU usage (via `psutil`) if `monitor` is set to True.


VERSION 2.4.0
================
- Default argument for `.update(iterations=1)` methods to increment the count by more than 1 per
  iteration.


VERSION 2.3.1
================
- Minor fix of the output formatting.


VERSION 2.3.0
================
- Added native print() support
  prints title and elapsed time of an tracked object after loop completed.
- Data member self.end stores elapsed time when loop completed.
- Data member self.title saves title of the tracking objects.


VERSION 2.2.0
================
- added ETA (estimated time until arrival) tracking to progress bar  
  (by Taylan Aydinli).
- better support for Python 2.x.



VERSION 2.1.1
================
- Changed visuals of the printed progress for percentage indicators.


VERSION 2.1.0
================
- added ETA (estimated time until arrival) tracking to percentage indicator  
  (by Taylan Aydinli, https://github.com/taylan)


VERSION 2.0.3
================
- Accepts a given outputstream for the `stream` parameter.


VERSION 2.0.2
================
- Fixed bug that occurred for some Python 3.3.3 users
specifically on Linux Red Hat 4.4.7-1, GCC v. 4.4.7
that self.max_iter was cast to a float when `ProgBar()`
object was seeded with n=48.


VERSION 2.0.1
================
- Fixed packaging of example files.


VERSION 2.0.0
==============
- ProgBar and ProgPerc inherit data members from parent class Prog
- Added ProgBar and ProgPerc default argument `stream=2` to write to stderr by
  default. Set `stream=1` to write to stdout.

    my_prbar = pyprind.ProgBar(n, stream=1) # writes to stdout
    my_prbar = pyprind.ProgBar(n, stream=2) # writes to stderr, default

- Does not redirect data to the standard output or error stream if program is not
  outputting to a terminal.


VERSION 1.1.1
==============
- Fixed problem with packaging of example scripts.


VERSION 1.1.0
===============
- Added live time tracking to percentage indicator
- progress bar and percentage indicator complete automatically,
  .finish() was removed


VERSION 1.0.4
===============
- Added boundary that .update() can't print over the
  right progress bar limit.
- Prints warning when ProgBar seed exits the number of iterations
  in the loop.


VERSION 1.0.3
===============
- Reformatting of README files.
- Minor updates in setup.py file.


VERSION 1.0.2
===============
- Corrected errors in the README files.
- Added docstring to the __init__.py


VERSION 1.0.1
===============
- Added more README formats.
- Added class descriptions.
- Added example scripts to the distribution.
