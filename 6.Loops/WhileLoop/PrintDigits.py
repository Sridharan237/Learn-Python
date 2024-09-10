# python program to implement a task to print the digits of an integer from right to left using while loop

num = int(input('Enter a number : '))

while num > 0:
    lastDigit = num % 10
    num = num // 10

    print('Digit :', lastDigit)