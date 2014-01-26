from distutils.core import setup

readme = open('README.txt', 'r')
README_TEXT = readme.read()
readme.close()


setup(name='PyPrind',
      version='1.0.1dev',
      description='Python Progress Indicator Utility',
      author='Sebastian Raschka',
      author_email='se.raschka@gmail.com',
      url='https://github.com/rasbt/pyprind',
      packages=['pyprind'],
      data_files = [('', ['LICENSE.txt']),
                    ('', ['README.html']),
                    ('', ['README.txt']),
                    ('', ['CHANGELOG.txt']),
                    ('examples', ['examples/ex_percentage_indicator.py']),
                    ('examples', ['examples/ex_progress_bar.py']),
                   ],
      license='GPLv3',
      long_description = README_TEXT,
      platforms='any',
    )
