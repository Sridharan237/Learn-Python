# python program to implement a function to sort a list using insertion sort using bisect class

import bisect

# function to sort a list using insertion sort using bisect class
def insertion_sort(elements):
    sorted_list = []
    
    for x in elements:
        bisect.insort(sorted_list, x)

    return sorted_list
    
# main part of the program (or) main block
elements = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]

sorted_list = insertion_sort(elements)

print('list after insertion sort :', sorted_list)