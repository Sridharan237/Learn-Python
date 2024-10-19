# python program to implement exception handling using try an except blocks and why we require try and except blocks

# Example 1 => program handles ZeroDivisionError Exception - without using try-except blocks 

a = int(input('Enter first number : '))
b = int(input('Enter second number : '))

if b != 0:
    c = a // b
    print('Division :', c)
    
else:
    print('Zero Division Error')
    


# Example 2 => program handles ZeroDivisionError Exception - without using try-except blocks and divides using custom function div()

# function to take 2 arguments and returns quotient (or) return -1 if second number is 0
def div(a, b):
    if b != 0:
        c = a // b
        return c
    else:
        return -1   # -1 - means ZeroDivisionError  => Division by zero


a = int(input('Enter first number : '))
b = int(input('Enter second number : '))

c = div(a, b)

if c == -1:
    print('Zero Division Error')
    
else:
    print('Division :', c)
    


# Example 3 => program handles ZeroDivisionError Exception - with using try-except blocks and divides using custom function div() 

# function to take 2 arguments and returns quotient (or) raises ZeroDivisionError exception if second number is 0
def div(a, b):
    if b != 0:
        c = a // b
        return c
    else:
        raise ZeroDivisionError

a = int(input('Enter first number : '))
b = int(input('Enter second number : '))

try:
    c = a // b
    print('Division :', c)
    
except:
    print('Zero Division Error')