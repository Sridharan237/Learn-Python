# python program to find the displacement of an object

u = int(input('Enter the initial velocity of an object : '))    # u - initial velocity
v = int(input('Enter the final velocity of an object : '))      # v - final velocity
a = int(input('Enter the acceleration of the object : '))       # a - acceleration

displacement = (v**2 - u**2)/(2*a)

print('Displacement is ', displacement)
