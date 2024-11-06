# python program to implement a polygon class and triangle class

import math

# class for polygon
class Polygon:
    
    def __init__(self, no_of_sides, sides):
        self.no_of_sides = no_of_sides
        self.sides = sides
    
# class for triangle which inherits from polygon
class Triangle(Polygon):
    
    def __init__(self, no_of_sides, sides):
        # super().__init__(no_of_sides, sides)
        # Polygon.__init__(self, no_of_sides, sides) => this is also possible
    
    def area(self):
        # unpacking from list 'sides'
        a, b, c = self.sides
        
        s = (a + b + c) / 2
        
        area = math.sqrt(s * (s-a) * (s-b) * (s-c))

        return area

# creating object for Triangle class
t = Triangle(3, [40, 50, 30])

print('Area :', t.area())