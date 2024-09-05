a = 10
print(a)

a = 0b1010
print(a)

# a = 0o8

#   File "<stdin>", line 1
#     a = 0o8
#           ^
# SyntaxError: invalid digit '8' in octal literal

a = 0o12
print(a)

a = 0xA
print(a)

a = input("Enter a number : ")
print(a)
print(type(a))

a = int(input("Enter a number : "))

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '0b1010'

a = int(input("Enter a number : "), 2)
print(a)

a = 5 + 4j
print(a)

a = 0b1010 + 5j
print(a)

# a = 10 + 0b101j

#   File "<stdin>", line 1
#     a = 10 + 0b101j
#                  ^
# SyntaxError: invalid binary literal

# a = 10 + (0b101)j

#   File "<stdin>", line 1
#     a = 10 + (0b101)j
#                     ^
# SyntaxError: invalid syntax