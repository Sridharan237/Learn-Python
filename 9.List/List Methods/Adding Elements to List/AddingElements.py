# python program to implement list methods (for adding elements into list) like : append, extend, insert, copy(shallow copy)

# index method - used to return the index of first occurrence of an element
l = [1, 2, 3]
print(l.index(2))
# Output : 1

# print(l.index(3939))
# Output : Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: 3939 is not in list

# append method
l = [1, 2, 3]
l.append(4)
print(l)
# Output : [1, 2, 3, 4]

# extend method
l = [1, 2, 3]
print(l)
# Output : [1, 2, 3]
l.extend([4, 5, 6])
print(l)
# Output : [1, 2, 3, 4, 5, 6]

# insert method
l = [1, 2, 3]
print(l)
# Output : [1, 2, 3]
l.insert(1, 10)
print(l)
# Output : [1, 10, 2, 3]

# copy method - shallow copy
l1 = [1, 2, 3]
print(l1)
# Output : [1, 2, 3]

# l2 = l2.copy()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'l2' is not defined. Did you mean: 'l'?

l2 = l1.copy()  # shallow copy
print(l2)
# Output : [1, 2, 3]
print(id(l1))
# Output : 2212935453824
print(id(l2))
# Output : 2212931162496
print(id(l1[0]))
# Output : 140717231446456
print(id(l2[0]))
# Output : 140717231446456
l2[0] = 10
print(l2)
# Output : [10, 2, 3]
print(l1)
# Output : [1, 2, 3]
l1[0] = 30
print(l1)
# Output : [30, 2, 3]
print(l2)
# Output : [10, 2, 3]

# reference copy
l1 = [1, 2, 3]
l2 = l1 # copying the reference of l1 and storing it in l2
print(l1)
# Output : [1, 2, 3]
print(l2)
# Output : [1, 2, 3]
print(id(l1))
# Output : 2212935460224
print(id(l2))
# Output : 2212935460224
l1[0] = 10
print(l1)
# Output : [10, 2, 3]
print(l2)
# Output : [10, 2, 3]

# deep copy - copying all the elements
l1 = [1, 2, 3]
l2 = l1[:]  # copying all the elements from l1 and creates a new list
print(l1)
# Output : [1, 2, 3]
print(l2)
# Output : [1, 2, 3]
print(id(l1))
# Output : 2212931162496
print(id(l2))
# Output : 2212935453824
l2[0] = 10
print(l2)
# Output : [10, 2, 3]
print(l1)
# Output : [1, 2, 3]









# append, extend, insert, copy - using slice operator(slicing operation)

# append - using slice operator
l = [1, 2, 3]
l[3:3] = [4]
print(l)
# Output : [1, 2, 3, 4]
l[len(l):] = [5]
print(l)
# Output : [1, 2, 3, 4, 5]
l = [1, 2, 3]
print(l)
# Output : [1, 2, 3]
l[1:1] = [3]
print(l)
# Output : [1, 3, 2, 3]

# extend - using slice operator
l = [1, 2, 3]
l[len(l):] = [4, 5, 6]
print(l)
# Output : [1, 2, 3, 4, 5, 6]

# insert - using slice operator
l = [1, 2, 3]
l[1:1] = [11, 22, 33]
print(l)
# Output : [1, 11, 22, 33, 2, 3]

# Examples - practice

l = [1, 2, 3, 4, 5]
print(l[5:])
# Output : []

print(l[5:10])
# Output : []

l[8:10] = [1, 2, 3]
print(l)
# Output : [1, 2, 3, 4, 5, 1, 2, 3]

print(l[5:5])
# Output : []

print(l[5:4])
# Output : []

l[5:3] = [22, 33, 44]
print(l)
# Output : [1, 2, 3, 4, 5, 22, 33, 44, 1, 2, 3]


# modifying values in a list using slice operator - through negative step value

l = [1, 2, 3, 4, 5, 1, 2, 3]

# l[5:3:-1] = [22, 33, 44]
# Output : Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: attempt to assign sequence of size 3 to extended slice of size 

l[5:3:-1] = [22, 33]
print(l)
# Output : [1, 2, 3, 4, 33, 22, 2, 3]

l = [1, 2, 3]
l[::-1] = [4, 5, 6]
print(l)
# Output : [6, 5, 4]

l = [1, 2, 3]
print(l)
# Output : [1, 2, 3]

# l[::-1] = [4, 5]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: attempt to assign sequence of size 2 to extended slice of size 3

l[2:0:-1] = [4, 5]
print(l)
# Output : [1, 5, 4]









# modifying the last element using slice operator
l[2:] = [10]
print(l)
# Output : [1, 2, 10]

# modifying element at index 1 using slice operator
l = [1, 2, 3]
l[1:2] = [11]
print(l)
# Output : [1, 11, 3]

# modifying more elements from index 1 using slice operator
l = [1, 2, 3]
l[1:2] = [10, 20, 30]
print(l)
# Output : [1, 10, 20, 30, 3]
