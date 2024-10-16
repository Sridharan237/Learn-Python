# python program to implement caller class in python

# Depts - Caller Class
class Depts:
    def __init__(self):
        self.depts = {
            'hr' : 'Human Resource Department',
            'acc' : 'Accounts and Finance Department',
            'sd' : 'Sales and Marketing Department',
            'mft' : 'Manufacturing Department',
            'mkt' : 'Marketing Department'
        }
        
    def __call__(self, dept_code):
        return self.depts[dept_code]
    

# creating object for caller class - Depts
d = Depts()

dname = d('hr')
print(dname)
print(d('mkt'))