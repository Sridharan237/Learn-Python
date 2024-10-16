# python program to implement the features of functions

# 3. Function as Parameter

# Example 1
def display():
    print('hello')

def func(d):
    d()
    
func(display)

# Example 2

def add(x, y):
    print(x+y)

def sub(x, y):
    print(x-y)
    
def func(f, x, y):  # f - function name (here)
    f(x, y)
    
func(add, 15, 10)
func(sub, 15, 10)

# 4. Function returning another Function

def outer():
    
    def display():
        print('hello')
        
    return display



print(outer())  
# Output : <function outer.<locals>.display at 0x000002635903B7E0>
f = outer
print(outer)    
# Output : <function outer at 0x000002385BE2D3A0>
print(f)
# Output : <function outer at 0x000002385BE2D3A0>
print(f())
# Output : <function outer.<locals>.display at 0x000002385BE8B7E0>
    
f = outer()
print(f)
# Output : <function outer.<locals>.display at 0x000001F62D0BB7E0>
f()
# Output : hello
print(f())
''' Output : 
hello
None
'''