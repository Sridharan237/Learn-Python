# python program to implement the conversion of string object to date object

from datetime import date

str_date = input('Enter date(in format : \'DD-MM-YY\') : ')

day, month, year = str_date.split('-')  # list unpacking

# creating date object
date = date(day=int(day), month=int(month), year=int(year))

print('Date object :', date)