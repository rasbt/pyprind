import sys
import pyprind

print('\n%s' % (80 * '='))
print('%s\n' % (80 * '='))
print('Testing Basic Progress Bar\n')

n = 100000
bar = pyprind.ProgBar(n)
for i in range(n):
    bar.update()

print('\n%s' % (80 * '='))
print('%s\n' % (80 * '='))
print('Testing stdout Stream\n')

bar = pyprind.ProgBar(n, stream=sys.stdout)
for i in range(n):
    bar.update()


print('\n%s' % (80 * '='))
print('%s\n' % (80 * '='))
print('Testing Progress Bar Generator\n')

for i in pyprind.prog_bar(range(n), stream=sys.stdout):
    # do something
    pass


print('\n%s' % (80 * '='))
print('%s\n' % (80 * '='))
print('Testing monitor function\n')

bar = pyprind.ProgBar(n, monitor=True)
for i in range(n):
    bar.update()
print(bar)
print('\n%s' % (80 * '='))
print('%s\n' % (80 * '='))
print('Testing Width Parameter\n')

bar = pyprind.ProgBar(n, width=10)
for i in range(n):
    bar.update()

print('\n%s' % (80 * '='))
print('%s\n' % (80 * '='))
print('Testing Item Tracking\n')

items = ['file_%s.csv' % i for i in range(0, n)]
bar = pyprind.ProgBar(len(items))
for i in items:
    # do some computation
    bar.update(item_id=i)

print('\n%s' % (80 * '='))
print('%s\n' % (80 * '='))
print("Testing Progress Bar Character ('>', default: '#')\n")

bar = pyprind.ProgBar(n, bar_char='>')
for i in range(n):
    bar.update()
