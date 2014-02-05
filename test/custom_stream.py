import sys
import pyprind

n= 1000000
mbar = pyprind.ProgBar(n, stream=sys.stdout)

for i in range(n):
    mbar.update()

mper = pyprind.ProgPercent(n, stream=sys.stdout)
for i in range(n):
    mper.update()

mbar2 = pyprind.ProgBar(n, stream='test')
for i in range(n):
    mbar2.update()

