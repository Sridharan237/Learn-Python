# python program to use the Fraction class available in the fractions module

import fractions

f1 = fractions.Fraction(1, 2)
print(f1)
# Output : Fraction(1, 2)

print(f1)
# Output : 1/2

f2 = fractions.Fraction(0.2)
print(f2)
# Output : Fraction(3602879701896397, 18014398509481984)

print(print(f2))
# Output : 3602879701896397/18014398509481984

print(f2.limit_denominator(10))
# Output : Fraction(1, 5)

print(f2)
# Output : 3602879701896397/18014398509481984

f2 = f2.limit_denominator(10)
print(f2)
# Output : Fraction(1, 5)

print(f2)
# Output : 1/5

f3 = fractions.Fraction('0.3')
print(f3)
# Output : Fraction(3, 10)

print(f3)
# Output : 3/10

# Fraction Class : Attributes -> numerator, denominator
print(f3.numerator)
# Output : 3

print(f3.denominator)
# Output : 10

print(f1)
# Output : Fraction(1, 2)

print(f2)
# Output : Fraction(1, 5)

print(f3)
# Output : Fraction(3, 10)

# operations performed on Fraction Class Objects

print(f1 + f2)
# Output : 7/10

print(f1 - f2)
# Output : 3/10

print(f1 * f2)
# Output : 1/10

print(f1 / f2)
# Output : 5/2

print(f1 % f2) # 1/2 % 1/5 = 0.5 % 0.2 = 0.1
# Output : 1/10

print(f1 // f2)
# Output : 2
