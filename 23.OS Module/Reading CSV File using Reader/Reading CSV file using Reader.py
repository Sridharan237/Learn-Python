# python program to read the contents of a csv file using csv module's reader
import csv

# opening a csv file in read mode

f = open('D:\\Learn-Github-Repositories\\Learn Python Programming - Beginner to Master\\23.OS Module\\Reading CSV File using Reader\\Employees.csv', 'r')

csv_reader = csv.reader(f)  # csv_reader object is an iterator returned by reader() function

'''# used for printing all rows
for row in csv_reader:
    print(row)'''
    
# finding minimum and maximum salary

print(next(csv_reader))

'''for row in csv_reader:
    salaries.append(int(row[2]))'''

# find the name of employees with minimum and maximum salary

salaries = []

employees = []

for row in csv_reader:
    employees.append(row[1])
    salaries.append(int(row[2]))
    
print('Salaries :', salaries)
print('Minimum Salary :', min(salaries))
print('Maximum Salary :', max(salaries))

for i in range(len(salaries)):
    if salaries[i] == min(salaries):
        min_salary_index = i
    elif salaries[i] == max(salaries):
        max_salary_index = i

print('Employees :', employees)
print('Employee with Minimum Salary :', employees[min_salary_index])
print('Employee with Maximum Salary :', employees[max_salary_index])

f.close()   # closing the csv file