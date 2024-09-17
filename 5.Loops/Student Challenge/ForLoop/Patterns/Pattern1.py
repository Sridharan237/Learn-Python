# python program to print a square pattern of character '*' of size n x n -> (n - rows, n - columns) using two methods:
# method-1 -> using nested for loop
# method-2 -> using single for loop and * -> string multiplication operator(multiplication operator (asterisk))

n = int(input('Enter the size : '))

# method-1

"""for i in range(0,n):
    for j in range(0, n):
        print('* ', end='')
    print('')
"""

# method-2

for i in range(n):
    print('* ' * n)