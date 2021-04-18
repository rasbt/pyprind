[![Build Status](https://travis-ci.org/rasbt/pyprind.svg?branch=master)](https://travis-ci.org/rasbt/pyprind)
[![Coverage Status](https://coveralls.io/repos/rasbt/pyprind/badge.svg?branch=master&service=github)](https://coveralls.io/github/rasbt/pyprind?branch=master)
![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)
![Python 3](https://img.shields.io/badge/python-3-blue.svg)
[![License](https://img.shields.io/badge/license-new%20BSD-blue.svg)](https://github.com/rasbt/pyprind/blob/master/LICENSE.txt)



# PyPrind (Python Progress Indicator)


The `PyPrind` (Python Progress Indicator) module provides a **progress bar** and a
**percentage indicator** object that let you track the progress of a loop structure or other iterative computation.  
Typical applications include the processing of large data sets to provide an intuitive estimate
at runtime about the progress of the computation.



![PyPrind Demo](./images/pyprind-1.gif "PyPrind Demo")

<br>

#### Progress Bars and Percentage Generators

```python
import pyprind

for i in pyprind.prog_bar(range(n)):
    time.sleep(timesleep) # your computation here
```
```
0%                          100%
[##############################] | ETA: 00:00:00
Total time elapsed: 00:00:05
```

<br>
<br>

```python
for i in pyprind.prog_percent(range(n)):
    time.sleep(timesleep) # your computation here
```

```
[10 %] Time elapsed: 00:00:01 | ETA: 00:00:04
```

#### While-loops

The `ProgBar` and `ProgPercent` classes also support while loops if desired.
The objects are updated inside the loop using the `update` method as shown below:

```python
import random
import pyprind
import time

timesleep = 0.05
random.seed(1)
collection = set()

n = 100
bar = pyprind.ProgBar(n, track_time=False, title='while example')

while len(collection) < n:
    r = random.randint(0, 10**5)
    if r % 7 and r not in collection:
        collection.add(r)
        bar.update()
        time.sleep(timesleep)

print(bar)
```
```
while example
0%                          100%
[##############################]
Title: while example
  Started: 09/07/2016 13:06:58
  Finished: 09/07/2016 13:07:03
  Total time elapsed: 00:00:05
```


<br>
<br>

<a id='advanced_tracking'>

#### Advanced Tracking

If you have the `psutil` package installed, you can set the `monitor=True` to track CPU and memory usage:

```python
bar = pyprind.ProgBar(n, monitor=True)
for i in range(n):
    time.sleep(timesleep) # your computation here
    bar.update()
print(bar)
```

```
0%                          100%
[##############################] | ETA: 00:00:00
Total time elapsed: 00:00:05
Title:
  Started: 09/07/2016 13:14:09
  Finished: 09/07/2016 13:14:14
  Total time elapsed: 00:00:05
  CPU %: 1.90
  Memory %: 0.48
```

<br>
<br>

#### Choose Your Favorite Bar Style

```python
bar = pyprind.ProgBar(n, bar_char='█')
for i in range(n):
    time.sleep(0.1) # do some computation
    bar.update()
```

```
0%                          100%
[██████████████████████████████] | ETA: 00:00:00
Total time elapsed: 00:00:10
```

#### Note to PyCharm users

If you are using the PyCharm IDE, you need to pass the `sys.stdout` or `sys.err`
as a `stream` argument to display the progress indicators correctly in the IDE. For example,

```python
import sys

bar = pyprind.ProgBar(n, stream=sys.stdout)
for i in range(n):
    time.sleep(0.1) # do some computation
    bar.update()
```

<br>
<br>

###[View more examples in an IPython Demo Notebook](http://nbviewer.ipython.org/github/rasbt/pyprind/blob/master/examples/pyprind_demo.ipynb)


<br>
<br>


<a id='sections'>

# Sections


- [Installation](#installation)
- [Documentation](#documentation)
- [Examples](#examples)
- [Contact](#contact)
- [Changelog](https://raw.githubusercontent.com/rasbt/pyprind/master/CHANGELOG.txt)


<p><a id="installation"></a></p>

<br>
<br>
<br>

# Installation

[[back to top](#sections)]

The most convenient way to install PyPrind is via tools like `pip` or `easy_install`:

- `pip install pyprind`  

-  `easy_install pyprind`  



PyPrind comes without any dependencies except for the optional [psutil](https://pypi.python.org/pypi/psutil) to [monitor CPU and memory usages](#advanced_tracking). You can install `psutil` via `pip install psutil` or install it automatically with PyPrind:  
 `pip install pyprind -r requirements.txt`



Alternatively, you can install PyPrind the classic way: Download the package from the Python Package Index [https://pypi.python.org/pypi/PyPrind](https://pypi.python.org/pypi/PyPrind), unzip it,
navigate into the unzipped directory, and use the command

`python setup.py install`  




<p><a id="documentation"></a></p>
<br>
<br>
<br>

# Documentation

[[back to top](#sections)]



PyPrind consists of two class objects that can visualize the progress of a computation on the output screen.  
Progress bars are available via `ProgBar`, and percentage indicators can be used via a `ProgPercent`.  

```python
	n = 10000000
	bar = pyprind.ProgBar(n)   # 1) initialization with number of iterations
	for i in range(n):
    	# do some computation
    	bar.update()           # 2) update the progress visualization
```

Alternatively, the progress can be tracked via the equivalent generator functions `prog_bar` and `prog_percent`:

```python
	for i in pyprind.prog_bar(range(n)):
    	# do something
    	pass
```


<br>

#### Complete Parameter of Parameters and Options

##### ProgBar

*`ProgBar(iterations, track_time=True, width=30, bar_char='#',
               stream=2, title='', monitor=False, update_interval=None))`*

- iterations : `int`  
    Number of iterations for the iterative computation.
- track_time : `bool` (default: `True`)  
    Prints elapsed time when loop has finished.
- width : `int` (default: 30)  
    Sets the progress bar width in characters.
- stream : `int` (default: 2).  
    Setting the output stream.
    Takes `1` for stdout, `2` for stderr, or a custom stream object
- title : `str` (default:  `''`)  
    Setting a title for the progress bar.
- monitor : `bool` (default: `False`)  
    Monitors CPU and memory usage if `True` (requires `psutil` package).
- update_interval : float or int (default: `None`)  
    The update_interval in seconds controls how often the progress
    is flushed to the screen.
    Automatic mode if `update_interval=None`.

##### ProgPercent

*`ProgPercent(iterations, track_time=True,
               stream=2, title='', monitor=False, update_interval=None)`*

- iterations : `int`  
    Number of iterations for the iterative computation.  
- track_time : `bool` (default: `True`)  
    Prints elapsed time when loop has finished.
- stream : `int` (default: 2).  
    Setting the output stream.
    Takes `1` for stdout, `2` for stderr, or a custom stream object
- title : `str` (default : `''`).  
    Setting a title for the percentage indicator.
- monitor : `bool` (default: `False`)  
    Monitors CPU and memory usage if `True` (requires `psutil` package).
- update_interval : float or int (default: `None`)  
    The update_interval in seconds controls how often the progress
    is flushed to the screen.
    Automatic mode if `update_interval=None`.

##### update method

*`update(iterations=1, item_id=None, force_flush=False)`*

- iterations : int (default: `1`)  
    default argument can be changed to integer values
    `>=1` in order to update the progress indicators more than once
    per iteration.
- item_id : str (default: `None`)  
    Print an item_id sring behind the progress bar
- force_flush : bool (default: `False`)  
    If True, flushes the progress indicator to the output screen
    in each iteration.

<br>


<p><a id="examples"></a></p>

<br>
<br>
<br>

# Examples

[[back to top](#sections)]

Examples for using the progress bar and percentage indicator objects can be found in the [IPython Demo Notebook](https://github.com/rasbt/pyprind/blob/master/examples/pyprind_demo.ipynb).

<p><a id="contact"></a></p>

<br>
<br>
<br>



