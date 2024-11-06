# python program to implement a class for currency conversion

# class for currency conversion
class CurrencyConverter:

    def __init__(self, currency, rate):
        self.currency = currency
        self.rate = rate

    # Accessors
    def getCurrency(self):
        return self.currency

    def getRate(self):
        return self.rate

    # Mutators
    def setCurrency(self, new_currency):
        self.currency = new_currency

    def setRate(self, new_rate):
        self.rate = new_rate

    def convert(self, amount):  # function which converts the amount from given currency to local currency
        return amount * self.rate

# creating object for CurrencyConverter class
cc = CurrencyConverter('USD', 84)

print('Currency :', cc.getCurrency())
print('Rate :', cc.getRate())

print('1000 USD conversion is {} INR'.format(cc.convert(1000)))

cc.setCurrency('YEN')   # YEN - japanese currency
cc.setRate(0.5)

print('Currency :', cc.getCurrency())
print('Rate :', cc.getRate())

print('1000 YEN conversion is {} INR'.format(cc.convert(1000)))