from distutils.core import setup

setup(name='PyPrind',
      version='1.1.1',
      description='Python Progress Indicator Utility',
      author='Sebastian Raschka',
      author_email='se.raschka@gmail.com',
      url='https://github.com/rasbt/pyprind',
      packages=['pyprind'],
      data_files = [('', ['LICENSE.txt']),
                    ('', ['README.html']),
                    ('', ['README.txt']),
                    ('', ['CHANGELOG.txt']),
                    ('examples', ['examples/ex1_percentage_indicator.py']),
                    ('examples', ['examples/ex1_progress_bar.py']),
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
 


 Contact
=============

If you have any questions or comments about PyPrind, please feel free to contact me via  
eMail: [se.raschka@gmail.com](mailto:se.raschka@gmail.com)  
or Twitter: [@rasbt](https://twitter.com/rasbt)

""",
    )
