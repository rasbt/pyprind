# Sebastian Raschka 01/26/2014
# Intialization of a SQLite Database with 6056212
# entries from a data file

import sqlite3
import subprocess
import pyprind

input_file = './id_list.txt'

# get line count of the input file
line_cnt = subprocess.check_output(['wc', '-l', input_file])
line_cnt = int(line_cnt.split()[0])

print('Processing %d lines ...' % (line_cnt))

# instatiating new progress bar object
my_perc = pyprind.ProgPercent(line_cnt)

# open connection and create a new database
conn = sqlite3.connect('./my_sqlite_db.sqlite')
c = conn.cursor()
c.execute('CREATE TABLE my_db (ID INT PRIMARY KEY, column2 TEXT)')

# read entries from a text file and add them to the database
with open(input_file, 'r') as in_file:
    for line in in_file:
        line = line.strip()
        c.execute('INSERT INTO my_db VALUES (%s, "yes")' % (line))

        # update the progress bar
        my_perc.update()


# End the progress tracking adn report CPU time
my_perc.finish()

# commit changes and close connection
conn.commit()
conn.close()




