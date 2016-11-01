#!/usr/bin/env python3

import sqlite3

database = 'mydb.sqlite'
table_name = 'table2'
id_column = 'column1'
column_name = 'column2'

conn = sqlite3.connect(database)
c = conn.cursor()

try:
    c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')"\
        .format(tn=table_name, idf=id_column, cn=column_name))
except sqlite3.IntegrityError:
    print('ERROR: ID already exists in PRIMARY KEY column {}'\
        .format(id_column))

c.execute("INSERT OR IGNORE INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')"\
    .format(tn=table_name, idf=id_column, cn=column_name))

c.execute("UPDATE {tn} SET {cn}=('Hi world') WHERE {idf}=(123456)"\
    .format(tn=table_name, cn=column_name, idf=id_column))

conn.commit()
conn.close()


