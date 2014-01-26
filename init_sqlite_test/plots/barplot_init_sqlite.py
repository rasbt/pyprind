# Sebastian Raschka 01/26/2014
# Plotting performance of init_sqlite_.py scripts
# bar chart of relative comparison with variances as error bars

import numpy as np
import matplotlib.pyplot as plt

performance = [
                253.5762,
                270.3271,
                292.1328
              ]
variance = [
            2.5117,
            1.8397,
            1.0503
           ]
scripts = [
            'init_sqlite.py', 
            'init_sqlite_progbar.py', 
            'init_sqlite_percentind.py'
          ]

x_pos = np.arange(len(scripts))

plt.bar(x_pos, performance, yerr=variance, align='center', alpha=0.5)
plt.xticks(x_pos, scripts)
plt.ylim([0,350])

plt.ylabel('CPU time in sec')
plt.title('PyPrind Benchmark on SQLite Database Initialization\nwith 6056212 entries')

#plt.show()
plt.savefig(‘./barplot_init_sqlite.png')
