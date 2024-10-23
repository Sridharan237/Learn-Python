# python program to implement Class or Static Variables and Class Methods

# Example 1 => Class for Rectangle
class Rectangle:
    count = 0   # count - Class (or) Static Variable
    
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        # self.count += 1  # for counting number of objects created for a class and It must not be accessed using self and if accessed it should be treated as the data members of Rectangle and it will not be treated as class/static variables
        Rectangle.count += 1    # but should be accessed using class name
        
    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def area(self):
        return self.length * self.breadth
    
    @classmethod
    def getCount(self):     # getCount() => class method in Rectangle class
        return self.count
    
r1 = Rectangle(10, 5)

print('count :', r1.count)

print('count :', Rectangle.count)

r2 = Rectangle(20, 7)

print('count :', r2.count)

print(dir(Rectangle))