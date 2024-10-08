# python program to implement variable length keyword arguments

def fun1(**kwargs):
    print(type(kwargs))
    print(kwargs)

fun1(rollno=12, name='Ajay', address='Delhi')

def fun2(**kwargs):
    for k in kwargs:
        print(k, kwargs[k])

fun2(rollno=12, name='Ajay', address='Delhi')

def fun3(a, b, *args, c, **kwargs):
    print(a, b, c, args, kwargs)

fun3(10, 20, 11, 22, 33, c=15, rollno=12, name='Ajay', address='Delhi')

