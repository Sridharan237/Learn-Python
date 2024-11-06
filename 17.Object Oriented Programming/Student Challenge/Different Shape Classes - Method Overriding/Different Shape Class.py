# python program to implement different shape classes to achieve method overriding

import math

# class for shape
class Shape:
    
    def __init__(self, name):
        self.name = name
    
    def area():
        pass

# class for rectangle (inherited from shape)
class Rectangle(Shape):
    def __init__(self, name, length, breadth):
        super().__init__(name)
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth

# class for circle (inherited from shape)
class Circle(Shape):
    
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius * self.radius

# creating objects for classes (Shape, Rectangle, Circle)

s = Shape('Unknown')
print('Shape :', s.name)

r = Rectangle('Rectangle', 10, 5)
print('Area of rectangle :', r.area())

c = Circle('Circle', 6)
print('Area of circle :', c.area())