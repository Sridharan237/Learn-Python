# python program to find two roots (solve) for the quadratic equation   (ax^2 + bx + c = 0)

import math

a = int(input('Enter \'a\' value : '))
b = int(input('Enter \'b\' value : '))
c = int(input('Enter \'c\' value : '))

root1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)    # math.sqrt() -> will give ValueError : math domain error if the given input is negative because if we take squareroot for negative number then the result will in complex number and not in real number
root2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)

print('Root1 =', root1)
print('Root2 =', root2)