# Sebastian Raschka 01/25/2014
# Bad Progress Bar Examples 

import pyprind


def example_1():
    n = 1000000
    my_bar = pyprind.ProgBar(n, width=40)

    # updates progress bar twice as often as seeded
    # bar progress becomes inaccuate
    # but the CPU time is not affected.
    for i in range(2*n):
       my_bar.update()
    my_bar.finish() 


if __name__ == '__main__':
    example_1() 

