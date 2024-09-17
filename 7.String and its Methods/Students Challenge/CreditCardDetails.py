# python program to display only the last 4 digits of the credit or debit card number and remaining as '*'

cardNo = input('Enter the 16 digit card no. : ')

print(('*' * 4 + ' ') * 3 + cardNo[15::])