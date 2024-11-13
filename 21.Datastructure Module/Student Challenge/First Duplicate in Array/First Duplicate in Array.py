# python program to find the first duplicate in an array

import array

# function that returns the first duplicate in an array if found else returns -1 (no duplicate found)
def first_duplicate(arr):
    s = set()
    
    for x in arr:
        if x not in s:
            s.add(x)
        else:
            return x 
        
    return -1   # no duplicate found



# main part of the program (or) main block
A = array.array('i', [10, 20, 13, 14, 15, 13, 17, 10, 20, 13])

print(first_duplicate(A))