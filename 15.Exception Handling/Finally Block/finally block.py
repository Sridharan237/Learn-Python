# python program to implement try-except-else-finally (finally block - implementation in exception handling)

# (Usage of back slash) => program to show that back slash can be used in a statement to tell the python interpreter that the statements should be included below the line also

print('before try block')

try:
    a = int(input('Enter numerator : '))    # a = 10
    b = int(input('Enter denominator : '))  # b = 5
    
    c = a // b  \
        +       b + a                       # c = 10 // 5 + 5 + 10

    print(c)                                # c = 17 
    
except:
    print('hello')
    
# program to show try must have atleast one or more except (or) only one finally or both except and finally(only one) in exception handling
def fun():
    try:
        return 1    
    
    finally:
        return 2
    
print('fun :', fun())
    
    
    
# Example 1 => program handles ZeroDivisionError Exception using try-except-else-finally

print('before try block')

try:
    a = int(input('Enter numerator : '))
    b = int(input('Enter denominator : '))
    
    c = a // b
        
    print('End of try block')
    
except ZeroDivisionError as error:
    print(error)

else:
    print('Division :', c)
    
finally:
    print('Finally block')
    


# Example 2 => program to show the use case of finally block inside function (try-except-else-finally inside a function)

def div(a, b):
    print('before try block')
    try:
        c = a // b
        
        return c
    
    except ZeroDivisionError:
        raise ZeroDivisionError
    
    finally:
        print('Finally Block')
        

a = int(input('Enter numerator : '))
b = int(input('Enter denominator : '))

result = div(a, b)

print('Division :', result)    



# Example 3 => (use case of finally in clean-up process)    => program to show use case of finally in open a file, performing operations in the file and mandatorily closing the file using finally block
def file(file_name):
    print('before try block')
    
    try:
        f = open(file_name, 'r')
        
        print(f.read())
    
    except FileNotFoundError as error:
        return {'Error Message':error}

    else:
        print('Else Block')
    
    finally:
        # f.close()
        print('File Closed Successfully')
    
print(file('hello.txt'))
    
    
    

