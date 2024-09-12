# python program to find the factors of a given number using for loop(using range() function)

n = int(input('Enter a number : '))

print(1)

for x in range(2, n//2+1):
    if n % x == 0:
        print(x)
