# python program to find whether a given number is prime number or not using for loop(using range() function)
import math

n = int(input('Enter a number : '))

count = 2

for x in range(2, int(math.sqrt(n))+1):
    if n % x == 0:
        count += 1

if count > 2:
    print('Not Prime Number')
else:
    print('Prime Number')
