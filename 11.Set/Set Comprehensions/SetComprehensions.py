# python program to implement set comprehensions

# Creating - Emtpy Iterables => (list, tuple, dictionary, set, string)
L = []      # empty list
print(type(L))
# Output : <class 'list'>

t = ()      # empty tuple
print(type(t))

# Output : <class 'tuple'>

d = {}      # empty dictionary
print(type(d))
# Output : <class 'dict'>

s = set()   # empty set
print(s)
# Output : set()
print(type(s))
# Output : <class 'set'>

string = str('')  # empty string
print(string)
# Output : ''

# Set Comprehensions
S1 = {x for x in range(10)}
print(S1)
# Output : {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

S1 = set(x for x in range(5))
print(S1)
# Output : {0, 1, 2, 3, 4}

S2 = {x**2 for x in [-2, -1, 0, 1, 2]}
print(S2)
# Output : {0, 1, 4}

S3 = {x for x in (10, 5, 7, 8, 6, 4) if x % 2 == 0 }
print(S3)
# Output : {8, 10, 4, 6}

S4 = {x.upper() for x in 'python'}
print(S4)
# Output : {'N', 'P', 'O', 'H', 'T', 'Y'}

# S5 = {10, 12.5, 'hello', (1, 2, 3)}
# S6 = {10, 12.5, [1, 2, 3]}
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'list'

# S6 = {10, 12.5, {1, 2, 3}}
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'set'

# S6 = {10, 12.5, {1, 2, 3}, [1, 2, 3]}
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'set'