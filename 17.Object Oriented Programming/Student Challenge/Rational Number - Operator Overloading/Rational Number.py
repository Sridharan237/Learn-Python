# python program to implement class for rational number with operator overloading (+, -)

# class for rational number
class Rational:
    
    def __init__(self, p, q):
        self.numerator = p
        self.denominator = q
    
    # operator overloading (+)
    def __add__(self, other):
        numerator = self.numerator * other.denominator + self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        
        return Rational(numerator, denominator)

    # operator overloading (-)
    def __sub__(self, other):
        numerator = self.numerator * other.denominator - self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        
        return Rational(numerator, denominator)
    
    # method overriding (str)
    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

# creating objects for class Rational
r1 = Rational(2, 3)

r2 = Rational(2, 5)

print('Rational 1:', r1)
print('Rational 2:', r2)

print('Addition :', r1 + r2)

print('Subtraction :', r1 - r2)