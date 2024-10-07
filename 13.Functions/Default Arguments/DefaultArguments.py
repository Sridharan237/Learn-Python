# python program to implement default arguments in functions

def add(a, b, c):   # function-1
    return a+b+c

def add(a, b=0, c=0):   # function-2
    return a+b+c

print('Addition :', add(10, 5, 15))       # function-1 will be called

print('Addition :', add(10, 5))              # function-2 will be called
print('Addition :', add(10))                       # function-2 will be called

print('Addition :', add(a=10, b=5, c=15))         # function-2 will be called - keyword arguments
print('Addition :', add(10, b=5, c=15))        # function-2 will be called - keyword arguments
print('Addition :', add(10, 5, c=15))       # function-2 will be called - keyword arguments



# Default Arguments will be created only once
def addItem(item, L=[]):
    L.append(item)
    return L

L1 = [10, 20, 30]
addItem(50, L1)
print(L1)

# Default Arguments will be created only once
addItem(1)
addItem(2)
addItem(3)
print(addItem(4))