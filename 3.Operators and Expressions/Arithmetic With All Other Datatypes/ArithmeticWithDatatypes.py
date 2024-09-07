# python program to perform arithmetic operations on all datatypes

a, b = 10, 5

x = a + b
print(x)
# Output : 15

x = a - b
print(x)
# Output : 5

x = a * b
print(x)
# Output : 50

x = a / b
print(x)
# Output : 2.0

x = a // b
print(x)
# Output : 2

x = a % b
print(x)
# Output : 0

f = 1.5
x = a + f
print(x)
# Output : 11.5

x = a - f
print(x)
# Output : 8.5

x = a * f
print(x)
# Output : 15.0

x = a / f
print(x)
# Output : 6.666666666666667

x = a // f
print(x)
# Output : 6.0

print(5 // 10.5)
# Output : 0.0

x = a % f
print(x)
# Output : 1.0

print(10 // 2.0)
# Output : 5.0

x = a + True
print(x)
# Output : 11

x = a - True
print(x)
# Output : 9

x = a * False
print(x)
# Output : 0

x = a / False
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero

x = a // True
print(x)
# Output : 10

x = a % 0
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: integer modulo by zero

c = 5 + 10j
print(complex(5.3, 4.5))
# Output : (5.3+4.5j)

x = a + c
print(c)
# Output : (5+10j)

x = a - c
print(x)
# Output : (5-10j)

x = a * c
print(x)
# Output : (50+100j)

x = a / c
print(x)
# Output : (0.4-0.8j)

x = a // c
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for //: 'int' and 'complex'

x = a % c
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for %: 'int' and 'complex'

s = 'Hi'
print(2*'Hi')
# Output : HiHi

print(x * s)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can't multiply sequence by non-int of type 'complex'

print(a * s)
# Output : HiHiHiHiHiHiHiHiHiHi

print('Hi' + 'Hello')
# Output : HiHello