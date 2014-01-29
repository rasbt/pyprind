# Sebastian Raschka 01/25/2014
# Progress Bar Examples 

import pyprind


def example_1():
    n = 1000000
    my_bar = pyprind.ProgBar(n, width=40)
    for i in range(n):
       my_bar.update()
    my_bar.finish() 


if __name__ == '__main__':
    example_1() 

