# python program to implement tuple => (1.immutable, 2.creation(using parantheses, using tuple function), 3.packing and unpacking)

t1 = ('Jack', 38.5, 45, 5+9j, 45)
print(t1)
# Output : ('Jack', 38.5, 45, (5+9j), 45)

print(type(t1))
# Output : <class 'tuple'>

print(t1[2])
# Output : 45

print(t1[-2])
# Output : (5+9j)

# Immutable - property of tuple

# t1[2] = 'Hai'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment



# tuple creation
t1 = (1, 2, 3, 4, 5)
print(t1)
# Output : (1, 2, 3, 4, 5)

t2 = () # empty tuple - cannot be updated further
print(t2)
# Output : ()

print(type(t2))
# Output : <class 'tuple'>

t1 = (1, 2, 3, 4, 5)
print(t1)
# Output : (1, 2, 3, 4, 5)

t3 = (10)
print(type(t3))
# Output : <class 'int'>

t3 = (10,)
print(t3)
# Output : (10,)

print(type(t3))
# Output : <class 'tuple'>

# t4 = tuple(1, 2, 3, 4, 5)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: tuple expected at most 1 argument, got 5

t4 = tuple((1, 2, 3, 4, 5))
print(t4)
# Output : (1, 2, 3, 4, 5)

print(type(t4))
# Output : <class 'tuple'>

t5 = tuple([1, 2, 3, 4, 5])
print(t5)
# Output : (1, 2, 3, 4, 5)

print(type(t5))
# Output : <class 'tuple'>

t6 = tuple('Python')
print(t6)
# Output : ('P', 'y', 't', 'h', 'o', 'n')

print(type(t6))
# Output : <class 'tuple'>





t1 = 10
print(t1)
# Output : 10

print(type(t1))
# Output : <class 'int'>

t1 = 10,
print(t1)
# Output : (10,)

print(type(t1))
# Output : <class 'tuple'>

t2 = 10, 20, 30, 40
print(t2)
# Output : (10, 20, 30, 40)

print(type(t2))
# Output : <class 'tuple'>

# Unpacking - tuple

a, b, c, d = t2
print(a)
# Output : 10

print(b)
# Output : 20

print(c)
# Output : 30

print(d)
# Output : 40

# Packing - list
L1 = [1, 2, 3]
print(L1)
# Output : [1, 2, 3]

a, b, c = 1, 2, 3

# Packing - list
L2 = [a, b, c]
print(L2)
# Output : [1, 2, 3]

print(type(L1))
# Output : <class 'list'>

# Unpacking - list
a, b, c = L1
print(print(a, b, c))
# Output : 1 2 3

a = 'H'
b = 'a'
c = 'i'

# Packing - string
string = a + b + c

print(a, b, c)  
# Output : 'S' 'K' 'Y'

# Unpacking - string
a, b, c = 'SKY'
print(a)
# Output : 'S'
print(b)
# Output : 'K'
print(c)
# Output : 'Y'

# Packing - tuple
t1 = a, b, c
print(t1)
# Output : ('S', 'K', 'Y')

print(type(t1))
# Output : <class 'tuple'>

# Packing - tuple
t1 = 10, 20, 30, 40, 50
print(t1)
# Output : (10, 20, 30, 40, 50)




# a, b, c = t1
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: too many values to unpack (expected 3)
# a, b, c* = t1
#   File "<stdin>", line 1
#     a, b, c* = t1
#              ^
# SyntaxError: invalid syntax

# Unpacking - tuple
a, b, c, d, e = t1
print(a, b, c, d, e)
# Output : (10, 20, 30, 40, 50)

print(a, b, c, d, e)
# Output : 10 20 30 40 50

# Unpacking tuple
a, b, *c = t1
print(a)
# Output : 10
print(b)
# Output : 20
print(c)
# Output : [30, 40, 50]

# Unpacking - tuple
a, *b, c = t1
print(a)
# Output : 10
print(b)
# Output : [20, 30, 40]
print(c)
# Output : 50
