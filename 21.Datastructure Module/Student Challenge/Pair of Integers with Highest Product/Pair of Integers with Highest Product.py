# python program to write a function to find a pair of integers with highest product from an array

import array

# function to find a pair of integers with highest product from an array
def max_product(arr):
    x, y = arr[0], arr[1]
    
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] *arr[j] > x * y:
                x, y = arr[i], arr[j]
    
    return x, y

# main part of the program (or) main block
A = array.array('i', [0, -1, -3, -5, -8, 2, 4])

print('Maximum Product Pair :', max_product(A))