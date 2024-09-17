# python program to check whether password and confirmation password are correct or not

password1 = input('Enter password : ')
password2 = input('Enter confirmation password : ')     # confirmation password

if password1 == password2:
    print('Yes, They are matching')
elif password1.lower() == password2.lower():
    print('No, They are not matching and please check the cases properly! Try again')
else:
    print('No, They are not matching! Try again')

