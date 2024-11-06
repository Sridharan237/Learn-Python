# python program to implement angle class using operator overloading

# class for angle
class Angle:
    
    def __init__(self, degree):
        self.degree = degree
        
    # operator overloading
    def __add__(self, other_angle):
        return Angle(self.degree + other_angle.degree)
    
    # overriding 'str' method
    def __str__(self):
        return f'{self.degree}\N{DEGREE SIGN}'

# creating objects for Angle class
a1 = Angle(25)
a2 = Angle(55)

print('Angle 1 :', a1)
print('Angle 2 :', a2)
print('Addition :', a1 + a2)