#!/usr/bin/env python3

import sqlite3

database = 'mydb.sqlite'
table_name1 = 'table1'
table_name2 = 'table2'
new_field = 'column1'
field_type = 'INTEGER'

conn = sqlite3.connect(database)
c = conn.cursor()

c.execute('CREATE TABLE {tn} ({nf} {ft})' \
        .format(tn=table_name1, nf=new_field, ft=field_type))

c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)' \
        .format(tn=table_name2, nf=new_field, ft=field_type))

conn.commit()
conn.close()
