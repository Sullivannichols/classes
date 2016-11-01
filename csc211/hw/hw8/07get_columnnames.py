#!/usr/bin/env python3

import sqlite3

database = 'mydb.sqlite'
table_name = 'table3'

conn = sqlite3.connect(database)
c = conn.cursor()

c.execute('PRAGMA TABLE_INFO({})'.format(table_name))

names = [tup[1] for tup in c.fetchall()]
print(names)

conn.close()
