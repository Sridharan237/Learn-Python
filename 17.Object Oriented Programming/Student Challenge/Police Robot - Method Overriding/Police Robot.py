# python program to implement method overriding 

# class for robot
class Robot:
    
    def __init__(self, name):
        self.name = name
    
    def say_hi(self):
        print(f'Hi, my name is {self.name} and I am a Robot')

# class for police robot
class PoliceRobot(Robot):
    def say_hi(self):
        print(f'Hi, my name is {self.name} and I am a PoliceRobot')
        
# creating objects for classes Robot and PoliceRobot
robo = Robot('Chitti')
robo.say_hi()

police_robo = PoliceRobot('Android')
police_robo.say_hi()