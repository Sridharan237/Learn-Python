# python program to display multiplication table for a given number using count variable

n = int(input('Enter a number : '))

count = 1

print('Multipication Table of', n, ":")

while count <= 10:
    print(n, 'x', count, '=', n*count)
    count += 1

