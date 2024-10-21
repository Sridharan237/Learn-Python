# program to implement unpickling(retrieving stored objects from a file) in python

import Student, pickle

with open('students.data', 'rb') as f:
        students = pickle.load(f)
        
        for s in students:
            s.display()