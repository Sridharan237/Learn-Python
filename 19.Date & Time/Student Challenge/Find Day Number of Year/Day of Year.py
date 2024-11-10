# python program to find the no. of days of a given year
from datetime import date, timedelta

date1 = input('Enter date (in format : \'DD-MM-YY\') : ')

day, month, year = date1.split('-')

date1 = date(int(year), int(month), int(day))

# starting date of the year - (1st January)
first_date = date(int(year), 1, 1)

days = date1 - first_date

print('Day Number :', days.days)