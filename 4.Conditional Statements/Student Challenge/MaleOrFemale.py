# python program to check male(m/M) (or) female(f/F)

gender = input('Enter the gender : ')

if gender == 'm' or gender == 'M':
    print('Male')
elif gender == 'f' or gender == 'F':
    print('Female')
else:
        print('Invalid Gender')