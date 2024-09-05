i = 15
f = 16.59
b = True
c = 10 + 6j
s1 = 'john'
s2 = '125'
s3 = '12.56'
s4 = 'True'

# s5 = '5 + 18j"
#   File "<stdin>", line 1
#     s5 = '5 + 18j"
#          ^
# SyntaxError: unterminated string literal (detected at line 1)

s5 = '5 + 18j'
print(int(f))

print(int(b))

# print(int(c))

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

# print(int(s1))

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: 'john'

print(int(s2))

# print(int(s3))

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '12.56'

print(float(i))

print(float(f))

print(float(b))


# print(float(c))

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: float() argument must be a string or a real number, not 'complex'

print(float(s3))

# print(float(s1))

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: could not convert string to float: 'john'

print(float(s2))

print(bool(i))

print(bool(0))

print(bool(f))

print(bool(c))

print(bool(b))

print(bool(s1))

print(bool(s2))

print(bool(s3))

print(bool(s4))

print(bool(''))

print(bool(' '))

print(complex(i))

print(complex(f))

print(complex(b))

print(complex(c))

# print(complex(s1))

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: complex() arg is a malformed string

print(complex(s2))

print(complex(s3))

# print(complex(s4))

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: complex() arg is a malformed string

# print(complex(s5))

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: complex() arg is a malformed string

print(s5)

# print(complex(s5))

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: complex() arg is a malformed string

print(complex('5+10j'))     # o/p : (5+10j)