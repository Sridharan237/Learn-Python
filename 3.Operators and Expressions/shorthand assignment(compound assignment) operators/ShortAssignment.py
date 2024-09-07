# python program to implement shorthand assignment(compund assignment) operators

a = 1
a = a + 1
print(a)

# a + = 1
#   File "<stdin>", line 1
#     a + = 1
#         ^
# SyntaxError: invalid syntax

a += 1  # also called as "Arithmetic Assignment operators" here
print(a)

count = 0
count = count + 1
count += 1
print(count)

count += 1
print(count)

a, b = 10, 5
a &= b # a = a & b      #   # also called as "Bitwise Assignment operators" here
print(a)