# python program to implement a function to print positional messages

def printMessage(name, occupation):
    print('My name is {}, I am a {}'.format(name, occupation))
    
name, occupation = input('Enter your name : '), input('Enter your occupation : ')

printMessage(name, occupation)