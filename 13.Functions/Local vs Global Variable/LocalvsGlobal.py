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



# built-in functions => locals(), globals()

def fun5(a, b):
    c = a + b
    print(c)
    print(locals())
    # Output : {'a': 4, 'b': 8, 'c': 12}

    print(globals())
    # Output : {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001F11565BDA0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'D:\\Learn-Github-Repositories\\Learn Python Programming - Beginner to Master\\13.Functions\\Local vs Global Variable\\LocalvsGlobal.py', '__cached__': None, 'g': 15, 'fun1': <function fun1 at 0x000001F1158E8EA0>, 'fun2': <function fun2 at 0x000001F1158E8CC0>, 'fun4': <function fun4 at 0x000001F1158E8F40>, 'fun5': <function fun5 at 0x000001F1158E8FE0>}

fun5(4, 8)

print(locals())
# Output : {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001F11565BDA0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'D:\\Learn-Github-Repositories\\Learn Python Programming - Beginner to Master\\13.Functions\\Local vs Global Variable\\LocalvsGlobal.py', '__cached__': None, 'g': 15, 'fun1': <function fun1 at 0x000001F1158E8EA0>, 'fun2': <function fun2 at 0x000001F1158E8CC0>, 'fun4': <function fun4 at 0x000001F1158E8F40>, 'fun5': <function fun5 at 0x000001F1158E8FE0>}

print(globals())
# Output : {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001F11565BDA0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'D:\\Learn-Github-Repositories\\Learn Python Programming - Beginner to Master\\13.Functions\\Local vs Global Variable\\LocalvsGlobal.py', '__cached__': None, 'g': 15, 'fun1': <function fun1 at 0x000001F1158E8EA0>, 'fun2': <function fun2 at 0x000001F1158E8CC0>, 'fun4': <function fun4 at 0x000001F1158E8F40>, 'fun5': <function fun5 at 0x000001F1158E8FE0>}
