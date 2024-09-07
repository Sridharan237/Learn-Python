a = 15
b = 4
c = a + b
print(c)

c = a - b
print(c)

# print(c = a * b)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'c' is an invalid keyword argument for print()

c = a * b
print(c)

# c = a * * b
#   File "<stdin>", line 1
#     c = a * * b
#             ^
# SyntaxError: invalid syntax

c = a ** b
print(c)

c.__sizeof__()

c = a / b
print(c)

c = a // b
print(c)

c = a % b
print(c)

x, y = 21, 4

c = x / y
print(c)

c = x // y
print(c)

c = x % y
print(c)