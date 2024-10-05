# python program to find the birthday of a person

birthdays = {
    'Sachin':'03/14/2003',
    'Carl':'01/17/2001',
    'Donald':'06/14/2010',
    'Rohan':'01/06/2005'
}

name = input('Enter person\'s name : ')

if name in birthdays:
    print('Mr./Miss. {} was born on {}'.format(name, birthdays[name]))
else:
    print('Name Not Found')