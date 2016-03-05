"""
Sebastian Raschka 2014-2016
Python Progress Indicator Utility

Author: Sebastian Raschka <sebastianraschka.com>
License: BSD 3 clause

Contributors: https://github.com/rasbt/pyprind/graphs/contributors
Code Repository: https://github.com/rasbt/pyprind
PyPI: https://pypi.python.org/pypi/PyPrind
"""

import sys
import time
import pyprind

n = 100
sleeptime = 0.02


def test_basic_percent():
    perc = pyprind.ProgPercent(n)
    for i in range(n):
        time.sleep(sleeptime)
        perc.update()


def test_stdout():
    perc = pyprind.ProgPercent(n, stream=sys.stdout)
    for i in range(n):
        time.sleep(sleeptime)
        perc.update()


def test_generator():
    for i in pyprind.prog_percent(range(n), stream=sys.stdout):
        time.sleep(sleeptime)


def test_monitoring():
    perc = pyprind.ProgPercent(n, monitor=True)
    for i in range(n):
        time.sleep(sleeptime)
        perc.update()
    print(perc)


def test_item_tracking():
    items = ['file_%s.csv' % i for i in range(0, n)]
    perc = pyprind.ProgPercent(len(items))
    for i in items:
        time.sleep(sleeptime)
        perc.update(item_id=i)


def test_force_flush():
    perc = pyprind.ProgPercent(n)
    for i in range(n):
        time.sleep(sleeptime)
        perc.update(force_flush=True)


def test_update_interval():
    perc = pyprind.ProgPercent(n, update_interval=4)
    for i in range(n):
        time.sleep(sleeptime)
        perc.update()


if __name__ == "__main__":
    print('\n%s' % (80 * '='))
    print('%s\n' % (80 * '='))
    print('Testing Basic Percentage Indicator\n')
    test_basic_percent()

    print('\n%s' % (80 * '='))
    print('%s\n' % (80 * '='))
    print('Testing stdout Stream\n')
    test_stdout()

    print('\n%s' % (80 * '='))
    print('%s\n' % (80 * '='))
    print('Testing Percentage Indicator Generator\n')
    test_generator()

    print('\n%s' % (80 * '='))
    print('%s\n' % (80 * '='))
    print('Testing monitor function\n')
    test_monitoring()

    print('\n%s' % (80 * '='))
    print('%s\n' % (80 * '='))
    print('Testing Item Tracking\n')
    test_item_tracking()

    print('\n%s' % (80 * '='))
    print('%s\n' % (80 * '='))
    print('Testing Force Flush\n')
    test_force_flush()

    print('\n%s' % (80 * '='))
    print('%s\n' % (80 * '='))
    print('Testing Update Interval\n')
    test_update_interval()
