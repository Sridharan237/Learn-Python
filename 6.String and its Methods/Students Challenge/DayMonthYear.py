# python program to display day, month, year from a given string date(date format : dd/mm/yyyy)

date = input('Enter date(in format : dd/mm/yyyy) : ')

l = date.split('/')

print('Day :', l[0])
print('Month :', l[1])
print('Year :', l[2])