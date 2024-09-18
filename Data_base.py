import sqlite3
dbase=sqlite3.connect('pythondatabase.db')
dbase.execute('''create table if not exists new(ID Integer Primary Key Autoincrement,
Name Text Not Null,
Dept Text Not Null,
Year Text Not Null,
Clg Text Not Null,
Contact Text Not Null,
Email Text Not Null Unique)''')

dbase.commit()
dbase.close()
