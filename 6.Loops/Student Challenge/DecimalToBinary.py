# python program to convert a decimal number to a binary number using while loop (two methods)
import math

# method1 - by dividing the number by 2 and adding the remainder to the front of an integer
n = int(input('Enter a number(in decimal number system) : '))

temp = n

binary = 0

count = 0

while n:
    remainder = n % 2
    binary = remainder * 10**count + binary
    n //= 2
    count += 1

print('Binary Number(method1) :', binary)

# method2 - by dividing the number by 2 and adding the remainder to the front of a string (this makes logic simple and not using ** - exponentiation operator)
Binary = ''

while temp:
    remainder = temp % 2
    temp //= 2
    Binary = str(remainder) + Binary

print('Binary Number(method2) :', Binary)