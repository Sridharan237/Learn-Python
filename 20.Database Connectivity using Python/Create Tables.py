# python program to create tables(departments, students) using sqlite3 module

import sqlite3

# creating a connection object
connection = sqlite3.connect('university.db')

# creating a cursor object
cursor = connection.cursor()

cursor.execute('create table departments(deptno integer primary key, dname text);')

cursor.execute('create table students(rollno integer primary key, name text, city text, deptno integer, foreign key(deptno) references departments(deptno));')

connection.commit() # saving - it is useful in DML queries because doing changes in the tables will not be saved after executing queries using cursor(only DML queries) we need to save it

cursor.close()

connection.close()