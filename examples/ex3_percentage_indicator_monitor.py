# Sebastian Raschka 01/25/2014
# Percentage Indicator Examples 

import pyprind


def example_3():
    n = 1000000
    my_perc = pyprind.ProgPercent(n, stream=1, title='example3', monitor=True)
    for i in range(n):
        # do some computation
        my_perc.update()
    print(my_perc)

if __name__ == '__main__':
    example_3() 
