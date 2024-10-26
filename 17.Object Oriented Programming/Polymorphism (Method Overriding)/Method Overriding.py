# python program to implement polymorphism achieved through method overriding 

# Example 1 => program to show that in method overriding we cannot access parent class(iPhone6) method overrided method from child class(iPhoneX) object directly

# class for iphone 6
class iPhone6:
    def home(self):
        print('home button is pressed')     # iphone6 model -> home button is physical

# class for iphone 10
class iPhoneX(iPhone6):
    def home(self):
        print('home is touched')            # iphone10 model -> home button is touch based
        
i6 = iPhone6()
i6.home()
# Output : home button is pressed

ix = iPhoneX()
ix.home()
# Output : home is touched

'''ix.super().home()
Output : 
Traceback (most recent call last):
  File "d:\Learn-Github-Repositories\Learn Python Programming - Beginner to Master\17.Object Oriented Programming\Polymorphism (Method Overriding)\Method Overriding.py", line 23, in <module>
    ix.super().home()
    ^^^^^^^^
AttributeError: 'iPhoneX' object has no attribute 'super' ''' 

# Example 2 => program to show that in method overriding we can access parent class(iPhone6) method overrided method within child class(iPhoneX) but we cannot access it using child class(iPhoneX) object

# class for iphone 6
class iPhone6_1:
    def home(self):
        print('home button is pressed')     # iphone6 model -> home button is physical

# class for iphone 10
class iPhoneX_1(iPhone6_1):
    def home(self):
        print('home is touched')            # iphone10 model -> home button is touch based
        super().home()
        
i6 = iPhone6_1()
i6.home()
# Output : home button is pressed

ix = iPhoneX_1()
ix.home()
'''Output : 
home is touched
home button is pressed'''
