# python program to implement Negative Age Exception

# program :
# Input : age(integer) as input
# Output :
# NegativeAgeException - if age is less than 0 (should raise custom exception NegativeAgeException)
# kid - age greater than 0 and less than 13
# teen - age greater than 13 and less than 19
# young - age greater than 19 and less than 50
# old - age greater than 50

# Custom Exception should be raised when age is negative
class NegativeAgeException(Exception):
    # def __init__(self, msg):
    #     self.msg = msg
        
    # def __str__(self):
    #     return self.msg
    pass
    
# function that prints category of a person with respect to age
def stage(age):
    if age < 0:
        raise NegativeAgeException('Age cannot be negative')
    
    elif age > 0 and age < 13:
        print('kid')
    elif age >= 13 and age < 20:
        print('teen')
    elif age >=20 and age < 51:
        print('young')
    elif age >= 51:
        print('old')


# main function - main part of the part
try:
    age = int(input('Enter the age : '))

    print('Person Age Category :', end=' ')
    
    stage(age)

except NegativeAgeException as error:
    print('Error Message :', error)