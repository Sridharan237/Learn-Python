# python program to print a list in reverse using for loop - using positive indexing

l = [1, 2, 3, 4, 5]

for i in range(len(l)-1, -1, -1):
    print(l[i], end=' ')