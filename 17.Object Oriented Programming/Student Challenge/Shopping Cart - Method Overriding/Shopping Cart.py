# python program to implement orders class achieve method overriding

# class for orders
class Orders:
    
    def __init__(self):
        self.cart = []  # empty list
        
    def add_to_cart(self, item):
        self.cart.append(item)
    
    def remove_from_cart(self, item):
        self.cart.remove(item)
    
    # Method Overriding => len
    def __len__(self):
        return len(self.cart)

    # Method Overriding => str
    def __str__(self):
        return str(self.cart)
    
# creating object for Orders class
o = Orders()

o.add_to_cart('apple')
o.add_to_cart('banana')
o.add_to_cart('pineapple')

print('Length of cart :', len(o))

print('Shopping Cart :', o)

o.remove_from_cart('apple')

print('Shopping Cart :', o)  