# python program to implement a function which returns a flattened list (single dimensional list) from a nested list (multidimensional list)

# function which returns a flattened list (single dimensional list) from a nested list (multidimensional list)
def flattenNestedList(L):
    for e in L:
        if hasattr(e, '__iter__'):      # Every sequence (or) collection contains '__iter__' as an attribute and if they do not contain then they are not sequence (or) collection
            yield from flattenNestedList(e)
        else:
            yield e
  
input_list = [1, 2, [3, 4, [5, 6], 7],8]
    
print(list(flattenNestedList(input_list)))