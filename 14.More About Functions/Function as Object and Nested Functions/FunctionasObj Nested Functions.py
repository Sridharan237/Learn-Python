# python program to implement function as object and nested functions

# 1. Function as Object

def display(name):
    print('hello', name)
    
# d = display('name')   # d - None (type)
# d('Ramesh')           # d - TypeError: 'NoneType' object is not callable

d = display
print(type(display('ramesh')))  # Output : <class 'NoneType'>
print(type(display))            # Output : <class 'function'>
print(type(d))                  # Output : <class 'function'>

display('Ramesh')
d('Arun')

def display():
     print('hello')

d = display

print(display)
# Output : <function display at 0x0000029C8B308A40>

print(d)
# Output : <function display at 0x0000029C8B308A40>

# Both display and d are referring 0x0000029C8B308A40 (for example)



# 2. Nested Functions

def outer():        # outer - outer function
    def inner():    # inner - inner function (or) nested function
        print('inner function')
    inner()
    
outer()
inner()     # Output : NameError: name 'inner' is not defined. Did you mean: 'iter'?
    
    