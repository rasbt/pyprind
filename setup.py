from distutils.core import setup

setup(name='PyPrind',
      version='2.0.1',
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
[100 %]   elapsed: 2.674 sec
</pre>


 

Changes in Version 2.0.0
==========================
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
