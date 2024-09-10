# python program to find the sum of given positive and negative numbers separately using while loop

n = int(input('Enter the no. of numbers : '))

pSum, nSum = 0, 0

i = 0

while i < n:
    num = int(input('Enter a number : '))
    if num > 0:
        pSum += num
    elif num < 0:
        nSum += num
    i += 1

print('Sum of positive numbers :', pSum)
print('Sum of negative numbers :', nSum)