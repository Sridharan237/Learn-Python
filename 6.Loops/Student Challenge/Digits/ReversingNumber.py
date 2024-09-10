# python program to find the reverse of a number using while loop

n = int(input('Enter a number : '))

reverse = 0
flag = 0

if n < 0:
    flag = 1
    n = -n

while n:
    lastDigit = n % 10
    reverse = reverse * 10 + lastDigit

    n //= 10

if flag == 1:
    reverse = -reverse

print('Reversed Number :', reverse)
