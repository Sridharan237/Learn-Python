# python program to implement printable and non-printable - escape sequences

s = 'john'
print(s)    # Output : john

# s = 'john's'
#   File "<stdin>", line 1
#     s = 'john's'
#                ^
# SyntaxError: unterminated string literal (detected at line 1)

s = 'john\'s'
print(s)    # Output : "john's"

s = "john's"
print(s)    # Output : "john's"

s = """john"s"""
print(s)    # Output : 'john"s'

s = """john\'\'\'s"""
print(s)    # Output : "john'''s"

s = """john\'''s"""
print(s)    # Output : "john'''s"

s = """john\''''''''''''''''''''''''''s"""
print(s)    # Output : "john''''''''''''''''''''''''''s"

s = """john\''''''''''''''''''''''''''""""""""""""""""s"""
print(s)    # Output : "john''''''''''''''''''''''''''s"

s = """john\''''''''''''''''''''''''''""s"""
print(s)    # Output : 'john\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'""s'

s = 'abc\ndef'
print(s)    # Output : 'abc\ndef'

print(s)
# Output :
""" 
abc
def
"""

# print(r s)
#   File "<stdin>", line 1
#     print(r s)
#           ^^^
# SyntaxError: invalid syntax. Perhaps you forgot a comma?

# print(r{s})
#   File "<stdin>", line 1
#     print(r{s})
#           ^^^^
# SyntaxError: invalid syntax. Perhaps you forgot a comma?

print(r'abc\ndef\nhai') # Output : abc\ndef\nhai

print(r'abc\ndef')  # Output : abc\ndef

print('john\\s')    # Output : john\s

# print('\N{}')
#   File "<stdin>", line 1
#     print('\N{}')
#           ^^^^^^
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 0-2: malformed \N character escape

print('\N{pound sign}') # Output : £

s = '\N{pound sign}'
print(s)    # Output : '£'

s = '\N{dollar sign}'
print(s)    # Output : '$'

s = '\N{rupee sign}'
print(s)    # Output : '₨'

s = '\N{copyright sign}'
print(s)    # Output : '©'

s = '\N{yen sign}'
print(s)    # Output : '¥'

s = '\N{latin small letter a}'
print(s)    # Output : 'a'

s = '\N{superscript five}'
print(s)    # Output : '⁵'

s = '\N{subscript five}'
print(s)    # Output : '₅'

s = '\N{backspace}'         # Escape Sequence -> Non-printable - only returns hexadecimal code in string format
print(s)    # Output : '\x08'

s = '\N{Watch}'
print(s)    # Output : '⌚'