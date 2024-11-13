# python program to find missing natural number from an array

import array

# function to find missing natural number from an array
def missing_num(arr):
    start, end = arr[0], arr[len(arr)-1]
    
    actual_numbers = list(range(start, end+1))
    
    actual_sum = sum(actual_numbers)
    
    given_sum = sum(arr)
    
    missing_number = actual_sum - given_sum
    
    if missing_number == 0:
        return -1   # no missing number found
    else:
        return missing_number   
    
    
    
# main part of the program (or) main block
A = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 10])

missingNumber = missing_num(A)

if missingNumber == -1:
    print('No missing number found')
else:
    print('Missing Number is', missingNumber)