# python program to implement a function to generate bill with subtotals

from collections import Counter

# function to generate bill with subtotals
def generate_bill(cart):
    total = 0
    
    print('{:12} {:11} {:7} {}'.format('Product', 'Price', 'Qty', 'Subtotal'))
    
    for product, quantity in cart.items():
        product_price = quantity * prices[product]  # subtotal -> means s of single product from cart
        total += product_price
        print('{:10} : {:5}   X   {:2}   =   {}'.format(product, prices[product], quantity, product_price))
    
    print('{:22}{:7} = {:8}'.format('', 'Total', total))

# creating price of products as a dictionary
prices = {'Soap':50, 'Toothpaste':25, 'Shampoo':45.50, 'Toothbrush':15.99}

cart = Counter(Soap=5, Toothpaste=1, Shampoo=2, Toothbrush=3)   # cart with product name and quantity

generate_bill(cart)