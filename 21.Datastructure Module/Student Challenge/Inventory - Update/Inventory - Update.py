# python program to implement the function update_inventory 

from collections import Counter

# function to update the inventory by deducting quantities from inventory by using the order
def update_inventory(order):
    inventory.subtract(order)

# creating a Counter object for inventory
inventory = Counter(apple=50, mango=100, banana=120, orange=70)

# creating a Counter object for order
order = Counter(apple=10, banana=12, orange=5)

update_inventory(order)

print(inventory)