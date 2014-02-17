PyPrind
=============
The PyPrind (Python Progress Indicator) module provides a progress bar and a percentage indicator  
object that let you track the progress of a loop structure or other iterative computation.  
Typical applications include the processing of large data sets to provide an intuitive estimate 
at runtime about the progress of the computation.


####Sections
<p><a href="#installation">Installation</a><br>
<p><a href="#documentation">Documentation</a><br>
<p><a href="#options">Optional Parameters</a><br>
<p><a href="#examples">Examples</a><br>
<p><a href="#contact">Contact</a><br>
<p><a href="#changelog">Changelog</a><br>


<p><a name="installation"></a></p>

Installation
=============
You can use the following command to install PyPrind:  
`pip install pyprind`  
 or    
`easy_install pyprind`  

Alternatively, you download the package manually from the Python Package Index [https://pypi.python.org/pypi/PyPrind](https://pypi.python.org/pypi/PyPrind), unzip it, navigate into the package, and use the command:

`python setup.py install`  
or  
`python3 setup.py install`  



<p><a name="documentation"></a></p>

Documentation
=============
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

Optional parameters :
--------------------------

#### Default Parameters

	ProgBar(iterations, track_time=True, width=30, stream=2, title='')	
		
        iterations (int): number of iterations of the computation
        track_time (bool): prints elapsed time when loop has finished
        width (int): sets the progress bar width in characters.
        stream: takes 1 for stdout, 2 for stderr, or given stream object
        title (str): A title for the progress bar


	ProgPercent(iterations, track_time=True, stream=2, title=''):
		
		iterations (int): number of iterations of the computation
        width (int): width of the progress bar in characters
        track_time (bool): prints elapsed time and estimated time left
        stream: takes 1 for stdout, 2 for stderr, or given stream object
        title (str): A title for the percent indicator



##### Setting the width of the progress bar

`my_prog = pyprind.ProgBar(n, width=70)	# default = 50`


##### Set whether CPU time should be reported or not 
The optional `track_time` parameter can be set for both `ProgBar()` and `ProgPercent()` objects.   

`my_prbar = pyprind.ProgBar(n, track_time=False)  # default = True`  
`my_perc = pyprind.ProgPercent(n, track_time=False)  # default = True`  

`ProgBar` objects will print the estimated time left and the total time  
when the computation has finished.  
`ProgPercent` objects reports the elapsed time during the computation and prints  
the estimated finish time of the loop.   


##### Selecting an output stream  
By default, `pyprind` objects writes output to the Standard error stream (`stderr`). If you  
want to direct the output to the Standard output (`stdout`), you can initialize `pyprind` 
with the argument `stream=2`.

<pre>
my_prbar = pyprind.ProgBar(n, stream=1) # writes to stdout
my_prbar = pyprind.ProgBar(n, stream=2) # writes to stderr, default
</pre>

***If you want to use a given stream, just pass that. Example:***
<pre>
my_prbar = pyprint.ProgBar(n, stream=self.stdout)  # writes to given stream
</pre>


##### Givin a tracking object a title
If a tracking object is initialized with a title, it is printed when a new tracking  
object is initialized.
The title and elapsed time can be printed via the `print()` function after the tracking has finished.

<pre>
my_prbar = pyprint.ProgBar(n, title='My Progress Bar')

Screen output:
My Progress Bar
0%                          100%
[##############################] | ETA [sec]: 0.000 sec

</pre>

##### Printing a tracking object
The `print()` method can be invoked after the tracking is completed to  
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
[##############################] | ETA [sec]: 0.000 sec 
Title: My Progress Bar
Total time elapsed: 4.049 sec


Print tracking object ...

Title: My Progress Bar
Total time elapsed: 4.049 sec

</pre>

##### Small note on usage in a custom Django management command.
Django gives you a stdout object on the BaseCommand class. You will need to pass this to
`pyprind` as done above. Also note that by default, Django appends a newline to every write.
This uglyfies `pyprind` output, so ensure the write function gets passed `ending=""`.
`pyprind` will NOT do this for you.


<p><a name="examples"></a></p>

Examples
=============

The following examples shall illustrate the typical usage of the PyPrind package.  
A visualization can be viewed on YouTube: [http://youtu.be/Ex05RM9vLKE](http://youtu.be/Ex05RM9vLKE)


Example - Progress Bar (simple)
--------------------------

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
[########################################] - ETA [sec]: 0.000 sec  
Total time elapsed: 4.481 sec
</pre>


Example - Percentage Indicator (simple)
--------------------------

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


Example - Progress Bar (all arguments)
--------------------------

<pre>import pyprind
n = 1000000
    my_bar = pyprind.ProgBar(n, stream=1, width=30, track_time=True, title='My Progress Bar')
    for i in range(n):
        # do some computation
        my_bar.update()
    print('\n\nPrint tracking object ...\n')
    print(my_bar)
</pre>
 
**Screen Output**  
<pre>My Progress Bar
0%                          100%
[##############################] | ETA [sec]: 0.000 sec 
Title: My Progress Bar
Total time elapsed: 4.049 sec


Print trackin object ...

Title: My Progress Bar
Total time elapsed: 4.049 sec
</pre>


Example - Percent Indicator (all arguments)
--------------------------

<pre>import pyprind
n = 1000000
    my_per = pyprind.ProgPercent(n, stream=1, track_time=True, title='My Percent Indicator')
    for i in range(n):
        # do some computation
        my_per.update()
    print('\n\nPrint tracking object ...\n')
    print(my_per)
</pre>
 
**Screen Output**  
<pre>My Percent Indicator
[100 %] elapsed [sec]: 4.205 | ETA[sec]: 0.000 
Title: My Percent Indicator
Total time elapsed: 4.206 sec


Print tracking object ...

Title: My Percent Indicator
Total time elapsed: 4.206 sec
</pre>


<p><a name="contact"></a></p>

 Contact
=============

If you have any questions or comments about PyPrind, please feel free to contact me via  
eMail: [se.raschka@gmail.com](mailto:se.raschka@gmail.com)  
or Twitter: [@rasbt](https://twitter.com/rasbt)


<br>
<br>

<p><a name="changelog"></a></p>

Changelog
==========

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

