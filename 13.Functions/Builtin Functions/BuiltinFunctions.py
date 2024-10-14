# python program to implement various builtin functions in python in alphabetical order

print(abs(5))
# Output : 5

print(abs(-5))
# Output : 5

print(abs(4-3j))
# Output : 5.0

print(ascii(65))
# Output : '65'

print(ascii('hello'))
# Output : "'hello'"


# ascii(hello)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'hello' is not defined. Did you mean: 'help'?

# ascii('\u002')
#   File "<stdin>", line 1
#     ascii('\u002')
#           ^^^^^^^
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 0-4: truncated \uXXXX escape

print(ascii('\u0021'))
# Output : "'!'"

ba = bytearray(5)
print(ba)
# Output : bytearray(b'\x00\x00\x00\x00\x00')

print(ba)
bytearray(b'\x00\x00\x00\x00\x00')
ba = bytearray('abcde'.encode())
print(ba)
# Output : bytearray(b'abcde')

# ba = bytearray('abcde')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: string argument without an encoding

for x in ba:
  print(x)
''' Output : 
97
98
99
100
101
'''

ba.append(105)
print(ba)
# Output : bytearray(b'abcdei')

b = bytes(5)
print(b)
# Output : b'\x00\x00\x00\x00\x00'

print(b)
# Output : b'\x00\x00\x00\x00\x00'

b = bytes('abc'.encode())
print(b)
# Output : b'abc'

print(callable(len))
# Output : True

print(callable(callable))
# Output : True

# callable(myFunc)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'myFunc' is not defined

print(callable(b))
# Output : False

print(chr(65))
# Output : 'A'

print(complex(5, 6))
# Output : (5+6j)

# dict(for x, y in zip([1, 2, 3], ['A', 'B', 'C']))
#   File "<stdin>", line 1
#     dict(for x, y in zip([1, 2, 3], ['A', 'B', 'C']))
#          ^^^
# SyntaxError: invalid syntax

# dict(for item in zip([1, 2, 3], ['A', 'B', 'C']))
#   File "<stdin>", line 1
#     dict(for item in zip([1, 2, 3], ['A', 'B', 'C']))
#          ^^^
# SyntaxError: invalid syntax

print(dict(zip([1, 2, 3], ['A', 'B', 'C'])))
# Output : {1: 'A', 2: 'B', 3: 'C'}

print(dir(dict))
# Output : ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

print(divmod(6, 3))
# Output : (2, 0)

print(divmod(2.5, 1.25))
# Output : (2.0, 0.0)

for x in enumerate(['A', 'B', 'C']):
  print(x)
''' Output : 
(0, 'A')
(1, 'B')
(2, 'C')
'''

iterator = enumerate(['A', 'B', 'C', 'D', 'E'])
print(next(iterator))
# Output : (0, 'A')

print(next(iterator))
# Output : (1, 'B')

print(next(iterator))
# Output : (2, 'C')

print(next(iterator))
# Output : (3, 'D')

print(next(iterator))
# Output : (4, 'E')

# next(iterator)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

iterator = enumerate(['A', 'B', 'C', 'D', 'E'])
print(next(iterator))
# Output : (0, 'A')

print(next(iterator))
# Output : (1, 'B')

print(list(iterator))
# Output : [(2, 'C'), (3, 'D'), (4, 'E')]

# next(iterator)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

expression = eval('2**4 + 9')
print(expression)
# Output : 25

print(type(expression))
# Output : <class 'int'>

# statements = 'x = 10\ny = 20\nprint('x+y :', x+y)'
#   File "<stdin>", line 1
#     statements = 'x = 10\ny = 20\nprint('x+y :', x+y)'
#                                          ^
# SyntaxError: invalid syntax

statements = 'x = 10\ny = 20\nprint(\'x+y :\', x+y)'
print(print(statements))
''' Output : 
x = 10
y = 20
print('x+y :', x+y)'''

print(exec(statements))
# Output : x+y : 30

print(x)
# Output : 10

print(y)
# Output : 20

L = [1, 2, 3, 4, 5]
itr = filter(lambda x : x % 2 == 0, L)
print(print(itr))
# Output : <filter object at 0x0000028C9BFBD210>

print(next(itr))
# Output : 2

itr = filter(lambda x : x % 2 == 0, L)
print(list(itr))
# Output : [2, 4]


# itr = filter(lambda x+y : x % 2 == 0 and y % 2 == 0, L, [10, 11, 12])
#   File "<stdin>", line 1
#     itr = filter(lambda x+y : x % 2 == 0 and y % 2 == 0, L, [10, 11, 12])
#                          ^
# SyntaxError: invalid syntax

# itr = filter(lambda x, y : x % 2 == 0 and y % 2 == 0, L, [10, 11, 12])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: filter expected 2 arguments, got 3

fs = frozenset([9, 20, 11, 20, 15, 11])
print(fs)
# Output : frozenset({9, 11, 20, 15})

print(globals())
# Output : {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'ba': bytearray(b'abcdei'), 'x': 10, 'b': b'abc', 'expression': 25, 'statements': "x = 10\ny = 20\nprint('x+y :', x+y)", 'y': 20, 'L': [1, 2, 3, 4, 5], 'itr': <filter object at 0x0000028C9BF86D70>, 'fs': frozenset({9, 11, 20, 15})}

print(locals())
# Output : {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'ba': bytearray(b'abcdei'), 'x': 10, 'b': b'abc', 'expression': 25, 'statements': "x = 10\ny = 20\nprint('x+y :', x+y)", 'y': 20, 'L': [1, 2, 3, 4, 5], 'itr': <filter object at 0x0000028C9BF86D70>, 'fs': frozenset({9, 11, 20, 15})}

s = 'abc'
print(hasattr(s, 'lower'))
# Output : True

