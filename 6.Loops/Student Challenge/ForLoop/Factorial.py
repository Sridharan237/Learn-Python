# python program to find the factorial of a given number using for loop(using range() function)

n = int(input('Enter a number : '))

factorial = 1

for x in range(2, n+1):
    factorial *= x

print('Factorial :', factorial)