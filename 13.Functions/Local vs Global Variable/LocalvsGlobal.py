# python program to implement global and local variable

# global variable defined after function call so that line will not exectued
# def fun(a, b):     # a, b, c - local variables of function fun1
#     c = a+b
#     print('Local inside function fun1 \'c\' :', c)
#     print('Global inside function fun1 \'g\' :', g)
#
# fun(10, 20)     # Output : NameError: name 'g' is not defined

g = 10  # global variable

def fun1(a, b):     # a, b, c - local variables of function fun1
    c = a+b
    print('Local inside function fun1 \'c\' :', c)
    print('Global inside function fun1 \'g\' :', g)

fun1(10, 20)

g = 10  # global variable

def fun2(a, b):     # a, b, c - local variables of function fun1
    g = 20
    c = a+b
    print('Local inside function fun2 \'c\' :', c)
    print('local inside function fun2 \'g\' :', g)

print('Global outside function fun2 \'g\' :', g)

fun2(10, 20)

# g = 10      # global variable
#
# def fun3(a, b):
#     g = g + 5
#     c = a + b
#     print('Local inside function fun3 \'c\' :', c)
#     print('global inside function fun3 \'g\' :', g)
#
# print('Global outside function fun3 \'g\' :', g)
#
# fun3(10, 20)      # Output : UnboundLocalError: cannot access local variable 'g' where it is not associated with a value

g = 10      # global variable

def fun4(a, b):
    global g
    g = g + 5
    c = a + b
    print('Local inside function fun4 \'c\' :', c)
    print('global inside function fun4 \'g\' :', g)

print('Global outside function fun4 \'g\' :', g)

fun4(10, 20)

print('Global outside function fun4 \'g\' :', g)