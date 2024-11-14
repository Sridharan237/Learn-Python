# python program to implement heap sort using heapq datastructure

import heapq

# function that performs heap sort and returns a sorted list
def heap_sort(elements):
    heapq.heapify(elements) # heapify will arrange values in 'elements' in heap datastructure form (min heap)
    
    sorted_list = [] # to store the popping out elements from heap 'elements'
    
    for i in range(len(elements)):
        x = heapq.heappop(elements)
        sorted_list.append(x)
    
    return sorted_list

# main part of the program (or) main block
elements = [11, 22, 3, 14, 25, 16, 17, 28, 10]

sorted_list = heap_sort(elements)

print('list after performing heap sort :', sorted_list)
