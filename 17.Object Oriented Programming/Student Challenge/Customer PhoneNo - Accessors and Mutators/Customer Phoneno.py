# python program to implement a class for Customer 

# class for Customer
class Customer:
    
    def __init__(self, name, phno):
        self.__name = name
        self.__phno = phno
    
    # Accessors 
    def getName(self):
        return self.__name 
    
    def getPhno(self):
        return self.__phno 
    
    # Mutators
    def setPhno(self, new_phno):
        self.__phno = new_phno

# creating object for Customer class
c1 = Customer('Arun', '9838383453')

print('Name :', c1.getName())
print('Phoneno :', c1.getPhno())

c1.setPhno('8339303333')
print('New Phoneno :', c1.getPhno())

