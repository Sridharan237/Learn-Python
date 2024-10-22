# python program to implement cuboid class in python and exploring about self - keyword

# self - reference to the current object

# class for cuboid
class Cuboid:
    def __init__(self, length, breadth, height):
        print('id of self :', id(self))
        self.length = length
        self.breadth = breadth
        self.height = height
        
    # # last written constructor will be used (which means constructor cannot be overloading is not possible) instead we can use default arguments
    # def __init__(self, length, breadth):
    #     print('id of self :', id(self))
    #     self.length = length
    #     self.breadth = breadth
    
    # constructor will default arguments    
    # This one will be called everytime an object is created because it is the last written constructor in the class
    def __init__(self, length=1, breadth=1, height=1):
        print('id of self :', id(self))
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
print('id of c1 :', id(c1))

c2 = Cuboid(20, 15, 5)
print('id of c1 :', id(c2))

c3 = Cuboid(20, 15)
print('id of c3 :', id(c3))

# Constructor overloading is not possible instead we can use default arguments
c4 = Cuboid()
c5 = Cuboid(10)
c6 = Cuboid(10, 5)
c7 = Cuboid(10, 5, 3)