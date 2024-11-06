# python program to implement cat and dog classes to achieve polymorphism

# class for cat
class Cat:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f'My name is {self.name} and age is {self.age}')
    
    def make_sound(self):
        print('Sound : Meow Meow')
    
# class for dog
class Dog:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f'My name is {self.name} and age is {self.age}')
    
    def make_sound(self):
        print('Sound : Bow Bow')

# function to achieve polymorphism
def my_pet(pet):
    pet.info()
    pet.make_sound()
    
# creating object for classes Cat, Dog
c = Cat('Kitty', 2)
my_pet(c)

d = Dog('Jimmy', 8)
my_pet(d)