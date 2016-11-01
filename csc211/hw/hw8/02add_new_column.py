#!/usr/bin/env python3

import sqlite3

database = 'mydb.sqlite'
table_name = 'table2'
id_column = 'column1'
new_column1 = 'column2'
new_column2 = 'column3'
column_type = 'TEXT'
default_val = 'Hello World'

conn = sqlite3.connect(database)
c = conn.cursor()

c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}" \
        .format(tn=table_name, cn=new_column1, ct=column_type))

c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct} DEFAULT '{df}'" \
        .format(tn=table_name, cn=new_column2, ct=column_type, df=default_val))

conn.commit()
conn.close()

