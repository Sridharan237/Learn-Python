# python program to check whether a person has administrator access(user-'john' or 'smith')

user_name = input('Enter the user name : ')

if user_name == 'john' or user_name == 'smith':
    print('Authorised')
else:
    print('Not Authorised')