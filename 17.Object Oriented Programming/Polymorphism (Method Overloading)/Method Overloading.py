# python program to implement polymorphism achieved through method overloading

# Example 1 => program in which sum() method works for any datatype (python supports operator overloading internally)
class Arith:
    def sum(self, a, b):
        return a + b
    
a = Arith()

print(a.sum(10, 5)) 
# Output : 15
print(a.sum(8.5, 7.6))
# Output : 16.1
print(a.sum('hello', 'world'))
# Output : helloworld

# Example 2 => program to show that multiple methods with same name can be written error will not be thrown but last written method will be taken and other methods are shadowed or hidden
class Arith:
    def sum(self, a, b):    # sum() with 2 positional arguments is shadowed or hidden
        return a + b
    
    def sum(self, x, y, z):
        return x + y + z
    
a = Arith()

print(a.sum(10, 5, 3))
# Output : 18

'''print(a.sum(10, 5)) 
Output : 
Traceback (most recent call last):
  File "d:\Learn-Github-Repositories\Learn Python Programming - Beginner to Master\17.Object Oriented Programming\Polymorphism (Method Overloading)\Method Overloading.py", line 29, in <module>
    print(a.sum(10, 5)) 
          ^^^^^^^^^^^^
TypeError: Arith.sum() missing 1 required positional argument: 'z'''

# Example 3 => program to show that sum() - one method - with 2 parameters will work(act) for any number of arguments (2 or 3 arguments only) passed
class Arith:
    def sum(self, a, b, c=None):
        s = a + b
        
        if c == None:
            return s
        else:
            return s + c
    
a = Arith()

print(a.sum(10, 5, 3))
# Output : 18
print(a.sum(10, 5))
# Output : 15