# Sebastian Raschka 01/26/2014
# Intialization of a SQLite Database with 6056212
# entries from a data file.
# Uses pyprind.ProgPercent() to visualize the progess as percentage

import sqlite3
import subprocess
import time

input_file = './id_list.txt'

# get line count of the input file
line_cnt = subprocess.check_output(['wc', '-l', input_file])
line_cnt = int(line_cnt.split()[0])

print('Processing %d lines ...' % (line_cnt))
start_time = time.clock()

# open connection and create a new database
conn = sqlite3.connect('./my_sqlite_db.sqlite')
c = conn.cursor()
c.execute('CREATE TABLE my_db (ID INT PRIMARY KEY, column2 TEXT)')

# read entries from a text file and add them to the database
with open(input_file, 'r') as in_file:
    for line in in_file:
        line = line.strip()
        c.execute('INSERT INTO my_db VALUES (%s, "yes")' % (line))

# report CPU time
end_time = time.clock()
total_time = end_time - start_time
print('Time elapsed: {0:.4f} sec'.format(total_time))

# commit changes and close connection
conn.commit()
conn.close()


