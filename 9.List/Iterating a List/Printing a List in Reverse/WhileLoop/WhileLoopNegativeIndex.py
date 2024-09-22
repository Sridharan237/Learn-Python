# python program to print a list in reverse using while loop - using negative indexing

l = [1, 2, 3, 4, 5]

i = -1    # -1 => index of last element in list 'l' - as negative index

while i >= -len(l):
    print(l[i], end=' ')
    i = i - 1