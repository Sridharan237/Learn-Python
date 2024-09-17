# python program to display data like in a bill

item_name = input('Enter item name : ')
item_price = input('Enter item price : ')

total_len = len(item_name) + len(item_price)

print("Total Length :",total_len)

dots = '.' * (25 - total_len)

length = len('Item Name') + len('Price')

print('Item Name' + '.'*(25-length) + 'Price')

print(item_name+dots+item_price)