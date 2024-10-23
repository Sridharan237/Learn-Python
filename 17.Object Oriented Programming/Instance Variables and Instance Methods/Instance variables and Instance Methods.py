# python program to implement Instance Variables and Instance Methods

# Example 1 => class for Rectangle
# length, breadth - instance variables of class Rectangle
# area, perimeter - instance methods of class Rectangle
class Rectangle:
    def __init__(self, length, breadth):    # Instance variables can be created inside constructor
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
r1 = Rectangle(10, 5)

r2 = Rectangle(20, 15)



# Example 2 => class for Test
# a, b, c  - instance variables of class Test
# fun - instance methods of class Test
class Test:
    def __init__(x):
        x.a = 10
    
    def fun(y):     # Instance variables can be created inside methods of a class
        y.b = 20
        
t1 = Test()

t1.c = 30   # Instance variables can be created outside of a class

print(dir(t1))

# Output : ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'a', 'c', 'fun']

t1.fun()

print(dir(t1))

# Output : ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'a', 'b', 'c', 'fun']