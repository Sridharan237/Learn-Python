# python program to query data from tables (students, departments) from universtiy.db

import sqlite3

# creating a connection object
connection = sqlite3.connect('university.db')

# creating a cursor object
cursor = connection.cursor()

# Executing 10 sql queries

'''# 1.query
rows = cursor.execute("select * from departments")

print(rows.fetchone())
# Output : (10, 'CSE')

print(rows.fetchmany(4))
# Output : [(20, 'ECE'), (30, 'Civil'), (40, 'Mech')]'''

'''# 2.query
rows = cursor.execute("select name from students")

print(rows.fetchall())
# Output : [('Ajay',), ('Vijay',), ('Ajay',), ('Ramesh',), ('Suneeta',), ('Anita',), ('Raj',), ('Ali',), ('Michael',), ('Pavan',), ('Suraj',), ('Altaf',), ('Ravi',), ('Verma',), ('Sharma',)]'''

'''# 3.query
rows = cursor.execute("select distinct deptno from students")

print(rows.fetchall())
# Output : [(10,), (20,), (30,), (40,)]'''

'''# 4.query
rows = cursor.execute("select * from students where city='Delhi'")

for row in rows.fetchall():
    print(row)
# Output :
# (1, 'Ajay', 'Delhi', 10)
# (4, 'Ramesh', 'Delhi', 30)
# (14, 'Verma', 'Delhi', 20)'''

'''# 5.query
rows = cursor.execute("select name from students where name like 'A%'")

print(rows.fetchall())
# Output : [('Ajay',), ('Ajay',), ('Anita',), ('Ali',), ('Altaf',)]'''

'''# 6.query
rows = cursor.execute("select rollno, name from students where city not in ('Delhi', 'Hyderabad')")

print(rows.fetchall())
# Output : [(2, 'Vijay'), (3, 'Ajay'), (5, 'Suneeta'), (6, 'Anita'), (7, 'Raj'), (8, 'Ali'), (9, 'Michael'), (10, 'Pavan'), (12, 'Altaf'), (13, 'Ravi'), (15, 'Sharma')]'''

'''# 7.query
rows = cursor.execute("select rollno, students.name, departments.dname from students, departments where students.deptno = departments.deptno")

print(rows.fetchall())
# Output : [(1, 'Ajay', 'CSE'), (2, 'Vijay', 'CSE'), (3, 'Ajay', 'ECE'), (4, 'Ramesh', 'Civil'), (5, 'Suneeta', 'Mech'), (6, 'Anita', 'Civil'), (7, 'Raj', 'Civil'), (8, 'Ali', 'Mech'), (9, 'Michael', 'CSE'), (10, 'Pavan', 'ECE'), (11, 'Suraj', 'CSE'), (12, 'Altaf', 'Mech'), (13, 'Ravi', 'ECE'), (14, 'Verma', 'ECE'), (15, 'Sharma', 'CSE')]'''

'''# 8.query
rows = cursor.execute("select city, count(*) from students group by city")

print(rows.fetchall())
# Output : [(1, 'Ajay', 'CSE'), (2, 'Vijay', 'CSE'), (3, 'Ajay', 'ECE'), (4, 'Ramesh', 'Civil'), (5, 'Suneeta', 'Mech'), (6, 'Anita', 'Civil'), (7, 'Raj', 'Civil'), (8, 'Ali', 'Mech'), (9, 'Michael', 'CSE'), (10, 'Pavan', 'ECE'), (11, 'Suraj', 'CSE'), (12, 'Altaf', 'Mech'), (13, 'Ravi', 'ECE'), (14, 'Verma', 'ECE'), (15, 'Sharma', 'CSE')]'''

'''# 9.query
rows = cursor.execute("select city, count(*) from students group by city having count(*) > 2")

print(rows.fetchall())
# Output : [('Delhi', 3)]'''

'''# 10.query
rows = cursor.execute("select name from students where city = (select city from students where name='Verma')")

for row in rows.fetchall():
    print(row[0])

# Output : 
# Ajay
# Ramesh
# Verma'''

cursor.close()

connection.close()