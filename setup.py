from distutils.core import setup

setup(name='PyPrind',
      version='2.1.1',
      description='Python Progress Indicator Utility',
      author='Sebastian Raschka',
      author_email='se.raschka@gmail.com',
      url='https://github.com/rasbt/pyprind',
      packages=['pyprind'],
      data_files = [('', ['LICENSE.txt']),
                    ('', ['README.html']),
                    ('', ['README.txt']),
                    ('', ['CHANGELOG.txt']),
                    ('examples', ['examples/ex1_percentage_indicator_stderr.py']),
                    ('examples', ['examples/ex1_percentage_indicator_stdout.py']),
                    ('examples', ['examples/ex1_progress_bar_stderr.py']),
                    ('examples', ['examples/ex1_progress_bar_stdout.py']),

                   ],
      license='GPLv3',
      platforms='any',
      classifiers=[
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Environment :: Console',
      ],
      long_description="""

The PyPrind (Python Progress Indicator) module provides a progress bar and a percentage indicator  
object that let you track the progress of a loop structure or other iterative computation.  
Typical applications include the processing of large data sets to provide an intuitive estimate 
at runtime about the progress of the computation.





Examples
=============

The following examples shall illustrate the typical usage of the PyPrind package.  
A visualization can be viewed on YouTube: [http://youtu.be/gjj5K8OWo7U](http://youtu.be/gjj5K8OWo7U)


Example - Progress Bar
--------------------------

<pre>import pypr<pre>sebastian > python3 ./examples/ex1_percentage_indicator.py 
[ 12 %]   elapsed: 2.095 sec | eta: 16.000 sec
</pre>
ind

n = 10000000
my_prbar = pyprind.ProgBar(n)
for i in range(n):
    # do some computation
    my_prbar.update()
</pre>

**Screen Output**  

<pre>sebastian > python3 ./examples/ex1_progress_bar.py 
0%                                    100%
[########################################]
Total time elapsed: 1.033 sec
</pre>


Example - Percentage Indicator
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
[ 17 %]   elapsed [sec]: 3.066  | ETA [sec]: 15.000
</pre>


#### Default Parameters

	ProgBar(iterations, track_time=True, width=50, stream=2):
	
		iterations (int): number of iterations of the computation
        track_time (bool): prints elapsed time when loop has finished
        stream: takes 1 for stdout, 2 for stderr, or given stream object


	ProgPercent(iterations, track_time=True, stream=2):
		
		iterations (int): number of iterations of the computation
        width (int): width of the progress bar in characters
        track_time (bool): prints elapsed time and estimated time left
        stream: takes 1 for stdout, 2 for stderr, or given stream object


**VERSION 2.1.0**

- changed visuals of the printed progress for percentage indicators  

**VERSION 2.1.0**

- added ETA (estimated time until arrival) tracking by Taylan Aydinli  

**VERSION 2.0.3**

- Accepts a given outputstream for the `stream` parameter.   

**VERSION 2.0.0**

- ProgBar and ProgPerc inherit data members from parent class Prog
- Added ProgBar and ProgPerc default argument `stream=2` to write to stderr by
  default. Set `stream=1` to write to stdout.

    my_prbar = pyprind.ProgBar(n, stream=1) # writes to stdout
    my_prbar = pyprind.ProgBar(n, stream=2) # writes to stderr, default


- Does not redirect data to the standard output or error stream if program is not
  outputting to a terminal



 Contact
=============

If you have any questions or comments about PyPrind, please feel free to contact me via  
eMail: [se.raschka@gmail.com](mailto:se.raschka@gmail.com)  
or Twitter: [@rasbt](https://twitter.com/rasbt)

""",
    )
