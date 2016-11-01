#!/usr/bin/env python3

import sqlite3

database = 'mydb.sqlite'
table_name = 'table2'
id_column = 'column1'
new_column = 'unique_names'
column_type = 'TEXT'
index_name = 'my_unique_index'

conn = sqlite3.connect(database)
c = conn.cursor()

c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
    .format(tn=table_name, cn=new_column, ct=column_type))

c.execute("UPDATE {tn} SET {cn}='sebastian_r' WHERE {idf}=123456"\
    .format(tn=table_name,idf=id_column, cn=new_column))

c.execute("CREATE INDEX {ix} on {tn}({cn})"\
    .format(ix=index_name, tn=table_name, cn=new_column))

c.execute("DROP INDEX {ix}"\
    .format(ix=index_name))

conn.commit()
conn.close()
