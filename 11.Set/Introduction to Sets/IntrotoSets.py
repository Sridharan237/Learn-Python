# python program to implement set datatype in python

s1 = {1, 2, 3, 4, 'Jack', 3.4, 'Jack'}
print(s1)
# Output : {1, 2, 3.4, 3, 4, 'Jack'}

# print(s1[0])

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'set' object is not subscriptable

print(type(s1))
# Output : <class 'set'>

# s2 = set(1, 2, 3, 4, 5)

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: set expected at most 1 argument, got 5

s2 = set( (1, 2, 3, 4, 5) )
print(s2)
# Output : {1, 2, 3, 4, 5}

s3 = set('python')
print(s3)
# Output : {'t', 'p', 'o', 'n', 'y', 'h'}

print(s3)
# Output : {'t', 'p', 'o', 'n', 'y', 'h'}

print(s3)
# Output : {'t', 'p', 'o', 'n', 'y', 'h'}

s4 = {10, 20, 30, 40, 50}
print(s4)
# Output : {50, 20, 40, 10, 30}

# s4[0] = 25

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'set' object does not support item assignment

s4.discard(50)
print(s4)
# Output : {20, 40, 10, 30}

s4.add(100)
print(s4)
# Output : {20, 100, 40, 10, 30}

s4.add(100)
print(s4)
# Output : {20, 100, 40, 10, 30}

s4.add(30)
print(s4)
# Output : {20, 100, 40, 10, 30}

s4.add(50)
print(s4)
# Output : {50, 20, 100, 40, 10, 30}

print(len(s4))
# Output : 6

