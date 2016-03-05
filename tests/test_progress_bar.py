import sys
import time
import pyprind


n = 100
sleeptime = 0.02


def test_bar():
    bar = pyprind.ProgBar(n)
    for i in range(n):
        time.sleep(sleeptime)
        bar.update()


def test_stdout():
    bar = pyprind.ProgBar(n, stream=sys.stdout)
    for i in range(n):
        time.sleep(sleeptime)
        bar.update()


def test_generator():
    for i in pyprind.prog_bar(range(n), stream=sys.stdout):
        time.sleep(sleeptime)


def test_monitoring():
    bar = pyprind.ProgBar(n, monitor=True)
    for i in range(n):
        time.sleep(sleeptime)
        bar.update()
    print(bar)


def test_width():
    bar = pyprind.ProgBar(n, width=10)
    for i in range(n):
        time.sleep(sleeptime)
        bar.update()


def test_item_tracking():
    items = ['file_%s.csv' % i for i in range(0, n)]
    bar = pyprind.ProgBar(len(items))
    for i in items:
        time.sleep(sleeptime)
        bar.update(item_id=i)


def test_character():
    bar = pyprind.ProgBar(n, bar_char='>')
    for i in range(n):
        time.sleep(sleeptime)
        bar.update()


def test_force_flush():
    bar = pyprind.ProgBar(n)
    for i in range(n):
        time.sleep(sleeptime)
        bar.update(force_flush=True)


def test_update_interval():
    bar = pyprind.ProgBar(n, update_interval=0.1)
    for i in range(n):
        time.sleep(sleeptime)
        bar.update()


if __name__ == '__main__':

    print('\n%s' % (80 * '='))
    print('%s\n' % (80 * '='))
    print('Testing Basic Progress Bar\n')
    test_bar()

    print('\n%s' % (80 * '='))
    print('%s\n' % (80 * '='))
    print('Testing stdout Stream\n')
    test_stdout()

    print('\n%s' % (80 * '='))
    print('%s\n' % (80 * '='))
    print('Testing Progress Bar Generator\n')
    test_generator()

    print('\n%s' % (80 * '='))
    print('%s\n' % (80 * '='))
    print('Testing monitor function\n')
    test_monitoring()

    print('\n%s' % (80 * '='))
    print('%s\n' % (80 * '='))
    print('Testing Width Parameter\n')
    test_width()

    print('\n%s' % (80 * '='))
    print('%s\n' % (80 * '='))
    print('Testing Item Tracking\n')
    test_item_tracking()

    print('\n%s' % (80 * '='))
    print('%s\n' % (80 * '='))
    print("Testing Progress Bar Character ('>', default: '#')\n")
    test_character()

    print('\n%s' % (80 * '='))
    print('%s\n' % (80 * '='))
    print('Testing Force Flush\n')
    test_force_flush()

    print('\n%s' % (80 * '='))
    print('%s\n' % (80 * '='))
    print('Testing Update Interval\n')
    test_update_interval()
