# python program to find the sum of digits of a number using while loop

n = int(input('Enter a number : '))

Sum = 0

if n < 0:
    n = -n

while n:
    lastDigit = n % 10
    Sum += lastDigit
    n //= 10

print('Sum of digits :', Sum)