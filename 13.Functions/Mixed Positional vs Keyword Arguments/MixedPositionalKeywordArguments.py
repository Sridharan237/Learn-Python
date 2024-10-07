# python program to implement mixed positional and keyword arguments

def add1(a, b, c, d, e, f):
    return a+b+c+d+e+f

print('Addition :', add1(2, 5, 9, 5, 10, 20))
print('Addition :', add1(b=2, a=5, c=9, f=5, e=10, d=20))



def add2(a, b, /, c, d, e, f):
    return a+b+c+d+e+f

print('Addition :', add2(2, 5, 9, 5, f=10, e=20))
print('Addition :', add2(2, 5, d=9, e=5, f=10, c=20))

# print('Addition :', add2(a=10, b=5, 8, 6, 7, 5)) # SyntaxError: positional argument follows keyword argument



def add3(a, b, /, c, d, *, e, f):
    return a+b+c+d+e+f

print('Addition :', add3(2, 5, 6, 7, e=10, f=15))
print('Addition :', add3(2, 5, d=6, c=7, e=10, f=15))

def add4(a, b, /):
    return a+b

print('Addition :', add4(15, 10))

def add5(*, a, b):
    return a+b

print('Addition :', add5(a=1, b=2))


