# python program to implement Quantifiers in Regular Expressions 

from re import *

# re.match('a', 'a').group()

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 're' is not defined. Did you forget to import 're'?

print(match('a', 'a').group())
# Output : 'a'

print(match('a|b', 'a'))
# Output : <re.Match object; span=(0, 1), match='a'>

print(match('a|b', 'a').group())
# Output : 'a'

# match('abc', 'a').group()

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'NoneType' object has no attribute 'group'

print(match('abc', 'abc').group())
# Output : 'abc'

print(match('[abc]', 'bc').group())
# Output : 'b'

print(match('[abc]', 'abcd').group())
# Output : 'a'

print(match('[abc]', 'bcd').group())
# Output : 'b'

print(match('[abc]+', 'ccccc').group())
# Output : 'ccccc'

print(match('[abc]+', 'ccccc'))
# Output : <re.Match object; span=(0, 5), match='ccccc'>

print(match('[abc]+', 'abcabcabcbbcee'))
# Output : <re.Match object; span=(0, 12), match='abcabcabcbbc'>

print(match('[abc]+', 'abcabcabcbbcee').group())
# Output : 'abcabcabcbbc'

print(match('[abc]+', 'abcabcabcbbceeabcabc').group())
# Output : 'abcabcabcbbc'

print(match('[abc]+', 'abcabcabcbbceeabcabc'))
# Output : <re.Match object; span=(0, 12), match='abcabcabcbbc'>

print(match('[abc]*', '').group())
# Output : ''

print(match('[abc]{5}', 'ababab').group())
# Output : 'ababa'

print(match('[abc]{5,7}', 'ababababab').group())
# Output : 'abababa'