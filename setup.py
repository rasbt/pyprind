from distutils.core import setup

setup(name='PyPrind',
      version='1.0.4',
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
                    ('examples', ['examples/ex2_bad_progress_bar.py']),
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
PyPrind
=============
The PyPrind (Python Progress Indicator) module provides a progress bar and a 
percentage indicator object that let you track the progress of a loop  
structure or other iterative computation.  
Typical applications include the processing of large data sets to provide 
an intuitive estimate at runtime about the progress of the computation.



Example - Progress Bar
--------------------------

    import pyprind

    n = 10000000
    my_prbar = pyprind.ProgBar(n)
    for i in range(n):
        # do some computation
        my_prbar.update()
    my_prbar.finish() 

**Screen Output**  

sebastian > python3 examples/ex_progress_bar.py 
0%                                    100%
[########################################]
Time elapsed: 0.7829 sec
""",
    )
