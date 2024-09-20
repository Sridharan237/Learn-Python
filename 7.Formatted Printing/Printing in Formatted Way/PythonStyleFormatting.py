# python program to implement python style of formatting

a = 22
b = 7
c = a / b

print('Division of {} and {} is {}'.format(a, b, c))
# Output : Division of 22 and 7 is 3.142857142857143

print('Division of {0} and {1} is {2}'.format(a, b, c))
# Output : Division of 22 and 7 is 3.142857142857143

print('Division of {2} and {1} is {0}'.format(a, b, c))
# Output : Division of 3.142857142857143 and 7 is 22

print('Division of {2} and {1} is {0}'.format(c, b, a))
# Output : Division of 22 and 7 is 3.142857142857143

print('Division of {0:10} and {1:15} is {2:2.4}'.format(a, b, c))
# Output : Division of         22 and               7 is 3.143

print('Division of {0:10} and {1:15} is {2:2.3}'.format(a, b, c))
# Output : Division of         22 and               7 is 3.14

print('Division of {0:10} and {1:15} is {2:.4}'.format(a, b, c))
# Output : Division of         22 and               7 is 3.143

print('Division of {0:10} and {1:15} is {2:.4f}'.format(a, b, c))
# Output : Division of         22 and               7 is 3.1429

print('Division of {0:<10} and {1:^15} is {2:.4f}'.format(a, b, c))
# Output : Division of 22         and        7        is 3.1429

x = 1234567890
print('{0:20,}'.format(x))
    # Output :    1,234,567,890

x = 1234567890.83999999974
# print('{0:20.4,f}'.format(x))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: Invalid format specifier '20.4,f' for object of type 'float'

print('{0:20,.4f}'.format(x))
# Output :   1,234,567,890.8400

print('{0:20_.4f}'.format(x))
# Output :   1_234_567_890.8400

print('Division of {0:<10} and {1:^15} is {2:.4E}'.format(a, b, c)
)
# Output : Division of 22         and        7        is 3.1429E+00

print('Division of {0:<10} and {1:^15} is {2:E}'.format(a, b, c))
# Output : Division of 22         and        7        is 3.142857E+00

print('Division of {0:<10} and {1:^15} is {2:e}'.format(a, b, c))
# Output : Division of 22         and        7        is 3.142857e+00

# f string -> new style of formatting in python

print(f'Division of {a:<10} and {b:^15} is {c:e}')
# Output : Division of 22         and        7        is 3.142857e+00

# print(f 'Division of {a:<10} and {b:^15} is {c:e}')
#   File "<stdin>", line 1
    # print(f 'Division of {a:<10} and {b:^15} is {c:e}')
#             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# SyntaxError: invalid syntax