# python program to check whether a given year is leap year or not

year = int(input('Enter the year : '))

# Two Methods
# 1.using nested if
# 2.using elif

print('Method1 :', end='')
# 1.using nested if
if year % 100 == 0:
    if year % 400 == 0:
        print('Leap Year')
    else:
        print('Not Leap Year')
elif year % 4 == 0:
    print('Leap Year')
else:
    print('Not Leap Year')

print('Method2 :', end='')
# 2.using elif
if year % 400 == 0 and year % 100 == 0:
    print('Leap Year')
elif year % 4 == 0 and year % 100 != 0:
    print('Leap Year')
else:
    print('Not Leap Year')