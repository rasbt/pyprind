import sys
sys.path = ['/Users/Sebastian/Dropbox/_ot/code/pyprind'] + sys.path

import sys
import time
import pyprind

print('\n%s' % (80 * '='))
print('%s\n' % (80 * '='))
print('Testing Basic Progress Bar\n')

#n = 10000000
#sleeptime = 0.1
n = 100
sleeptime = 0.02

bar = pyprind.ProgBar(n)
for i in range(n):
    time.sleep(sleeptime)
    bar.update()

print('\n%s' % (80 * '='))
print('%s\n' % (80 * '='))
print('Testing stdout Stream\n')

bar = pyprind.ProgBar(n, stream=sys.stdout)
for i in range(n):
    time.sleep(sleeptime)
    bar.update()


print('\n%s' % (80 * '='))
print('%s\n' % (80 * '='))
print('Testing Progress Bar Generator\n')

for i in pyprind.prog_bar(range(n), stream=sys.stdout):
    time.sleep(sleeptime)


print('\n%s' % (80 * '='))
print('%s\n' % (80 * '='))
print('Testing monitor function\n')

bar = pyprind.ProgBar(n, monitor=True)
for i in range(n):
    time.sleep(sleeptime)
    bar.update()
print(bar)
print('\n%s' % (80 * '='))
print('%s\n' % (80 * '='))
print('Testing Width Parameter\n')

bar = pyprind.ProgBar(n, width=10)
for i in range(n):
    time.sleep(sleeptime)
    bar.update()

print('\n%s' % (80 * '='))
print('%s\n' % (80 * '='))
print('Testing Item Tracking\n')

items = ['file_%s.csv' % i for i in range(0, n)]
bar = pyprind.ProgBar(len(items))
for i in items:
    time.sleep(sleeptime)
    bar.update(item_id=i)

print('\n%s' % (80 * '='))
print('%s\n' % (80 * '='))
print("Testing Progress Bar Character ('>', default: '#')\n")

bar = pyprind.ProgBar(n, bar_char='>')
for i in range(n):
    time.sleep(sleeptime)
    bar.update()
