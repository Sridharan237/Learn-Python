# python program to print the prime numbers from 1 to 100 using nested for loop using flag variable

import math

flag = 0

print('='*3, 'Prime Numbers from 1 to 100', '='*3)

for n in range(1, 101):
    if n == 1:         # 1 - is not a prime number (prime number - a natural number greater than 1 which only needs to have divisors as 1 and itself
        print(n, ':', 'Not Prime Number')
        continue
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            flag = 1
            break
    if flag == 0:
        print(n, ':', 'Prime Number')
    else:
        print(n, ':', 'Not Prime Number')
    flag = 0
