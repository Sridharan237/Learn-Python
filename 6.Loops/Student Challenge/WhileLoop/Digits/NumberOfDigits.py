# python program to find the number of digits in a number using while loop

n = int(input('Enter a number : '))

digits = 0

if n < 0:
    n = -n

if n != 0:
    while n:
        digits += 1
        n //= 10
else:
    digits = 1

print('Digits : ', digits)