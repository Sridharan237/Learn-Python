# python program to create a nested dictionary for student details

n = int(input('Enter the total number of students : '))

students = {}

for i in range(n):
    name = input('Enter Student Name : ')
    rollno = int(input('Enter Student Rollno : '))
    dept = input('Enter Department Name : ')

    students[name] = {'Rollno':rollno, 'Name':name, 'Dept_name':dept}

print(students)
