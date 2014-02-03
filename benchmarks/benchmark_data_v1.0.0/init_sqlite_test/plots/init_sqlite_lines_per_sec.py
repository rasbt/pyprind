# Sebastian Raschka 01/26/2014
# Plotting performance of init_sqlite_.py scripts
# Barplot of additional computing time as lines per sec

import numpy as np
import matplotlib.pyplot as plt

performance = [
                361546.9081,
                157073.5612,
              ]
scripts = [
            'init_sqlite_progbar.py', 
            'init_sqlite_percentind.py'
          ]

x_pos = np.arange(len(scripts))

plt.bar(x_pos, performance, align='center', alpha=0.5)
plt.xticks(x_pos, scripts)
#plt.ylim([0,350])

plt.ylabel('Lines per sec')
plt.title('PyPrind Benchmark: How many lines per second can be processed\n\
        for 1 second of performance loss?')

#plt.show()
plt.savefig('./init_sqlite_lines_per_sec.png')
