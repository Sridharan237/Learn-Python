# python program to print a list in reverse using while loop - using positive indexing

l = [1, 2, 3, 4, 5]

i = len(l)-1    # len(l) - 1 => index of last element in list 'l'

while i >= 0:
    print(l[i], end=' ')
    i = i - 1