# python program to implement static method in python

# Example 1 => Class for Rectangle
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def area(self):
        return self.length * self.breadth
    
    @staticmethod
    def issquare(length, breadth):  # issquare() => issquare is a static method
        return length == breadth
    
r = Rectangle(10, 5)

"""
print('Is Square :', r.issquare(15, 10))    # static methods cannot be accessed using object name if @staticmethod decorator is not used before method inside class
Output :
Traceback (most recent call last):
  File "d:\Learn-Github-Repositories\Learn Python Programming - Beginner to Master\17.Object Oriented Programming\Static Methods\Static Methods.py", line 20, in <module>
    print('Is Square :', r.issquare(15, 10))
                         ^^^^^^^^^^^^^^^^^^
TypeError: Rectangle.issquare() takes 2 positional arguments but 3 were given
"""

print('Is Square :', r.issquare(10, 10))    # static methods can be accessed using object name if @staticmethod decorator is used before method inside class
# Output : Is Square : True

print('Is Square :', Rectangle.issquare(15, 10))    # static methods can be accessed using class name also
# Output : Is Square : False