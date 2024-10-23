# python program to implement the oop's principle inheritance in python

# class for Rectangle
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
    def area(self):
        return self.length * self.breadth
    
# class for Cuboid - child class inheriting from parent class(Rectangle)
class Cuboid(Rectangle):
    def __init__(self, length, breadth, height):
        self.height = height
        super().__init__(length, breadth)   # (or) self.length, self.breadth = length, breadth  -> this is also correct
        
    def total_area(self):
        return 2 * (self.length * self.breadth + self.breadth * self.height + self.length * self.height)
    
    def volume(self):
        return self.length * self.breadth * self.height
    
r = Rectangle(10, 5)

print('Perimeter :', r.perimeter())
print('Area :', r.area())

c = Cuboid(10, 5, 3)

print('Total Area :', c.total_area())
print('Volume :', c.volume())