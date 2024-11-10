# python program to implement a function to calculate age from date of birth(dob)

from datetime import date

# function to calculate age from date of birth(dob)
def age(dob):
    today = date.today()

    years = today.year - dob.year

    if (today.month, today.day) < (dob.month, dob.day):
        years -= 1

    return years

dob = input('Enter Date Of Birth (in format : \'DD-MM-YY\') : ')

day, month, year = dob.split('-')  # list unpacking

# creating date object
dob = date(day=int(day), month=int(month), year=int(year))

age = age(dob)

print('Age :', age)