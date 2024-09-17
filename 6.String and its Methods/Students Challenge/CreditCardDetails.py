# python program to display only the last 4 digits of the credit or debit card number and remaining as '*'

cardNo = input('Enter the 16 digit card no. : ')

stars = ('*' * 4 + ' ') * 3

displayNo = stars + cardNo[15::]

print(displayNo)