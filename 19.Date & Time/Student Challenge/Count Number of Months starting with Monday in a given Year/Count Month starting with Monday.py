# python program to count the no. of months starting with month in a give year

from datetime import date

year = int(input('Enter year : '))

mondays = 0   # to store the count of months starting with monday in a given year

for month in range(1, 13):
    d = date(year, month, 1)

    if d.weekday() == 0:
        mondays += 1
        print('Month :', month)

print('Count of months starting with monday :', mondays)
