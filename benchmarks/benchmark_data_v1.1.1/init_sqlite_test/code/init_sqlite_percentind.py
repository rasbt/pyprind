# Sebastian Raschka 02/01/2014
# Intialization of a SQLite Database with 6056212
# entries from a data file which consists of 2 comma-separated columns
# Uses pyprind.ProgPercent() to visualize the progess as percentage

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
c.execute('CREATE TABLE my_db (ID INT PRIMARY KEY, rank TEXT)')

# read entries from a text file and add them to the database
with open(input_file, 'r') as in_file:
    for line in in_file:
        line = line.strip().split(',')
        c.execute('INSERT INTO my_db (id, rank) VALUES (%s, "%s")' 
            % (line[0],line[1]))

        # update the progress bar
        my_perc.update()


# commit changes and close connection
conn.commit()
conn.close()




