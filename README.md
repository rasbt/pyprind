[![PyPI version](https://badge.fury.io/py/pyprind.svg)](http://badge.fury.io/py/pyprind)
[![License](https://img.shields.io/badge/license-new%20BSD-blue.svg)](https://github.com/rasbt/pyprind/blob/master/LICENSE.txt)
![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)
![Python 3.4](https://img.shields.io/badge/python-3.4-blue.svg)

# PyPrind (Python Progress Indicator)


The `PyPrind` (Python Progress Indicator) module provides a **progress bar** and a **percentage indicator** object that let you track the progress of a loop structure or other iterative computation.  
Typical applications include the processing of large data sets to provide an intuitive estimate
at runtime about the progress of the computation.





<br>

#### Progress Bars and Percentage Indicators

![Screenshot of PyPrind executed in an IPython notebook](https://raw.githubusercontent.com/rasbt/pyprind/master/images/overview_1.png)

<br>
<br>

<a id='advanced_tracking'>

#### Advanced Tracking

![Screenshot of PyPrind executed in an IPython notebook](https://raw.githubusercontent.com/rasbt/pyprind/master/images/overview_2.png)

#### Choose Your Favorite Bar Style
![Screenshot of PyPrind executed in an IPython notebook](https://raw.githubusercontent.com/rasbt/pyprind/master/images/overview_3.png)


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



PyPrind comes without any dependencies except for the optional [psutil](https://pypi.python.org/pypi/psutil) to [monitor CPU and memory usages](#advanced_tracking). You can install `psutil` via `pip install pyprind` or install it automatically with PyPrind:  
 `pip install pyprind -r requirements.txt`



Alternatively, you can install PyPrind the classic way: Download the package from the Python Package Index [https://pypi.python.org/pypi/PyPrind](https://pypi.python.org/pypi/PyPrind), unzip it, navigate into the unzipped directory, and use the command

`python setup.py install`  




<p><a id="documentation"></a></p>
<br>
<br>
<br>

# Documentation

[[back to top](#sections)]



PyPrind consists of two class objects that can visualize the progress of a computation on the output screen.  
Progress bars are available via `ProgBar`, and percentage indicators can be used via a `ProgPercent`.  

	n = 10000000
	bar = pyprind.ProgBar(n)   # 1) initialization with number of iterations
	for i in range(n):
    	# do some computation
    	bar.update()           # 2) update the progress visualization

Alternatively, the progress can be tracked via the equivalent generator functions `prog_bar` and `prog_percent`:

	for i in pyprind.prog_bar(range(n)):
    	# do something
    	pass

<br>

#### Complete Parameter List for ProgBar Objects

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

<br>

#### Complete Parameter List for ProgPercent Objects

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


<p><a id="examples"></a></p>

<br>
<br>
<br>

# Examples

[[back to top](#sections)]

Examples for using the progress bar and percentage indicator objects can be found in the [IPython Demo Notebook](http://nbviewer.ipython.org/github/rasbt/pyprind/blob/master/examples/pyprind_demo.ipynb).

<p><a id="contact"></a></p>

<br>
<br>
<br>




#  Contact

[[back to top](#sections)]

If you have any questions or comments about `PyPrind`, please feel free to contact me via  
eMail: [mail@sebastianraschka.com](mailto:mail@sebastianraschka.com)  
or Twitter: [@rasbt](https://twitter.com/rasbt)


The `pyprind` module is available on GitHub at [https://github.com/rasbt/pyprind](https://github.com/rasbt/pyprind).
