# python program to read the contents of a csv file using csv DictReader

import csv 
import pprint # pprint - is a module to print very large data in a formatted way

# opening the csv file
f = open('D:\\Learn-Github-Repositories\\Learn Python Programming - Beginner to Master\\23.OS Module\\Reading CSV File using Reader\\Employees.csv', 'r')

csv_dictreader = csv.DictReader(f)

'''# for printing the details of each employee
for row in csv_dictreader:
    print(row)'''
    
# to make a single dictionary of employee names as keys and values as each employee details(dictionary format)
employees = {}  # empty dictionary

for row in csv_dictreader:
    employees[row['Name']] = row

pprint.pprint(employees)    # employees - dictionary with employee name as key and employee details(another dictionary) as values

print('-'*3, 'Employee Details', '-'*3)
print('Employee Name : Harry')
print('Details :', employees['Harry'])
    
f.close() # closing the csv file