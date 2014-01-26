from distutils.core import setup

setup(name='PyPrind',
      version='1.0.0',
      description='Python Progress Indicator Utility',
      author='Sebastian Raschka',
      author_email='se.raschka@gmail.com',
      url='https://github.com/rasbt/pyprind',
      packages=['pyprind'],
      data_files = [('', ['LICENSE.txt']),],
      license='GPLv3',
      #long_description = read('README.rst'),
      extras_require={'testing': ['pytest']},
      platforms='any',
    )
