# python program to implement a class for employee

# class for employee
class Employee:
    employee_count = 0  # class/static variable
    
    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation
        
        Employee.employee_count += 1
        self.employee_id = 'e' + str(100 + Employee.employee_count)
        
    def show_details(self):
        print('-'*3+' Employee Details '+'-'*3)
        print('Id :', self.employee_id)
        print('Name :', self.name)
        print('Salary :', self.salary)
        print('Designation :', self.designation)
    
    @classmethod
    def total_employees(cls):
        return cls.employee_count
    
# creating object for employee class
e1 = Employee('Akash', 25000, 'IT Support Engineer')    

e1.show_details()
print('Total Employees :', Employee.total_employees())

e2 = Employee('Krishna', 10000, 'AI Engineer')  

e2.show_details()
print('Total Employees :', e2.total_employees())  