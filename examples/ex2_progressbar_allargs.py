# Sebastian Raschka 01/25/2014
# Progress Bar Examples 

import pyprind


def example_2():
    n = 1000000
    my_bar = pyprind.ProgBar(n, stream=1, track_time=True)
    for i in range(n):
        # do some computation
        my_bar.update()
    print('Print elapsed time again ...')
    print(my_bar)

if __name__ == '__main__':
    example_2()
         

