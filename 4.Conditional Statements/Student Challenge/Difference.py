# python program to find the difference between two numbers (difference - only +ve)

n1 = int(input('Enter number1 : '))
n2 = int(input('Enter number2 : '))

if n1 - n2 >= 0:
    print('Difference :', n1 - n2)
else:
    print('Difference :', n2 - n1)