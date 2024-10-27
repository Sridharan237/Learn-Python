# python program to implement abstract classes and interfaces in python

from abc import ABC, abstractmethod



# Example 1 => program to implement an abstract class

# Parent class -> abstract class (which contains abstract methods and concrete methods)
class Parent(ABC):
    @abstractmethod
    def show(self):     # show()    -> abstract method
        pass

    def display(self):  # display() -> concrete method
        print('display() -> Parent class -> abstract class')
    
# Child class -> Concrete Class which inherits and overrides all the abstract methods in abstract class(Parent)
class Child(Parent):    # Concrete class
    def show(self):
        print('show() -> Child class -> Concrete class')
   
'''     
p = Parent()

p.display()

Traceback (most recent call last):
  File "d:\Learn-Github-Repositories\Learn Python Programming - Beginner to Master\17.Object Oriented Programming\Abstract Classes and Interfaces\Abstract Classes and Interfaces.py", line 21, in <module>
    p = Parent()
        ^^^^^^^^
TypeError: Can't instantiate abstract class Parent without an implementation for abstract method 'show' '''

c = Child()

c.show()
# Output : show() -> child class
c.display()
# Output : display() -> Parent class -> abstract class



# Example 2 => program to implement an interface

# Parent Class -> interface (which only contains abstract methods)
class Interface(ABC):
    @abstractmethod
    def show(self):    # show() -> abstract method  
        pass
    
# Child class -> Concrete Class which inherits and overrides all the abstract methods in interface(Parent)
class Child_1(Interface):    # Child_1 -> Concrete class
    def show(self):
        print('show() -> Child_1 class -> Concrete class')
     
# creating objects for the above classes
'''
p_1 = Parent_1()

p_1.show()

# Output : 
Traceback (most recent call last):
  File "d:\Learn-Github-Repositories\Learn Python Programming - Beginner to Master\17.Object Oriented Programming\Abstract Classes and Interfaces\Abstract Classes and Interfaces.py", line 56, in <module>
    p_1 = Parent_1()
          ^^^^^^^^^^
TypeError: Can't instantiate abstract class Parent_1 without an implementation for abstract method 'show' '''

c_1 = Child_1()

c_1.show()
# Output : show() -> Child_1 class