print(hasattr(s, 'isdigit'))
# Output : True

print(hasattr(s, 'hello'))
# Output : False

print(hash(s))
# Output : 6859523775661339212

print(help(s.isdigit))
''' Output : 

Help on built-in function isdigit:

isdigit() method of builtins.str instance
    Return True if the string is a digit string, False otherwise.

    A string is a digit string if all characters in the string are digits and there
    is at least one character in the string.
'''

print(hex(10))
# Output : '0xa'

print(id(100))
# Output : 140732503107096

input = input('Enter the message : ')
# Output :=> Enter the message : hello

print(print(input))
# Output : hello

print(int(15.45))
# Output : 15

print(int('15'))
# Output : 15

n = 5
print(isinstance(n, int))
# Output : True

print(isinstance(n, float))
# Output : False

print(issubclass(int, object))
# Output : True

# issubclass(stack, collections)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'stack' is not defined

L = [1, 2, 3, 4, 5]
iterator = iter(L)
print(next(iterator))
# Output : 1

print(next(iterator))
# Output : 2

print(next(iterator))
# Output : 3

print(next(iterator))
# Output : 4

print(next(iterator))
# Output : 5

# next(iterator)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

print(len('abc'))
# Output : 3

print(list('abc'))
# Output : ['a', 'b', 'c']

print(locals())
# Output : {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'ba': bytearray(b'abcdei'), 'x': 10, 'b': b'abc', 'expression': 25, 'statements': "x = 10\ny = 20\nprint('x+y :', x+y)", 'y': 20, 'L': [1, 2, 3, 4, 5], 'itr': <filter object at 0x0000028C9BF86D70>, 'fs': frozenset({9, 11, 20, 15}), 's': 'abc', 'input': 'hello', 'n': 5, 'iterator': <list_iterator object at 0x0000028C9C0FBC10>}

iterator = map(lambda x : x**2, [1, 2, 3, 4, 5])
print(next(iterator))
# Output : 1

print(next(iterator))
# Output : 4

print(next(iterator))
# Output : 9

print(next(iterator))
# Output : 16

print(next(iterator))
# Output : 25

# next(iterator)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

iterator = map(lambda x, y : x + str(y), ['A', 'B', 'C'], [1, 2, 3])
print(next(iterator))
# Output : 'A1'

print(next(iterator))
# Output : 'B2'

print(next(iterator))
# Output : 'C3'

# next(iterator)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

iterator = map(lambda x : x**2, [1, 2, 3, 4, 5])
print(print(list(iterator)))
# Output : [1, 4, 9, 16, 25]

iterator = map(lambda x : x**2, [1, 2, 3, 4, 5])
print(next(iterator))
# Output : 1

print(list(iterator))
# Output : [4, 9, 16, 25]

# next(iterator)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
L = [1, 2, 3, 4, 5]
print(max(L))
# Output : 5

print(min(L))
# Output : 1

L = ['a', 'b', 'c']
print(max(L))
# Output : 'c'

print(min(L))
# Output : 'a'

print(max(L, key=len))
# Output : 'a'

print(min(L, key=len))
# Output : 'a'

L = [1, 2, 3]
iterator = iter(L)
print(next(iterator))
# Output : 1

print(next(iterator))
# Output : 2

print(next(iterator))
# Output : 3

# next(iterator)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

print(dir(object))
# Output : ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

obj = object()
print(print(obj))
# Output : <object object at 0x0000028C9BCA88F0>

# print(obj.)
#   File "<stdin>", line 1
#     print(obj.)
#               ^
# SyntaxError: invalid syntax

# print(obj.list)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'object' object has no attribute 'list'

print(oct(10))
# Output : '0o12'

# open()  => used to open a file
print(ord('A'))
# Output : 65

print(pow(2, 4))
# Output : 16

print('hello, how are you')
# Output : hello, how are you

print(range(10))
# Output : range(0, 10)

iterator = range(10)
print(range(10))
# Output : range(0, 10)

# next(iterator)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'range' object is not an iterator

print(list(iterator))
# Output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(10)))
# Output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

L = [1, 2, 3, 4, 5]
print(reversed(L))
# Output : <list_reverseiterator object at 0x0000028C9C453CD0>

iterator = reversed(L)
print(next(iterator))
# Output : 5

print(next(iterator))
# Output : 4

print(next(iterator))
# Output : 3

print(next(iterator))
# Output : 2

print(next(iterator))
# Output : 1

# next(iterator)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

iterator = reversed(L)
print(list(iterator))
# Output : [5, 4, 3, 2, 1]

print(round(12.45))
# Output : 12

print(round(12.57))
# Output : 13

s = set([1, 2, 3, 3])
print(s)
# Output : {1, 2, 3}

sliced = slice(3)
L = [1, 2, 3, 4, 5]
print(L[sliced])
# Output : [1, 2, 3]

L = [3, 5, 2, 1, 6]
print(sorted(L))
# Output : [1, 2, 3, 5, 6]

print(sorted(L, reverse=True))
# Output : [6, 5, 3, 2, 1]

L = [1, 2 ,3, 4, 5]
string = str(L)
print(string)
# Output : '[1, 2, 3, 4, 5]'

print(sum(L))
# Output : 15

print(tuple([1, 2, 3, 4, 5]))
# Output : (1, 2, 3, 4, 5)

print(type(L))
# Output : <class 'list'>

iterator = zip([1, 2, 3, 4, 5], ['A', 'B', 'C', 'D', 'E'])
print(next(iterator))
# Output : (1, 'A')

print(next(iterator))
# Output : (2, 'B')

print(next(iterator))
# Output : (3, 'C')

print(next(iterator))
# Output : (4, 'D')

print(next(iterator))
# Output : (5, 'E')

# next(iterator)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration