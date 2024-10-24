# python program to implement oop's principle polymorphism - DuckTyping in python

# function to implement the action of driver
def driver(car):
    car.drive()
    
# class for Hyundai
class Hyundai:
    def drive(self):
        print('Hyundai is being driven by a driver')
        
# class for MarutiSuzuki
class MarutiSuzuki:
    def drive(self):
        print('MarutiSuzuki is being driven by a driver')
        
# creating objects for classes : Hyundai, MarutiSuzuki
car1 = Hyundai()
car2 = MarutiSuzuki()

driver(car1)

driver(car2)
        