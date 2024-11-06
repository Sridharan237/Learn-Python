# python program to implement a class for circle

import math

# class for circle
class Circle:
    
    def __init__(self, radius):
        self.radius = radius
        
    # methods of circle class
    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

# creating object for Circle class
c = Circle(10)

print('Area : %.2f' % c.area())
print('Perimeter : %.2f' % c.perimeter())