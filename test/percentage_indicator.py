import sys
import pyprind

print('\n%s' % (80 * '='))
print('%s\n' % (80 * '='))
print('Testing Basic Percentage Indicator\n')

n = 100000
perc = pyprind.ProgPercent(n)
for i in range(n):
    perc.update()

 
print('\n%s' % (80 * '='))
print('%s\n' % (80 * '='))
print('Testing stdout Stream\n')

perc = pyprind.ProgPercent(n, stream=sys.stdout)
for i in range(n):
    perc.update()


print('\n%s' % (80 * '='))
print('%s\n' % (80 * '='))
print('Testing Percentage Indicator Generator\n')

for i in pyprind.prog_percent(range(n), stream=sys.stdout):
    # do something
    pass


print('\n%s' % (80 * '='))
print('%s\n' % (80 * '='))
print('Testing monitor function\n')

perc = pyprind.ProgPercent(n, monitor=True)
for i in range(n):
    perc.update()
print(perc)


print('\n%s' % (80 * '='))
print('%s\n' % (80 * '='))
print('Testing Item Tracking\n')

items = ['file_%s.csv' %i for i in range(0,n)]
perc = pyprind.ProgPercent(len(items))
for i in items:
    # do some computation
    perc.update(item_id=i)
