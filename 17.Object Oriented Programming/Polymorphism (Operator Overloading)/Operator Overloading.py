# python program to implement polymorphism achieved through operator overloading

# Example 1 => program to show operator overloading -> for adding 2 vectors

# class for Vector -> Vector - (x, y) - xi + yj in 2 dimensional space
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):   # for adding 2 vectors __add__() method is used -> for overloading + operator to add 2 objects of class or type 'Vector'
        return Vector(self.x+other.x, self.y+other.y)
    
    def __str__(self):          # for overloading builtin method 'print()', __str__() is used
        return f'Vector({self.x}, {self.y})'
    
# creating objects for Vector class
v1 = Vector(5, 6)   # 5i+6j in 2-dimensional space
v2 = Vector(10, 15) # 10i+15j in 2-dimensional space

sum = v1 + v2 # 5i+10i + 6j+15j -> v1 + v2 automatically calls __add__ -> which means python internally calls like this v1.__add__(v2) and another Vector object is returned

print(sum)  # while using sum python internally calls sum.__str__() -> it returns 'Vector({self.x}, {self.y})'

# Example 2 => program to show operator overloading -> for adding 2 rational numbers

# class for Rational Number -> Rational Number (p / q, q != 0) 
class Rational:
    def __init__(self, p=1, q=1):   
        self.p = p  # p - numerator
        self.q = q  # q - denominator
    
    def __add__(self, other):    # for adding 2 rational numbers __add__() method is used -> for overloading + operator to add 2 objects of class or type 'Rational'
        sum = Rational()
        
        # cross multiplication method - for adding two rational numbers
        sum.p = self.p * other.q + self.q * other.p
        sum.q = self.q * other.q
        
        return sum
    
    def __str__(self):          # for overloading builtin method 'print()', __str__() is used
        return str(self.p) + '/' + str(self.q)
    
# creating objects for Rational class
r1 = Rational(2, 3) # 2 / 3
r2 = Rational(2, 5) # 2 / 5

sum = r1 + r2   # 2/3 + 2/5

print('Sum Of 2 Rational Numbers :', sum)