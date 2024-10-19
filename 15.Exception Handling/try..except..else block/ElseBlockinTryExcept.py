# python program to implement try except else blocks in exception handling

print(ZeroDivisionError)    
# Output : <class 'ZeroDivisionError'>



# Example 1 => program handles ZeroDivisionError using try-except-else blocks

print('before try block')

try:
    a = int(input('Enter numerator : '))
    b = int(input('Enter denominator : '))

    c = a // b
    
    print('try block completely executed')  # this statement will not cause any exception so should be in else block
    
except ZeroDivisionError as message:
    print('Error Message :', message)

else:
    print('Division :', c)

print('Outside try-except-else')



# Example 2 => program handles ZeroDivisionError using try-except-else blocks 

print('before try block')

try:    # only should write statements which may cause exception in try block and others should be in else block
    a = int(input('Enter numerator : '))
    b = int(input('Enter denominator : '))

    c = a // b
    
except ZeroDivisionError as message:
    print('Error Message :', message)

else:
    print('try block completely executed')
    print('Division :', c)

print('Outside try-except-else')