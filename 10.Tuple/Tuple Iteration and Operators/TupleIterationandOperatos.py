# python program to implement tuple iteration and operators

# tuple iteration
t1 = ('Jack', 45, 38.6, False, 5+6j, 'Jill', 45)
print(t1)
#Output : ('Jack', 45, 38.6, False, (5+6j), 'Jill', 45)

for x in t1:
    print(x)
''' Output : 
Jack
45
38.6
False
(5+6j)
Jill
45
'''

for i in range(len(t1)):
    print(t1[i])
'''Output : 
Jack
45
38.6
False
(5+6j)
Jill
45
'''

# tuple operators


# index => []
print(t1[1])
#Output : 45
print(t1[4])
#Output : (5+6j)

# t1[4] = 25
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment

print(t1[-1])
#Output : 45
print(t1[-2])
#Output : 'Jill'


# slice => [:]

print(t1[:])
#Output : ('Jack', 45, 38.6, False, (5+6j), 'Jill', 4
print(t1[::])
#Output : ('Jack', 45, 38.6, False, (5+6j), 'Jill', 45)
print(t1[3:])
#Output : (False, (5+6j), 'Jill', 45)
print(t1[3:len(t1)])
#Output : (False, (5+6j), 'Jill', 45)
print(t1[3:len(t1):-1])
#Output : ()
print(t1[3:len(t1):-1])    # Here, it returns empty tuple because when step is negative then start should be less than end(start < end) otherwise it will return empty tuple
# Output : ()
print(t1[-3:-(len(t1)-1)])
#Output : ()
print(t1[-3:-(len(t1)-1):-1])
#Output : ((5+6j), False, 38.6)
print(t1[:-(len(t1)-1):-1])
#Output : (45, 'Jill', (5+6j), False, 38.6)
print(t1[:-(len(t1)+1):-1])
#Output : (45, 'Jill', (5+6j), False, 38.6, 45, 'Jack')
print(t1[::-1])
#Output : (45, 'Jill', (5+6j), False, 38.6, 45, 'Jack')
print(t1[::2])
#Output : ('Jack', 38.6, (5+6j), 45)


t1 = (1, 2, 3)
t2 = 4, 5, 6
print(t1)
#Output : (1, 2, 3)

print(t2)
#Output : (4, 5, 6)

print(t1, t2)
#Output : ((1, 2, 3), (4, 5, 6))

t3 = (t1, t2)
print(t3)
#Output : ((1, 2, 3), (4, 5, 6))

# concatenation => +

print(t1 + t2)
#Output : (1, 2, 3, 4, 5, 6)

print(t1)
#Output : (1, 2, 3)

print(t2)
#Output : (4, 5, 6)

t4 = t1 + t2
print(t4)
#Output : (1, 2, 3, 4, 5, 6)

# print(t1 + [7, 8, 9])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate tuple (not "list") to tuple

print(t1 + tuple([7, 8, 9]))
#Output : (1, 2, 3, 7, 8, 9)

# repetition => *

print(t1 * 2)
#Output : (1, 2, 3, 1, 2, 3)
print(t2 * 3)
#Output : (4, 5, 6, 4, 5, 6, 4, 5, 6)

# t2 * 2.5
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can't multiply sequence by non-int of type 'float'

temp = t1 * 3
print(temp)
#Output : (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Membership Operators => in, not in

print(3 in t1)
#Output : True

print(5 in t1)
#Output : False

print(5 not in t1)
#Output : True

print((2, 1) in t1)
#Output : False

print(2, 1 in t1)
#Output : (2, True)

print((1, 2) in t1)
#Output : False

t4 = (1, 2, (1, 2))
print((1, 2) in t1)
#Output : False

print((1, 2) in t4)
#Output : True

print((2, 1) in t4)
#Output : False






# Important

T = ('python', [10, 20, 30], (40, 50))

print(T)
# Output : ('python', [10, 20, 30], (40, 50))

print(T[1:2][1])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: tuple index out of range

print(T[:][2])  # (40, 50)
