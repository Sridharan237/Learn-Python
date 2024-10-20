# python program to implement match case for printing days of a week using day number

day = int(input('Enter day number : '))

# method-1 -> using elif statements

# if day == 1:
#     print('Sunday')
# elif day == 2:
#     print('Monday')
# elif day == 3:
#     print('Tuesday')
# elif day == 4:
#     print('Wednesday')
# elif day == 5:
#     print('Thursday')
# elif day == 6:
#     print('Friday')
# elif day == 7:
#     print('Saturday')
# else:
#     print('Invalid day number!')

# method-2 -> using match case

match day:
    case 1:
        print('Sunday')
    case 2:
        print('Monday')
    case 3:
        print('Tuesday')
    case 4:
        print('Wednesday')
    case 5:
        print('Thursday')
    case 6:
        print('Friday')
    case 7:
        print('Saturday')
    case _:     # default case
        print('Invalid day number!')
