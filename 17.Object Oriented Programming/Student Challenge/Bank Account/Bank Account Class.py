# python program to implement a class for Bank Account

# class for minimum balance exception
class MinimumBalanceError(Exception):
    pass

# class for bank account
class Account:
    AccNumber = 0
    
    def __init__(self, name, balance):
        self.name = name
        
        if balance <= 1000:
            raise MinimumBalanceError('Minimum balance must be 1000')
        else:
            self.balance = balance
        
        Account.AccNumber += 1
        self.acc_number = str(1000 + Account.AccNumber)
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance - amount <= 1000:
            raise MinimumBalanceError('Minimum balance must be 1000')
        else:
            self.balance -= amount
    
    def show_details(self):
        print('-'*3+' Account Details '+'-'*3)
        print('Account Number :', self.acc_number)
        print('Account Holder Name :', self.name)
        print('Account Balance :', self.balance)

# creating object for Account class
a1 = Account('Fahrisa', 2000)

a1.show_details()

a1.deposit(1000)

a1.show_details()

a1.withdraw(1500)

a1.show_details()