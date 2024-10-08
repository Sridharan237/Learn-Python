# python program to implement variable length positional arguments

# Variable Length Positional Arguments

def fun1(*args):
    print(type(args), args)

fun1()
fun1(10)
fun1(10, 20)
fun1(10, 20, 30)
fun1(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
fun1(10, 'hello', 24.75, True)


def fun2(a, b, *args):
    print(a, b, args)

# fun2()
# Output : TypeError: fun2() missing 2 required positional arguments: 'a' and 'b'
fun2(11, 22)
fun2(11, 22, 33, 44, 55, 66, 77)


def fun3(*args, a, b):
    print(a, b, args)

# fun3()
# Output : TypeError: fun3() missing 2 required keyword-only arguments: 'a' and 'b'
# fun3(1, 2, 3, 4, 5)
# Output : TypeError: fun3() missing 2 required keyword-only arguments: 'a' and 'b'
fun3(1, 2, 3, 4, 5, b=10, a=11)


# Packing and Unpacking - lists
a, b, c = 10, 20, 30

L = [a, b, c]   # Packing

x, y, z = L     # Unpacking

# Unpacking Arguments
def fun4(a, b, c):
    print(a, b, c)

L1 = [11, 22, 33]

fun4(L1[0], L1[1], L1[2])
# fun4(L1)
# Output : TypeError: fun4() missing 2 required positional arguments: 'b' and 'c'
fun4(*L1)   # *L1 => starred expression
# Output : 1


# Multiple Return Values
def fun5(a, b, c):
    return a+1, b+1, c+1

x, y, z = fun5(10, 20, 30)
print(x, y, z)

t = fun5(10, 20, 30)
print(t)


