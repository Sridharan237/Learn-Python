# python program to implement the addition of 3 numbers using function

# Function that takes 3 parameters and return their sum as the result
def add3(a, b, c):
    a = 50
    print('a:', id(a), 'b:', id(b), 'c:', id(c))
    result = a + b + c
    return result



x, y, z = 20, 5, 15
print('x:', id(x), 'y:', id(y), 'z:', id(z))

result = add3(x, y, z)
print('Addition of 3 Numbers :', result)

print(x)

# print(add3(12, 30, 40))


