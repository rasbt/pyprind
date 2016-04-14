"""
Sebastian Raschka 2014-2016
Python Progress Indicator Utility

Author: Sebastian Raschka <sebastianraschka.com>
License: BSD 3 clause

Contributors: https://github.com/rasbt/pyprind/graphs/contributors
Code Repository: https://github.com/rasbt/pyprind
PyPI: https://pypi.python.org/pypi/PyPrind
"""


from setuptools import setup, find_packages
import pyprind

VERSION = pyprind.__version__

setup(name='PyPrind',
      version=VERSION,
      description='Python Progress Bar and Percent Indicator Utility',
      author='Sebastian Raschka',
      author_email='mail@sebastianraschka.com',
      url='https://github.com/rasbt/pyprind',
      packages=find_packages(),
      package_data={'': ['LICENSE',
                         'README.md',
                         'requirements.txt',
                         'CHANGELOG.md',
                         'CONTRIBUTING.md'],
                    'tests': ['tests/test_percentage_indicator.py',
                              'tests/test_progress_bar.py']},
      include_package_data=True,
      license='BSD 3-Clause',
      platforms='any',
      classifiers=[
          'License :: OSI Approved :: BSD License',
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Environment :: Console'],
      long_description="""

The PyPrind (Python Progress Indicator) module provides a progress
bar and a percentage indicator
object that let you track the progress of a loop structure or
other iterative computation.
Typical applications include the processing of
large data sets to provide an intuitive estimate
at runtime about the progress of the computation.

For more details and examples please see the package documentation
https://github.com/rasbt/pyprind/blob/master/README.md.

Contact
=============

If you have any questions or comments about PyPrind,
please feel free to contact me via
email: mail@sebastianraschka.com
or Twitter: https://twitter.com/rasbt""",)
