# python program to implement Barbershop queue - functions (walk_in, serviced)

from collections import deque

# function to append into the deque shop
def walk_in(customer):
    customers.append(customer)
    print(customer, 'comes into shop')

# function to popleft from the deque shop
def serviced(): 
    customer = customers.popleft()
    print(customer, 'leaves the shop')
    
    
    
# main part of the program 

# creating object for deque - customers coming into barber shop are appended into customers deque
customers = deque()

# customers comes into the shop
walk_in('John')
walk_in('David')

# customer leaves the shop
serviced()
serviced()

# new customer comes into the shop
walk_in('Ajay')
walk_in('Akash')