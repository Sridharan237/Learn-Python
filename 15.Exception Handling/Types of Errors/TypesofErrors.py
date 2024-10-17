# python program to implement types of errors in programming

# Types of Error : 

# 1.Syntax Error

# Example 1
# if 10 > 5
# # Output : SyntaxError: expected ':'

# Example 2
# if 10 > 5:  # Output : IndentationError: expected an indented block after 'if' statement on line 10
# print(10)



# 2.Runtime Error - Exceptions

# Example 1
# a = int(input('Enter first number : '))
# b = int(input('Enter second number : '))    

# c = a // b  # Output : if b is 0, then Output => ZeroDivisionError: integer division or modulo by zero 

# print(c)

# Example 2
print('hello')
# print(variable) # Output : NameError: name 'variable' is not defined. Did you mean: 'callable'?
print('welcome')



# 3.Logical Error 

# program with logical error
a = int(input('Enter first number : '))
b = int(input('Enter second number : '))   
c = int(input('Enter third number : '))   

d = a // b - c

print('d :', d) # if a = 20, b = 7, c = 2, then d = 0


# program without logical error (after correcting logical error)
a = int(input('Enter first number : '))
b = int(input('Enter second number : '))   
c = int(input('Enter third number : '))   

d = a // (b - c)

print('d :', d)
