# python program to implement DML queries (update, delete) on tables

import sqlite3

# creating connection object
connection = sqlite3.connect('university.db')

# creating cursor object
cursor = connection.cursor()

# update queries

'''# 1.query
cursor.execute("update departments set dname='Chem' where dname='Mech'")'''

'''# 2.query
cursor.execute("update students set city='Bhopal' where rollno=15")'''



# delete queries

'''# 3.query
cursor.execute("delete from students where rollno=15")'''

# 4.query
cursor.execute("delete from students where deptno=50")

connection.commit()

cursor.close()

connection.close()