# python program to implement the decorator function in python

# Example 1 - decorator
def decorator(fun):
    
    def wrapper():
        print('*' * 5)
        fun()
        print('*' * 5)
    
    return wrapper

def display():
    print('hello')
    
d = decorator(display)
d() 

''' 
Output : 
*****
hello
*****
'''



# Example 2 - decorator 
def decorator(fun):
    
    def wrapper(message):
        print('*' * 5)
        fun(message)
        print('*' * 5)
    
    return wrapper

def display(message):
    print(message)
    
d = decorator(display)
d('welcome') 

'''
Output : 
*****
welcome
*****
'''




# Example 3 - decorator 
def decorator(fun):
    
    def wrapper(message):
        print('*' * 5)
        fun(message)
        print('*' * 5)
    
    return wrapper

def display(message):
    print(message)
    
display = decorator(display)
display('good morning')
 
''' 
Output : 
*****
good morning
*****
'''



# Example 4 - decorator (original decorator)
def decorator(fun):
    
    def wrapper(message):
        print('*' * 5)
        fun(message)
        print('*' * 5)
    
    return wrapper

@decorator
def display(message):
    print(message)
    
# display = decorator(display)  # This Line must not be given when @decorator is used - because it will be automatically done when @decorator - annotation is used above the respective function to be decorated
display('well done!') 

''' 
Output : 
*****
well done!
*****
'''