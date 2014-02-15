# Sebastian Raschka 01/25/2014
# Progress Bar Examples 

import pyprind


def example_1():
    n = 10000000
    my_bar = pyprind.ProgBar(n, width=40, stream=2)
    for i in range(n):
        my_bar.update()


if __name__ == '__main__':
    example_1() 

