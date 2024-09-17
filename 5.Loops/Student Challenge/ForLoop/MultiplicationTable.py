# python program to print the multiplication table for a given number from 1 to 10 using for loop (using range())

n = int(input('Enter a number : '))

print('=' * 6, 'Multiplication Table', '=' * 6)

for x in range(1, 11):
    print(n, 'X', x, '=', n * x)