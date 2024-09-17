# python program to print the n terms of Fibonacci Series using for loop (using range() function)

n = int(input('Enter the no. of terms needs to be printed :  '))    # n - no. of terms

a = 0   # first term
b = 1   # second term

for x in range(0, n):
    if x <= 1:
        print(x)
    else:
        c = a+b
        print(c, '')
        a = b
        b = c
