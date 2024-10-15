# python program to implement a function which returns planet name when we pass planet id

# function which returns planet name when we pass planet id
def planet_name(planet_id) -> str:
    planets = {1:'Mercury', 2:'Venus', 3:'Earth', 4:'Mars', 5:'Jupiter', 6:'Saturn', 7:'Uranus', 8:'Neptune', 9:'Pluto'}
    
    return planets[id]

id = int(input('Enter a planet id (between 1 and 9 - self included) : '))

print('Planet Name :', planet_name(id))