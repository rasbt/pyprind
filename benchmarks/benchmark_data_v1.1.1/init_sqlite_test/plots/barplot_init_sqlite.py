# Sebastian Raschka 01/26/2014
# Plotting performance of init_sqlite_.py scripts
# bar chart of relative comparison with variances as error bars

import numpy as np
import matplotlib.pyplot as plt

performance = [
                285.8613,
                306.6960,
                326.3473
              ]
variance = [
            9.1784,
            1.0644,
            0.6383
           ]
scripts = [
            'init_sqlite.py', 
            'init_sqlite_progbar.py', 
            'init_sqlite_percentind.py'
          ]

x_pos = np.arange(len(scripts))

plt.bar(x_pos, performance, yerr=variance, align='center', alpha=0.5)
plt.xticks(x_pos, scripts)
plt.ylim([0,400])

plt.ylabel('CPU time in sec')
plt.title('PyPrind Benchmark on SQLite Database Initialization\nwith 6056212 entries')

#plt.show()
plt.savefig('./barplot_init_sqlite.png')
