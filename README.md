# PyPrind
The PyPrind (Python Progress Indicator) module lets you visualize the progress of a programming task in Python via a progress bar or a percentage indicator.


<br>
<br>


## Installation
You can use the following command to install PyPrind:  
`pip install pyprind`

Or you download the package manually, unzip it, and install it from the package folder via:

`python setup.py install`
or
`python3 setup.py install`

<br>
<br>

## Documentation

PyPrind consists of two class objects that can visualize the progress of a computation on the output screen.  
Progress bars are visualized via  a `ProgBar()` object, and alternatively, the progress can be shown as an percentage via the `ProgPercent()` object.  

The general usage of `ProgBar()` and ProgPercent()` consists of three steps:

1) initialize a new `ProgBar()` or `ProgPercent()` object with the number of iterations of the computation that is to be performed  
2) update the `ProgBar()` or `ProgPercent()`  object for each iteration via the `.update() `method  
3) complete the progress visualization via the `.finish()` method after the computation is completed  

<pre>
n = 10000000
my_progress = pyprind.ProgBar(n)      # 1) initialization with number of iterations
for i in range(n):	
    # do some computation
    my_prbar.update()           # 2) update the progress visualization
my_prbar.finish()               # 3) complete the progress visualization
</pre>

<br>
### Optional parameters :
<br>
##### Setting the width of the progress bar

`my_prog = pyrpind.ProgBar(width=70)	# default = 50`

<br>
##### Set whether CPU time should be reported or not 
The optional `cpu_time` parameter can be set for both `ProgBar()` and `ProgPercent()` objects.  
E.g.,   
`my_prog.finish(cpu_time=False) # (default = True)`

<br>
<br>

## Examples

The following examples shall illustrate the typical usage of the PyPrind package.  
An visualization can be viewed on YouTube: [http://youtu.be/gjj5K8OWo7U](http://youtu.be/gjj5K8OWo7U)

<br>
### Example - Progress Bar

<pre>import pyprind

n = 10000000
my_prbar = pyprind.ProgBar(n)
for i in range(n):
    # do some computation
    my_prbar.update()
my_prbar.finish() </pre>

####Screen Output:

<pre>sebastian > ./python3 examples/ex_percentage_indicator.py 
[100 %]
Time elapsed: 2.6364 sec
</pre>

<br>

### Example - Percentage Indicator  
<pre>import pyprind

n = 1000000
my_perc = pyprind.ProgPercent(n)
for i in range(n):
    # do some computation
    my_perc.update()
my_perc.finish() </pre>

####Screen Output

<pre>sebastian > python3 examples/ex_progress_bar.py 
0%                                    100%
[########################################]
Time elapsed: 0.7829 sec
</pre>
 
<br>
<br>
## Contact

If you have any questions or comments about PyPrind, please feel free to contact me via  
eMail: [se.raschka@gmail.com](mailto:se.raschka@gmail.com)  
or Twitter: [https://twitter.com/rasbt](@rasbt)