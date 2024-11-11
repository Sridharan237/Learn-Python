# python program to implement code to insert data into tables in sqlite database

import sqlite3

# creating a connection object
connection = sqlite3.connect('university.db')

# creating a cursor object
cursor = connection.cursor()


# To insert 3 departments into departments table
'''for i in '123':
    dno = int(input('Enter dno : '))
    dname = input('Enter dname : ')
    cursor.execute(f'insert into departments values({dno}, "{dname}");')'''
    
# To insert 15 students into students table
'''for i in range(1, 16):
    rollno = int(input('Enter Rollno : '))
    name = input('Enter name : ')
    city = input('Enter city : ')
    deptno = int(input('Enter deptno : '))    
    
    cursor.execute(f'insert into students values({rollno}, "{name}", "{city}", {deptno})')'''

connection.commit() # saving - it is useful in DML queries because doing changes in the tables will not be saved after executing queries using cursor(only DML queries) we need to save it

cursor.close()

connection.close()