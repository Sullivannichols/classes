#!/usr/bin/env python3

import sqlite3

database = 'mydb.sqlite'
table_name = 'table2'
id_column = 'column2'
some_id = 123456
column2 = 'column2'
column3 = 'column3'

conn = sqlite3.connect(database)
c = conn.cursor()

c.execute('SELECT * FROM {tn} WHERE {cn}="Hi World"'\
    .format(tn=table_name, cn=column2))
all_rows = c.fetchall()
print('1):', all_rows)

c.execute('SELECT ({coi}) FROM {tn} WHERE {cn}="Hi World"'\
    .format(coi=column2, tn=table_name, cn=column2))
all_rows = c.fetchall()
print('2):', all_rows)

c.execute('SELECT {coi1},{coi2} FROM {tn} WHERE {coi1}="Hi World"'\
    .format(coi1=column2, coi2=column3, tn=table_name, cn=column2))
all_rows = c.fetchall()
print('3):', all_rows)

c.execute('SELECT * FROM {tn} WHERE {cn}="Hi World" LIMIT 10'\
    .format(tn=table_name, cn=column2))
ten_rows = c.fetchall()
print('4):', ten_rows)

c.execute("SELECT * FROM {tn} WHERE {idf}={my_id}"\
    .format(tn=table_name, cn=column2, idf=id_column, my_id=some_id))
id_exists = c.fetchone()
if id_exists:
    print('5): {}'.format(id_exists))
else:
    print('5): {} does not exist.'.format(some_id))

conn.close()
