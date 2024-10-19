# python program to implement nested try-except

# Normal program => skeleton program for the below kind of programs(Examples)

a = int(input('Enter numerator : '))
b = int(input('Enter denominator : '))

c = a // b

print('Division :', c)

# Example 1 => program to implement nested try-except (it is not a better way to use nested try-except instead use try with multiple except blocks)
try:
    a = int(input('Enter numerator : '))
    
    try:
        b = int(input('Enter denominator : '))
        
        try:
            c = a // b
            
            print('Division :', c)
        
        except ZeroDivisionError as e:
            print('Error Message :', e)
    
    except Exception as e:
        print('Error Message :', e)
        
except Exception as e:
    print('Error Message :', e)
    
# Example 2 => program to implement try with multiple except blocks (it is not a better way to use nested try-except instead use try with multiple except blocks)

try:
    a = int(input('Enter numerator : '))

    b = int(input('Enter denominator : '))

    c = a // b

    print('Division :', c)

except ZeroDivisionError as e:
    print('Error Message :', e)

except Exception as e:
    print('Error Message :', e)