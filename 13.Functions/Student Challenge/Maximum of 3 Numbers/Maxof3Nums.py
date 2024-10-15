# python program to implement a function to find the maximum of 3 numbers

def max3Nums(a, b, c):
    return a if a > b and a > c else b if b > c else c

print(max3Nums(5, 10, 12))