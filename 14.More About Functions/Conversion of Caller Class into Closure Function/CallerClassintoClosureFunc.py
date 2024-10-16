# python program to write a closure function for a caller class

# Depts - Closure function
def Depts():
    depts = {
        'hr' : 'Human Resource Department',
        'acc' : 'Accounts and Finance Department',
        'sd' : 'Sales and Marketing Department',
        'mft' : 'Manufacturing Department',
        'mkt' : 'Marketing Department'
    }
        
    def dname(dept_code):
        return depts[dept_code]

    return dname
    

# creating object for caller class - Depts
d = Depts()

department_name = d('hr')
print(department_name)
print(d('mkt'))