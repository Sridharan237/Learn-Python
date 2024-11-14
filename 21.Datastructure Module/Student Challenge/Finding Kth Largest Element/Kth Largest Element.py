# python program to implement a function to find the kth largest element in a list using heap datastructure

import heapq

# function to find the kth largest element in a list using heap datastructure
def kthLargest(elements, k):
    heap = []   # heap - empty list
    
    for e in elements:
        heapq.heappush(heap, -e)    # pushing into heap by reversing the sign so that we can get largest element from heap while popping    
    
    for i in range(k):
        x = heapq.heappop(heap)
    
    return -x   # multiplying x by -1 to reverse the sign to positive

# main part of the program (or) main block
l = [10, 29, 64, 90, 82, 74, 33]

print('Kth Largest Element :', kthLargest(l, 2))