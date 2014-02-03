# PyPrind Benchmarks

I tested the performance of the PyPrind progress bar and percentage indicator visualization with an typical application where I created a SQLite database.  
The database was initialized with IDs from a simple text files consisting of 6,056,212 rows.  
For this test, I used a set of three similar scripts:  <br>
<br>
1) init_sqlite.py  (procedure without PyPrind visualization)  
2) init_sqlite_progbar.py  (procedure with PyPrind progress bar visualization)  
3) init_sqlite_percentind.py  (procedure with PyPrind percentage indicator visualization)  

The test code and results can be found at [https://github.com/rasbt/pyprind/tree/master/benchmarks/benchmarks/benchmark_data_v1.1.1_v1.1.1/init_sqlite_test](https://github.com/rasbt/pyprind/tree/master/benchmarks/benchmarks/benchmark_data_v1.1.1_v1.1.1/init_sqlite_test)

## Test code

The contents of the input text file for the database initialization and the respective scripts are shown in the following figures:  
#### id_list.txt
![id_list.txt](https://raw2.github.com/rasbt/pyprind/master/benchmarks/benchmark_data_v1.1.1/init_sqlite_test/images/list_id.txt.png)
#### 1) init_sqlite.py
![init_sqlite.py](https://raw2.github.com/rasbt/pyprind/master/benchmarks/benchmark_data_v1.1.1/init_sqlite_test/images/init_sqlite_code.png)
#### 2) init_sqlite_progbar.py
![init_sqlite_progbar.py](https://raw2.github.com/rasbt/pyprind/master/benchmarks/benchmark_data_v1.1.1/init_sqlite_test/images/init_sqlite_progbar_code.png)
#### 3) init_sqlite_percentind.py
![init_sqlite_percentind.py](https://raw2.github.com/rasbt/pyprind/master/benchmarks/benchmark_data_v1.1.1/init_sqlite_test/images/init_sqlite_percentind_code.png)
#### 4) the resulting database: my_sqlite_db.sqlite
![my_sqlite_db.sqlite](https://raw2.github.com/rasbt/pyprind/master/benchmarks/benchmark_data_v1.1.1/init_sqlite_test/images/my_sqlite_db.png)

## Results

I measured the CPU times for each script three times in a row to check for consistency, and plotted the averages with variances as error bars.  
The data is shown in the spreadsheet below, which can be downloaded from [https://raw2.github.com/rasbt/pyprind/master/benchmarks/benchmark_data_v1.1.1/init_sqlite_test/raw_data/init_sqlite_spreadsheet.csv](https://raw2.github.com/rasbt/pyprind/master/benchmarks/benchmark_data_v1.1.1/init_sqlite_test/raw_data/init_sqlite_spreadsheet.csv)
![spreadheet_image](https://raw2.github.com/rasbt/pyprind/master/benchmarks/benchmark_data_v1.1.1/init_sqlite_test/images/init_sqlite_spreadsheet.png)  

The machine that was used for this test had the following specifications:  
<hr>
**System Specifications:**  
Model Name: Mac mini (Mid 2010)  
Processor Name: Intel Core 2 Duo  
Processor Speed: 2.4 GHz  
Number of Processors: 1  
Total Number of Cores: 2  
L2 Cache: 3 MB  
Memory: 8 GB 1067 MHz DDR3  
Bus Speed: 1.07 GHz  

Operating System: Mac OS X 10.9.1  
Python version: 3.3.3  
<hr>

Using PyPrind's progress bar visualization resulted in a 20.8347 sec longer CPU time for the 6,056,212 iterations in the data processing loop.  PyPrind's percentage indicator used a little bit more resources and added 40.4861 sec of CPU time.  
The results (average values with variances as error bars) are shown in the bar plot below.  
![https://raw2.github.com/rasbt/pyprind/master/benchmarks/benchmark_data_v1.1.1/init_sqlite_test/plots/barplot_nit_sqlite.png](https://raw2.github.com/rasbt/pyprind/master/benchmarks/benchmark_data_v1.1.1/init_sqlite_test/plots/barplot_nit_sqlite.png)

The results indicate that the PyPrind progress visualization has a reasonable performance.  
The cost can be calculated as follows: (total number of iterations) / (additional CPU time in sec)  
For PyPrind's progress bar, an 290,678 iterations cost 1 sec of CPU time, and PyPrind's percent indicator requires 1 sec of CPU time for every 149,587 iterations. The results are visualized in the bar plot below.  
![bar plot lines per second](https://raw2.github.com/rasbt/pyprind/master/benchmarks/benchmark_data_v1.1.1/init_sqlite_test/plots/init_sqlite_lines_per_sec.png)
