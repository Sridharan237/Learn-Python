# python program to implement greeting in different languages using polymorphism 

# class for english language
class English:
    
    def greeting(self):
        print('Hello')

# class for french language
class French:
    
    def greeting(self):
        print('Bonjour')

# function to achieve polymorphism
def greet(language):
    language.greeting()

# creating objects for classes English, French
e = English()
greet(e)

f = French()
greet(f)