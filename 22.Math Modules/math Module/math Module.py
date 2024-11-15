# python program to use the math module

import math

print(math.ceil(12.3))
# Output : 13

print(math.floor(11.9))
# Output : 11

print(math.fabs(-5))
# Output : 5.0

print(math.fabs(5))
# Output : 5.0

print(math.fmod(14, 3))
# Output : 2.0

print(math.remainder(14, 3))
# Output : -1.0

print(math.remainder(16, 3))
# Output : 1.0



print(math.sqrt(25))
# Output : 5.0

print(math.sqrt(27))
# Output : 5.196152422706632

print(math.isqrt(25))
# Output : 5

print(math.isqrt(27))
# Output : 5

print(math.pow(5, 2))
# Output : 25.0

print(math.factorial(5))
# Output : 120



print(math.gcd(35, 21))
# Output : 7

print(math.perm(5, 2))
# Output : 20

print(math.comb(5, 2))
# Output : 10



print(math.prod([1, 2, 3, 4, 5]))
# Output : 120

print(math.fsum([1, 2, 3, 4, 5]))
# Output : 15.0



print(math.radians(30))
# Output : 0.5235987755982988

'''print(math.degree(0.52))
Output : Traceback (most recent call last):

  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'degree'. Did you mean: 'degrees'?'''

print(math.degrees(0.52))
# Output : 29.79380534680281

print(math.degrees(0.5235987755982988))
# Output : 29.999999999999996



print(math.sin(30))
# Output : -0.9880316240928618

print(math.sin(math.radians(30)))
# Output : 0.49999999999999994

print(math.cos(math.radians(30)))
# Output : 0.8660254037844387

print(math.cos(math.radians(60)))
# Output : 0.5000000000000001

print(math.tan(math.radians(45)))
# Output : 0.9999999999999999



print(math.log(100))
# Output : 4.605170185988092

print(math.log10(100))
# Output : 2.0

print(math.log2(1024))
# Output : 10.0



print(math.pi)
# Output : 3.141592653589793

print(math.e)
# Output : 2.718281828459045

print(math.inf)
# Output : inf

print(math.nan)
# Output : nan
