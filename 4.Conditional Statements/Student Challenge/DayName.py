# python program to take a day number and display day name

day = int(input('Enter day number(between 1-7) : '))

if day == 1:
    print('Sunday')
elif day == 2:
    print('Monday')
elif day == 3:
    print('Tuesday')
elif day == 4:
    print('Wednesday')
elif day == 5:
    print('Thursday')
elif day == 6:
    print('Friday')
elif day == 7:
    print('Saturday')
else:
    print('Invalid day number!')