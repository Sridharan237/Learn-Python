# python program to find the sum of given numbers using while loop

n = int(input('Enter the no. of numbers : '))

i = 0
Sum = 0

while i < n:
    temp = int(input('Enter a number : '))
    Sum += temp
    i += 1

print('Sum of given numbers :', Sum)
