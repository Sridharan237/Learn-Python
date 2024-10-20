# python program to implemen Account Balance Exception

balance = 10000
min_account_balance = 1000

# class for Account Balance Exception
class AccountBalanceException(Exception):
    pass

# function to implement withdraw (or) deduct from the bank account balance
def withdraw(amount):
    global balance
    
    if balance - amount <= min_account_balance:
        raise AccountBalanceException('Minimum Balance Should be '+str(min_account_balance))
    else:
        balance -= amount
        print('Remaining Balance :', balance)
   
# main function (or) main part of the program 
try:     
    amount = int(input('Enter the amount to be withdrawn : '))

    withdraw(amount)

except AccountBalanceException as error:
    print('Error Message :', error)

