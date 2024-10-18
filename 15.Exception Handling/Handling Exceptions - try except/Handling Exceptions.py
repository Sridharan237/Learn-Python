# python program to implement handling exceptions using try and except

# Example 1 => program without using exception handling (try and except)

L = [10, 20, 30, 40, 50]

index = int(input('Enter an index : '))

print(L[index])
# Input : 5
# Output : IndexError: list index out of range - program will not execute hereafter

print('Terminated Gracefully')



# Example 2 => program with using exception handling (try and except)

L = [10, 20, 30, 40, 50]

try:
    index = int(input('Enter an index : '))

    print(L[index])
    
    print('Program end successfully')

except:
    print('Terminated Gracefully')

