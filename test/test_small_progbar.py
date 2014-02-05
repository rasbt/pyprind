import pyprind as ppr

n = 1000
mbar = ppr.ProgBar(n)
for i in range(n):
    mbar.update()

print('\n\nshort progress bar')

n = 1
mbar2 = ppr.ProgBar(n)
for i in range(n):
    mbar2.update()

