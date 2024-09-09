# python program to implement Identity Operators - is, is not
a = 10
b = 10
print(id(a))            # OUTPUT :  140716706896600
print(id(b))            # OUTPUT :  140716706896600
print(a is b)           # OUTPUT :  True
print(a is not b)       # OUTPUT :  False
a = 256
b = 256
print(id(a))            # OUTPUT :  140716706904472
print(id(b))            # OUTPUT :  140716706904472
print(a is b)           # OUTPUT :  True
print(a is not b)       # OUTPUT :  False
a = 257
b = 257
print(id(a))            # OUTPUT :  2693027283664
print(id(b))            # OUTPUT :  2693027298224
print(a is b)           # OUTPUT :  False
print(a is not b)       # OUTPUT :  True

# 1. Assigning values to variables directly(literals)
a = 10
b = 10
print(a is b)           # OUTPUT :  True
print(a is not b)       # OUTPUT :  False

# 2. getting input through input() function
a = input("Enter a number : ")
# Input : Enter a number : 10
b = input("Enter a number : ")
# Input : Enter a number : 10
print(a)                # OUTPUT : '10'
print(b)                # OUTPUT : '10'
print(id(a))            # OUTPUT :  2693027163776
print(id(b))            # OUTPUT :  2693027163536
print(a is b)           # OUTPUT :  False
print(a is not b)       # OUTPUT :  True

# 3. getting input through input() function and typecasting it at the same time
a = int(input("Enter a number : "))
# Input : Enter a number : 10
b = int(input("Enter a number : "))
# Input : Enter a number : 10
print(id(a))            # OUTPUT :  140716706896600
print(id(b))            # OUTPUT :  140716706896600
print(a is b)           # OUTPUT :  True
print(a is not b)       # OUTPUT :  False