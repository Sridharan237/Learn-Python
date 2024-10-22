# python program to implement a class for Cuboid(shape) in python

# class for cuboid
class Cuboid:
    def __init__(self, length, breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height
        
    def lidarea(self):
        return self.length * self.breadth
    
    def totalarea(self):
        return 2 * (self.length * self.breadth + self.breadth * self.height + self.height * self.length)
    
    def volume(self):
        return self.length * self.breadth * self.height

# Creating an Object for Cuboid Class
c1 = Cuboid(10, 5, 3)

print(type(c1))     
# Output : <class '__main__.Cuboid'>
print(c1.lidarea())
# Output : 50
print(c1.totalarea())
# Output : 190
print(c1.volume())
# Output : 150