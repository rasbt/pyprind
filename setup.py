from distutils.core import setup

readme = open('README.txt', 'r')
README_TEXT = readme.read()
readme.close()


setup(name='PyPrind',
      version='1.0.1',
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
      platforms='any',
      classifiers=[
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Environment :: Console',
      ],
      long_description = README_TEXT,
    )
