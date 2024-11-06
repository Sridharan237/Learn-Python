# python program to implement Dice class with property (side) and method (roll_dice())

from random import *

# class for dice
class Dice:
    
    def __init__(self, n):
        self.sides = n
    
    def roll_dice(self):
        return randint(1, self.sides)


# creating object for Dice class
d = Dice(12)

print('Dice :', d.roll_dice())
print('Dice :', d.roll_dice())
print('Dice :', d.roll_dice())