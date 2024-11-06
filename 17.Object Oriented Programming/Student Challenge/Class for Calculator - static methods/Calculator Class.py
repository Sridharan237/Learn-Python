# python program to implement a class for calculator

# class for calculator - with static methods
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def sub(a, b):
        return a - b
    
    @staticmethod
    def mul(a, b):
        return a * b
    
    @staticmethod
    def div(a, b):
        return a / b
    
# calling 4 static methods of above Calculator class
x = 10
y = 5

print('Addition :', Calculator.add(x, y))
print('Subtraction :', Calculator.sub(x, y))
print('Multiplication :', Calculator.mul(x, y))
print('Division :', Calculator.div(x, y))