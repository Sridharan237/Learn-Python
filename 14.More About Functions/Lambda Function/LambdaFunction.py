# python program to implement lambda function

# Example 1 => convert miles to kilometers

# function to return kilometers when miles is passed to it
def miles2Kms(miles):   
    kms = 1.6 * miles
    return kms

print('kms :', miles2Kms(10))

# lambda function to return kilometers when miles is passed to it
kms = lambda miles: 1.6 * miles

print('kms :', kms(10))



# Example 2 => add 2 numbers

# function to add 2 numbers and return the sum when 2 numbers are passed to it
def add(a, b):
    c = a + b
    return c

print('Sum :', add(10, 15))

# lambda function to add 2 numbers and return the sum when 2 numbers are passed to it
sum = lambda a, b: a + b

print('Sum :', sum(10, 15))



# Example 3    => find maximum of 3 numbers

# function to return maximum of 3 numbers
def max3(a, b, c):
    if a > b and a > c:
        max = a
    elif b > c:
        max = b
    else:
        max = c    
    return max

print('Maximum :', max3(10, 15, 20))

# lambda function to return maximum of 3 numbers
maximum = lambda a, b, c: a if a > b and a > c else b if b > c else c

print('Maximum :', maximum(10, 15, 20))