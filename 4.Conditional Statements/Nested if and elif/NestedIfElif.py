# python program to find greater age out of 3 people using nested if and elif statements

john_age = int(input("Enter john's age : "))
smith_age = int(input("Enter smith's age : "))
ajay_age = int(input("Enter ajay's age : "))

print('Nested if :', end='')
# Nested if  -> nested if make the code look congested
if john_age > smith_age and john_age > ajay_age:
    print('john is elder')
else:
    if smith_age > ajay_age:
        print('smith is elder')
    else:
        print('ajay is elder')

print('elif :', end='')
# elif  -> elif is better because it makes the code not congested
if john_age > smith_age and john_age > ajay_age:
    print('john is elder')
elif smith_age > ajay_age:
    print('smith is elder')
else:
    print('ajay is elder')