# python program to implement a function to find the last thursday's date

from datetime import date, timedelta

def last_day_date(day):
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    today_weekday = date.weekday(date.today())

    given_weekday = weekdays.index(day)

    difference = given_weekday - today_weekday

    if difference < 0:
        return date.today() + timedelta(difference)
    else:
        return date.today() - timedelta(7 - difference)

last_day = input('Enter day name : ')
print('Today :', date.today())
print(f'Last {last_day} date :', last_day_date(last_day))