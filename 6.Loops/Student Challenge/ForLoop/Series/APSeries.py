# python program to print the n terms of an Arithmetic Progression (AP) Series using for loop (using range() function)

a = int(input('Enter the first term : '))                       # first term
d = int(input('Enter the common difference : '))                # common difference
n = int(input('Enter the no. of terms needs to be printed : ')) # no. of terms

# Formula : Tn = a + (n-1)d -> to find the nth term of an AP

for x in range(a, a+n*d, d):
    print(x,'')
