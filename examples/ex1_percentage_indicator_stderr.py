# Sebastian Raschka 01/25/2014
# Percentage Indicator Examples 

import pyprind


def example_1():
    n = 10000000
    my_perc = pyprind.ProgPercent(n, stream=2)
    for i in range(n):
        # do some computation
        my_perc.update()

if __name__ == '__main__':
    example_1() 

