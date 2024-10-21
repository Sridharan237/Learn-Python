# program to implement pickling(storing objects in a file) in python

import Student, pickle

# creating a list of Student objects
students = [Student.Student(11, 'John', 'cs'), Student.Student(26, 'Ajay', 'ec'), Student.Student(33, 'Vikram', 'it')]

with open('students.data', 'wb') as f:
    pickle.dump(students, f)
    print(students)