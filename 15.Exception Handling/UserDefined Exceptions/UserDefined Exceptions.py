# python program to implement user defined exceptions (or) custom exceptions

# Example 1 => program to write our own custom exception (MyError) inheriting from Exception class - without class body

class MyError(Exception):
    pass


print('Before try block')

try:
    print('Entering try block')
    
    raise MyError('MyError-Some Error')

except MyError as error:
    print('Error Message :', error)
    
    
    
# Example 2 => program to write our own custom exception (MyCustomError) inheriting from Exception class - with class body

class MyCustomError(Exception):
    def __init__(self, msg):
        self.msg = msg
        
    def __str__(self):
        return self.msg
    
    
    
print('Before try block')

try:
    print('Entering try block')
    
    raise MyCustomError('MyCustomError-Some Error')

except MyCustomError as error:
    print('Error Message :', error)
    
