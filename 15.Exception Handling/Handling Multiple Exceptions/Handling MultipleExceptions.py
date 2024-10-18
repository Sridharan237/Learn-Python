# python program to implement handling multiple exceptions using try and except - (multiple except block, single except block) -> multiple exceptions will be handled

# # Example 1 => program without using exception handling (try and except)

# L = [10, 20, 30, 40, 50]

# index = int(input('Enter an index : '))

# print(L[index])
# # Input : 5
# # Output : IndexError: list index out of range - program will not execute hereafter

# print('Terminated Gracefully')

# # Example 2 => program with using exception handling (try and except) - Handles IndexError Exception only

# L = [10, 20, 30, 40, 50]

# try:
#     index = int(input('Enter an index : '))

#     print(L[index])
    
#     print('end of try block')

# except IndexError:
#     print('Invalid index')

# print('Terminated Gracefully')

# # Example 3 => program with using exception handling (try and except) - Handles IndexError, ValueError Exceptions - using multiple except except block

# L = [10, 20, 30, 40, 50]

# try:
#     index = int(input('Enter an index : '))

#     print(L[index])
    
#     print('end of try block')

# except IndexError:
#     print('Invalid index')

# except ValueError:
#     print('Enter integer index only')

# except:
#     print('Some Errors')

# print('Terminated Gracefully')

# # Example 4 => program with using exception handling (try and except) - Handles IndexError Exception and displays the Error or Exception message description

# L = [10, 20, 30, 40, 50]

# try:
#     index = int(input('Enter an index : '))

#     print(L[index])
    
#     print('end of try block')

# except IndexError as message:
#     print('Invalid index :', message)

# print('Terminated Gracefully')

# Example 5 => program with using exception handling (try and except) - Handles IndexError, ValueError Exceptions and displays the Error or Exception message description

L = [10, 20, 30, 40, 50]

try:
    index = int(input('Enter an index : '))

    print(L[index])
    
    print('end of try block')

except (IndexError, ValueError) as message:
    print(message)

print('Terminated Gracefully')

