# python program to implement oop's principle polymorphism - DuckTyping in python

# function to implement the action of pet
def pet(pet):
    pet.talk()
    pet.walk()
    
# class for Duck
class Duck:
    def talk(self):
        print('Duck is talking')
    
    def walk(self):
        print('Duck is walking')
        
# class for Dog
class Dog:
    def talk(self):
        print('Dog is talking')
    
    def walk(self):
        print('Dog is walking')
        
# creating objects for classes : Duck, Dog
pet1 = Duck()
pet2 = Dog()

pet(pet1)

pet(pet2)
        