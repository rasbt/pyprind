from distutils.core import setup

readme = open('README.rst', 'r')
README_TEXT = readme.read()
readme.close()


setup(name='PyPrind',
      version='1.0.0',
      description='Python Progress Indicator Utility',
      author='Sebastian Raschka',
      author_email='se.raschka@gmail.com',
      url='https://github.com/rasbt/pyprind',
      packages=['pyprind'],
      data_files = [('', ['LICENSE.txt']),
                    ('', ['README.rst']),
                    ('', ['README.md']),
                   ],
      license='GPLv3',
      long_description = README_TEXT,
      extras_require={'testing': ['pytest']},
      platforms='any',
    )
