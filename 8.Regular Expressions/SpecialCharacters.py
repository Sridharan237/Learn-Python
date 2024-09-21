# python program to implement special characters in regular expressions in python

from re import *

s = '[a-z]'
print(match(s, 'hello'))
# Output : <re.Match object; span=(0, 1), match='h'>

print(match(s, 'hello').group())
# Output : 'h'

pattern = '[a-z]'
string = 'abc'
substring = match(pattern, string).group()
print(substring)
# Output : a

print(match('[a-z]', 'a'))
# Output : <re.Match object; span=(0, 1), match='a'>

print(match('[a-z]', 'a').group())
# Output : a

print(match('[a-z]+', 'abacbckjfb').group())
# Output : abacbckjfb

print(match('[a-z]', 'a').group())
# Output : 'a'

print(match('[a-z]', 'adjfdjflkdfoemciek').group())
# Output : 'a'

print(match('[a-z]+', 'adjfdjflkdfoemciek').group())
# Output : 'adjfdjflkdfoemciek'

print(match('[a-z A-Z 0-9]+', 'adjfdjflkdfoeAKmDciedkdD03930').group())
# Output : 'adjfdjflkdfoeAKmDciedkdD03930'

# print(match('[^a-z]+', 'adjfdjflkdfoeAKmDciedkdD03930').group())

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'NoneType' object has no attribute 'group'

print(match('[^a-z]+', 'AKmDciedkdD03930').group())
# Output : 'AK'

# print(match('[0-9]+', 'adjfdjflkdfoeAKmDciedkdD03930').group())

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'NoneType' object has no attribute 'group'

# print(match('^[a-z]+ | [A-Z]+', 'AB12').group())

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'NoneType' object has no attribute 'group'

# print(match('([^a-z]+) | [A-Z]+', 'AB12').group())

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'NoneType' object has no attribute 'group'

# print(match('([^a-z]+) | ([A-Z]+)', 'AB12').group())

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'NoneType' object has no attribute 'group'

# print(match('([^a-z]+) | ([A-Z]+)', 'AB').group())

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'NoneType' object has no attribute 'group'

print(match('([^a-z]+)|([A-Z]+)', 'AB').group())
# Output : 'AB'

print(match('([^a-z]+)|([A-Z]+)', 'AB12').group())
# Output : 'AB12'

print(match('.', 'AodfldjfldjiEARAG343B12').group())
# Output : 'A'

# print(match('[.]+', 'AodfldjfldjiEARAG343B12').group())

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'NoneType' object has no attribute 'group'

print(match('.+', 'AodfldjfldjiEARAG343B12').group())
# Output : 'AodfldjfldjiEARAG343B12'

print(match('^Hell', 'Hello World').group())
# Output : 'Hell'

# print(match('orld$', 'Hello World').group())

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'NoneType' object has no attribute 'group'

# print(match('orld $', 'Hello World').group())

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'NoneType' object has no attribute 'group'

# print(match('orld$', 'Hello World').group())

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'NoneType' object has no attribute 'group'

# print(match('$orld', 'Hello World').group())

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'NoneType' object has no attribute 'group'

# print(match('rld$', 'Hello World').group())

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'NoneType' object has no attribute 'group'

# print(match('orld$', 'rld').group())

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'NoneType' object has no attribute 'group'

print(match('orld$', 'orld').group())
# Output : 'orld'

# print(match('orld$', 'wampireorld').group())

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'NoneType' object has no attribute 'group'

# print(match('orld$', 'wampire orld').group())

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'NoneType' object has no attribute 'group'

x = r'^Hell'
c = compile(x)
r = c.search('Hello World')
print(r.group())
# Output : 'Hell'

x = r'orld$'
c = compile(x)
r = c.search('Hello World')
print(r.group())
# Output : 'orld'

# print(match('\s', 'abc').group())

# <stdin>:1: SyntaxWarning: invalid escape sequence '\s'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'NoneType' object has no attribute 'group'

print(match('\n', '\n').group())
# Output : '\n'

print(match('\n', '\nabc').group())
# Output : '\n'