from distutils.core import setup

setup(name='PyPrind',
      version='2.9.4',
      description='Python Progress Indicator Utility',
      author='Sebastian Raschka',
      author_email='mail@sebastianraschka.com',
      url='https://github.com/rasbt/pyprind',
      packages=['pyprind'],
      data_files=[('', ['LICENSE']),
                  ('', ['README.html']),
                  ('', ['CHANGELOG.md']),
                  ('examples', ['examples/ex1_percentage_indicator_stderr.py']),
                  ('examples', ['examples/ex1_percentage_indicator_stdout.py']),
                  ('examples', ['examples/ex1_progress_bar_stderr.py']),
                  ('examples', ['examples/ex1_progress_bar_stdout.py']),
                  ('examples', ['examples/ex2_percent_indicator_allargs.py']),
                  ('examples', ['examples/ex2_progressbar_allargs.py']),
                  ('examples', ['examples/ex3_percentage_indicator_monitor.py']),
                  ('examples', ['examples/ex3_progress_bar_monitor.py']),
                  ],
      license='New BSD',
      platforms='any',
      classifiers=[
          'License :: OSI Approved :: BSD License',
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

For more details and examples please see the package documentation
https://github.com/rasbt/pyprind/blob/master/README.md.

Contact
=============

If you have any questions or comments about PyPrind, please feel free to contact me via
email: mail@sebastianraschka.com
or Twitter: https://twitter.com/rasbt

""",)
