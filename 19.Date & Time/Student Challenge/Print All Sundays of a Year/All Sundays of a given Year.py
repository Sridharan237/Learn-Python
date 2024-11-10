# python program to implement a function to print dates of all sundays of a year

from datetime import date, timedelta

# function to print dates of all sundays of a year
def all_sundays(year):
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    dt1 = date(year, 1, 1)
    
    first_day = dt1.weekday()
    
    difference = 6 - first_day
    
    first_sunday_date = dt1 + timedelta(difference)
    
    print('All Sundays Dates of Year', year)
    
    while first_sunday_date.year == year:
        print(first_sunday_date)
        
        first_sunday_date = first_sunday_date + timedelta(7)
        

year = int(input('Enter a year : '))

all_sundays(year)