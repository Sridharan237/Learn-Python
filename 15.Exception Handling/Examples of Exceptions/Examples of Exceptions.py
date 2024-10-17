# python program to implement programs to specify some of the exceptions

# Exceptions

'''# 1.IndexError
L = [10, 20, 30, 40, 50]

index = int(input('Enter an index : '))

print(L[index]) 
# Input : Enter an index : 5
# Output : IndexError: list index out of range -> Exception / Runtime Error'''

# Simply Handling above IndexError
L = [10, 20, 30, 40, 50]

index = int(input('Enter an index (between 0-4): '))

print(L[index]) 

'''# 2.ValueError
val = int('abc')

# Output : ValueError: invalid literal for int() with base 10: 'abc'''

'''# 3.TypeError
print('2'+3)
# Output : TypeError: can only concatenate str (not "int") to str'''

# Simply Handling above TypeError
print('2'+str(3))
# Output : 23

'''# 4.KeyError - Accessing key which is not present in dictionary
d = {1:'a', 2:'b', 3:'c'}

key = int(input('Enter a key : '))

print(d[key])
# Input : 5
# Output : KeyError: 5'''

# 5.ZeroDivisionError
a = int(input('Enter first number : '))
b = int(input('Enter second number : '))

c = a // b

print(c)

# Eg-1
# Input : Enter first number  : 10
# Input : Enter second number : 0
# Ouptut : ZeroDivisionError: integer division or modulo by zero

# Eg-2
# Input : Enter first number  : abc
# Ouptut :  ValueError: invalid literal for int() with base 10: 'abc'

