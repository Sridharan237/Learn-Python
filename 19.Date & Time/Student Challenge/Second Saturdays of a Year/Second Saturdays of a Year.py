# python program to find all the second saturdays of a month of a year

import calendar

year = int(input('Enter a year : '))

for month in range(1, 13):
    month_dates_list = calendar.monthcalendar(year, month)
    
    first_week = month_dates_list[0]
    second_week = month_dates_list[1]
    third_week = month_dates_list[2]
    
    if first_week[5] != 0:
        print('{}-{}-{}'.format(second_week[5], month, year))
    else:
        print('{}-{}-{}'.format(third_week[5], month, year))