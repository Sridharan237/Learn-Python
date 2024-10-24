# python program to implement Inner/Nested Class in python

# class for Customer
class Customer:
    def __init__(self, id, name, bdoorno, bstreet, bcity, bcountry, bpincode, sdoorno, sstreet, scity, scountry, spincode):
        '''Billing Address -> bdoorno, bstreet, bcity, bcountry, bpincode
        Shipping Address -> sdoorno, sstreet, scity, scountry, spincode'''
        
        self.customer_id = id
        self.customer_name = name
        
        # self.billing_address = Address(bdoorno, bstreet, bcity, bcountry, bpincode)   # Output : UnboundLocalError: cannot access local variable 'Address' where it is not associated with a value
        # self.shipping_address = Address(sdoorno, sstreet, scity, scountry, spincode)  # Output : UnboundLocalError: cannot access local variable 'Address' where it is not associated with a value
        
        self.billing_address = self.Address(bdoorno, bstreet, bcity, bcountry, bpincode)   
        self.shipping_address = self.Address(sdoorno, sstreet, scity, scountry, spincode)
        
    # class for Address -> Address is Inner/Nested Class of Outer Class Customer
    class Address:
        def __init__(self, doorno, street, city, country, pincode):
            self.doorno = doorno
            self.street = street
            self.city = city
            self.country = country
            self.pincode = pincode
            
        def display(self):
            print('Doorno : {} \nStreet : {} \nCity : {} \nCountry : {} \nPincode : {}'.format(self.doorno, self.street, self.city, self.country, self.pincode))
                
# creating an object for customer class
c = Customer(101, 'Akash', 200, 'billing street', 'billing city', 'india', 241321, 400, 'shipping street', 'shipping city', 'shipping country', 333444)

print('-'*3, 'Billing Address', '-'*3)
c.billing_address.display()

'''Output : 
--- Billing Address ---
Doorno : 200 
Street : billing street
City : billing city
Country : india
Pincode : 241321'''

print('-'*3, 'Shipping Address', '-'*3)
c.shipping_address.display()

'''Output : 
--- Shipping Address ---
Doorno : 400
Street : shipping street
City : shipping city
Country : shipping country
Pincode : 333444'''
