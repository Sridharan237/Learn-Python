# python program to implement accessors (getters) and mutators (setters)

# Example1 => class for Rectangle
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
    def getLength(self):
        return self.length
    
    def setLength(self, l):
        self.length = l
    
    def getBreadth(self):
        return self.breadth
    
    def setBreadth(self, b):
        self.breadth = b
        
r = Rectangle(10, 5)

print('length :', r.getLength())    # Output : 10
print('breadth :', r.getBreadth())  # Output : 5

r.setLength(25)
r.setBreadth(15)

print('length :', r.getLength())    # Output : 25
print('breadth :', r.getBreadth())  # Output : 15