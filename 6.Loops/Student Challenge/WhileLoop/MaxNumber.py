# python program to find the maximum of given numbers using while loop

n = int(input('Enter the no. of numbers : '))

i = 0

Max = -99999999

while i < n:
    num = int(input('Enter a number : '))

    if num > Max:
        Max = num

    i += 1

print('Maximum number :', Max)
