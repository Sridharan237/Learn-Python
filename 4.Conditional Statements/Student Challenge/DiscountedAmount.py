# python program to calculate the discounted amount

amount = float(input('Enter the amount : '))

if amount <= 1000:
    discount = 10/100 * amount
elif amount > 1000 and amount <= 5000:
    discount = 20/100 * amount
elif amount > 5000 and amount <= 10000:
    discount = 30/100 * amount
else:
    discount = 50/100 * amount

payable_amount = amount - discount

print('Payable Amount :', payable_amount)