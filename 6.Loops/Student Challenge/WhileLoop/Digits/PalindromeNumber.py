# Python program to find whether a number is palindrome or not

n = int(input('Enter a number : '))

temp = n

# Logic for Reversing a number
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

# To check whether palindrome or not
if temp == reverse:
    print('Palindrome')
else:
    print('Not Palindrome')