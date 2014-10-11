# PyPrind (Python Progress Indicator)


The `PyPrind` (Python Progress Indicator) module provides a **progress bar** and a **percentage indicator** object that let you track the progress of a loop structure or other iterative computation.  
Typical applications include the processing of large data sets to provide an intuitive estimate 
at runtime about the progress of the computation.





<br>

![Screenshot from iPython notebook](https://raw.githubusercontent.com/rasbt/pyprind/master/images/overview.png)

- [Open an IPython Demo Notebook in nbviewer](http://nbviewer.ipython.org/github/rasbt/pyprind/blob/master/examples/pyprind_demo.ipynb)

<br>
**Example demonstration videos:**  
  
- [in a terminal shell](http://youtu.be/iWjSGe89Pvs)  
- [in an IPython Notebook](http://youtu.be/XXy-fslQ09g)

<br>
<br>


<a id='sections'>
## Sections


- [Installation](#installation)
- [More Examples](#examples)
- [Documentation](#documentation)
- [Optional Parameters](#options)
- [Contact](#contact)
- [Changelog](#changelog)


<br>
<br>
<br>

<p><a name="installation"></a></p>
<br>
<br>
<br>

## Installation
[[back to top](#sections)]

You can use the following command to install PyPrind:  
`pip install pyprind`  
 or    
`easy_install pyprind`  

Alternatively, you download the package manually from the Python Package Index [https://pypi.python.org/pypi/PyPrind](https://pypi.python.org/pypi/PyPrind), unzip it, navigate into the package, and use the command:

`python setup.py install`  
or  
`python3 setup.py install`  



<p><a name="documentation"></a></p>
<br>
<br>
<br>

## Documentation
[[back to top](#sections)]

PyPrind consists of two class objects that can visualize the progress of a computation on the output screen.  
Progress bars are visualized via  a `ProgBar()` object, and alternatively, the progress can be tracked and shown as percentage via a `ProgPercent()` object.  

The general usage of `ProgBar()` and `ProgPercent()` consists of 2 basic steps:

1) initialize a new `ProgBar()` or `ProgPercent()` object with the number of iterations of the computation that is to be performed  
2) update the `ProgBar()` or `ProgPercent()`  object for each iteration via the `.update() `method  


<pre>n = 10000000
my_prbar = pyprind.ProgBar(n)   # 1) initialization with number of iterations
for i in range(n):	
    # do some computation
    my_prbar.update()           # 2) update the progress visualization
</pre>


<p><a name="optional"></a></p>
<br>
<br>
<br>




#### Default Parameters
[[back to top](#sections)]

<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">class</span> <span style="color: #BB0066; font-weight: bold">ProgBar</span>(Prog):
    <span style="color: #DD4422">&quot;&quot;&quot;</span>
<span style="color: #DD4422">    Initializes a progress bar object that allows visuzalization</span>
<span style="color: #DD4422">    of an iterational computation in the standard output screen. </span>

<span style="color: #DD4422">    Keyword Arguments:</span>
<span style="color: #DD4422">        iterations (int): number of iterations of the computation</span>
<span style="color: #DD4422">        track_time (bool): default True. Prints elapsed time when loop has finished</span>
<span style="color: #DD4422">        width (int): default 30. Sets the progress bar width in characters.</span>
<span style="color: #DD4422">        stream (int): default 2. Takes 1 for stdout, 2 for stderr, or given stream object</span>
<span style="color: #DD4422">        title (str): default &#39;&#39;. A title for the progress bar</span>
<span style="color: #DD4422">        monitor (bool): default False. Monitors CPU and memory usage if True </span>
<span style="color: #DD4422">            (requires &#39;psutil&#39; package).</span>

<span style="color: #DD4422">    &quot;&quot;&quot;</span>
</pre></div>


<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">class</span> <span style="color: #BB0066; font-weight: bold">ProgPercent</span>(Prog):
    <span style="color: #DD4422">&quot;&quot;&quot;</span>
<span style="color: #DD4422">    Initializes a percentage indicator object that allows visuzalization</span>
<span style="color: #DD4422">    of an iterational computation in the standard output screen. </span>

<span style="color: #DD4422">    Keyword Arguments:</span>
<span style="color: #DD4422">        iterations (int): number of iterations of the computation</span>
<span style="color: #DD4422">        track_time (bool): default True. Prints elapsed time when loop has finished</span>
<span style="color: #DD4422">        stream (int): default 2. Takes 1 for stdout, 2 for stderr, or given stream object</span>
<span style="color: #DD4422">        title (str): default &#39;&#39;. A title for the progress bar</span>
<span style="color: #DD4422">        monitor (bool): default False. Monitors CPU and memory usage if True </span>
<span style="color: #DD4422">            (requires &#39;psutil&#39; package).</span>

<span style="color: #DD4422">    &quot;&quot;&quot;</span>
</pre></div>







<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">    <span style="color: #008800; font-weight: bold">def</span> <span style="color: #0066BB; font-weight: bold">update</span>(<span style="color: #007020">self</span>, iterations<span style="color: #333333">=</span><span style="color: #0000DD; font-weight: bold">1</span>):
        <span style="color: #DD4422">&quot;&quot;&quot;</span>
<span style="color: #DD4422">        Updates the progress bar in every iteration of the task.</span>

<span style="color: #DD4422">        Keyword arguments:</span>
<span style="color: #DD4422">            iterations (int): default argument can be changed to integer values</span>
<span style="color: #DD4422">                &gt;=1 in order to update the progress indicators more than once </span>
<span style="color: #DD4422">                per iteration.</span>

<span style="color: #DD4422">        &quot;&quot;&quot;</span>
</pre></div>

<br>
<br>
<br>

#### Setting the width of the progress bar
[[back to top](#sections)]

`my_prog = pyprind.ProgBar(n, width=70)	# default = 50`
<br>
<br>
<br>

#### Set whether CPU time should be reported or not 
[[back to top](#sections)]

The optional `track_time` parameter can be set for both `ProgBar()` and `ProgPercent()` objects.   

`my_prbar = pyprind.ProgBar(n, track_time=False)  # default = True`  
`my_perc = pyprind.ProgPercent(n, track_time=False)  # default = True`  

`ProgBar` objects will print the estimated time left and the total time  
when the computation has finished.  
`ProgPercent` objects reports the elapsed time during the computation and prints  
the estimated finish time of the loop.   
<br>
<br>
<br>

#### Selecting an output stream  
[[back to top](#sections)]

By default, `pyprind` objects writes output to the Standard error stream (`stderr`). If you  
want to direct the output to the Standard output (`stdout`), you can initialize `pyprind` 
with the argument `stream=2`.

<pre>
my_prbar = pyprind.ProgBar(n, stream=1) # writes to stdout
my_prbar = pyprind.ProgBar(n, stream=2) # writes to stderr, default
</pre>

***You can also just use a given stream by passing it directly:   
Example:***
<pre>
my_prbar = pyprind.ProgBar(n, stream=self.stdout)  # writes to given stream
</pre>

<br>
<br>
<br>
#### Giving a tracking object a title
[[back to top](#sections)]

If a tracking object is initialized with a title, it is printed when a new tracking  
object is initialized.
The title and elapsed time can be printed via the `print()` function after the tracking has finished.

<pre>
my_prbar = pyprind.ProgBar(n, title='My Progress Bar')

Screen output:
My Progress Bar
0%                          100%
[##############################] | ETA[sec]: 0.000

</pre>
<br>
<br>
<br>
#### Printing a tracking object
[[back to top](#sections)]

The `print()` function can be invoked after the tracking is completed to  
print the title and elapsed time to the screen.  

<pre>
n = 1000000
    my_bar = pyprind.ProgBar(n, title='My Progress Bar')
    for i in range(n):
        # do some computation
        my_bar.update()
    print('\n\nPrint tracking object ...\n')
    print(my_bar)

Screen output:

My Progress Bar
0%                          100%
[##############################] | ETA[sec]: 0.000 
Total time elapsed: 6.399 sec
Title: My Progress Bar
                      Started: 04/18/2014 19:12:07
                      Finished: 04/18/2014 19:12:14
                      Total time elapsed: 6.399 sec

</pre>

<br>
<br>
<br>
#### Printing a tracking object with CPU and memory usage
[[back to top](#sections)]

If we additionally want to `print()` the CPU and memory usage after a run has completed, 
we have to set the `monitor` argument to `True` when we initialize a new tracking object. (Note: the `monitor` mode requires the `psutil` package.)


<pre>
n = 1000000
    my_bar = pyprind.ProgBar(n, title='My Progress Bar', monitor=True)
    for i in range(n):
        # do some computation
        my_bar.update()
    print('\n\nPrint tracking object ...\n')
    print(my_bar)

Screen output:

My Progress Bar
0%                          100%
[##############################] | ETA[sec]: 0.000 
Total time elapsed: 6.391 sec
Title: My Progress Bar
                      Started: 04/18/2014 19:16:55
                      Finished: 04/18/2014 19:17:02
                      Total time elapsed: 6.391 sec
                      CPU %: 91.200000
                      Memory %: 0.098133
</pre>


#### Small note on usage in a custom Django management command.
[[back to top](#sections)]

Django gives you a stdout object on the BaseCommand class. You will need to pass this to
`pyprind` as done above. Also note that by default, Django appends a newline to every write.
This uglyfies `pyprind` output, so ensure the write function gets passed `ending=""`.
`pyprind` will NOT do this for you.


<p><a name="examples"></a></p>

<br>
<br>
<br>

## More Examples
[[back to top](#sections)]

A subset of examples is given in the section below, more examples can be found in this [IPython Demo Notebook](http://nbviewer.ipython.org/github/rasbt/pyprind/blob/master/examples/pyprind_demo.ipynb).

<br>
<br>
<br>

### Example - Progress Bar (simple)
[[back to top](#sections)]

<pre>import pyprind

n = 10000000
my_prbar = pyprind.ProgBar(n)
for i in range(n):
    # do some computation
    my_prbar.update()
</pre>

**Screen Output**  

<pre>sebastian > python3 ./examples/ex1_progress_bar.py 
0%                                    100%
[########################################] - ETA[sec]: 0.000  
Total time elapsed: 4.481 sec
</pre>

<br>
<br>
<br>

### Example - Percentage Indicator (simple)
[[back to top](#sections)]

<pre>import pyprind

n = 1000000
my_perc = pyprind.ProgPercent(n)
for i in range(n):
    # do some computation
    my_perc.update()
</pre>

**Screen Output**  

<pre>sebastian > python3 ./examples/ex1_percentage_indicator.py 
[ 34 %]   elapsed [sec]: 1.377  | ETA [sec]: 2.570
</pre>
<br>
<br>
<br>

### Example - Progress Bar (all arguments)
[[back to top](#sections)]

<pre>import pyprind
n = 1000000
    my_bar = pyprind.ProgBar(n, stream=1, width=30, track_time=True, title='My Progress Bar', monitor=True)
    for i in range(n):
        # do some computation
        my_bar.update()
    print(my_bar)
</pre>
 
**Screen Output**  
<pre>My Progress Bar
0%                          100%
[##############################] | ETA[sec]: 0.000 
Title: Progress Bar
                      Started: 04/18/2014 19:23:10
                      Finished: 04/18/2014 19:23:22
                      Total time elapsed: 11.272 sec
                      CPU %: 54.400000
                      Memory %: 0.098085
</pre>

<br>
<br>
<br>
### Example - Percent Indicator (all arguments)
[[back to top](#sections)]

<pre>import pyprind
n = 1000000
    my_per = pyprind.ProgPercent(n, stream=1, track_time=True, title='My Percent Indicator', monitor=True)
    for i in range(n):
        # do some computation
        my_per.update()
    print(my_per)
</pre>
 
**Screen Output**  
<pre>My Percent Indicator
[100 %] elapsed [sec]: 4.205 | ETA[sec]: 0.000 
Title: My Percent Indicator
                      Started: 04/18/2014 19:23:26
                      Finished: 04/18/2014 19:23:38
                      Total time elapsed: 11.775 sec
                      CPU %: 44.000000
                      Memory %: 0.097990
</pre>

<br>
<br>
<br>

##  Contact
[[back to top](#sections)]

If you have any questions or comments about `PyPrind`, please feel free to contact me via  
eMail: [se.raschka@gmail.com](mailto:se.raschka@gmail.com)  
or Twitter: [@rasbt](https://twitter.com/rasbt)


The `pyprind` module can be found on GitHub at [https://github.com/rasbt/pyprind](https://github.com/rasbt/pyprind)


<br>
<br>
<br>




## Changelog
[[back to top](#sections)]


**VERSION 2.6.2**

- Fixed bug that the report was squeezed after the bar and before the "time elapsed" string if printed immediately after the progress bar has reached 100%.

**VERSION 2.6.1**


- small bugfix on some system a warning was printed although
  a valid output string was provided



**VERSION 2.6.0**

- Added IPython Notebook support
- Fixed to work with most recent psutil v. 0.6 for monitoring CPU and memory usage


**VERSION 2.5.0**

- new default argument `monitor=False` was added to `ProgBar()` and `ProgPercent()` objects to monitor memory and CPU usage (via `psutil`) if `monitor` is set to True.
  

**VERSION 2.4.0**

- default argument for `.update(iterations=1)` methods to increment the count by more than 1 per
  iteration.


**VERSION 2.3.1**

- minor fix of the output formatting



**VERSION 2.3.0**

- added native print() support
  prints title and elapsed time of an tracked object after loop completed
- data member self.end stores elapsed time when loop completed
- data member self.title saves title of the tracking objects


**VERSION 2.2.0**

- added ETA (estimated time until arrival) tracking to progress bar  
  by Taylan Aydinli
- better support for Python 2.x


**VERSION 2.1.1**

- changed visuals of the printed progress for percentage indicators  


**VERSION 2.1.0**

- added ETA (estimated time until arrival) tracking by Taylan Aydinli  


**VERSION 2.0.3**

- Accepts a given outputstream for the `stream` parameter.  


**VERSION 2.0.2**  

- Fixed bug that occurred for some Python 3.3.3 users
specifically on Linux Red Hat 4.4.7-1, GCC v. 4.4.7
that self.max_iter was cast to a float when `ProgBar()`
object was seeded with n=48


**VERSION 2.0.1**  

- fixed packaging of example files


**VERSION 2.0.0**  

- ProgBar and ProgPerc inherit data members from parent class Prog
- Added ProgBar and ProgPerc default argument `stream=2` to write to stderr by
  default. Set `stream=1` to write to stdout.

    my_prbar = pyprind.ProgBar(n, stream=1) # writes to stdout
    my_prbar = pyprind.ProgBar(n, stream=2) # writes to stderr, default


- Does not redirect data to the standard output or error stream if program is not
  outputting to a terminal

 

**VERSION 1.1.1**  

- fixed problem with packaging of example scripts

**VERSION 1.1.0**  

- Added live time tracking to percentage indicator
- progress bar and percentage indicator complete automatically,
  .finish() was removed


**VERSION 1.0.4**  

- Added boundary that .update() can't print over the
  right progress bar limit.
- Prints warning when ProgBar seed exits the number of iterations
  in the loop.


**VERSION 1.0.3**  

- Reformatting of README files
- minor updates in setup.py file


**VERSION 1.0.2**  

- corrected errors in the README files
- added docstring to the __init__.py


**VERSION 1.0.1**  


- added more README formats
- added class descriptions
- added example scripts to the distribution

