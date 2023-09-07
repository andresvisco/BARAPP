import sqlite3


##create table
with open('db/CREATE_MOVIMIENTOS.sql', 'r') as sql_file:
    sql_script = sql_file.read()

db = sqlite3.connect('db/bar.db')
cursor = db.cursor()
cursor.executescript(sql_script)
db.commit()
db.close()

###insert data
