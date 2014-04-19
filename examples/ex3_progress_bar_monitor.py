# Sebastian Raschka 01/25/2014
# Progress Bar Examples 

import pyprind


def example_3():
    n = 1000000
    my_bar = pyprind.ProgBar(n, stream=1, title='example3', monitor=True)
    for i in range(n):
        # do some computation
        my_bar.update()
    print(my_bar)



if __name__ == '__main__':
    example_3() 

