from distutils.core import setup

setup(name='PyPrind',
      version='2.2.0',
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

For more details and examples please see the package documentation.

A short video demonstration of the progress tracking can be found on YouTube:
http://youtu.be/Ex05RM9vLKE


 Contact
=============

If you have any questions or comments about PyPrind, please feel free to contact me via
eMail: se.raschka@gmail.com
or Twitter: https://twitter.com/rasbt

""",
    )
