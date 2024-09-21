# python program to implement indexing and slicing in list

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1)
# Output : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# INDEXING 

print(list1[6])
# Output : 7

print(list1[-4])
# Output : 7

list1[6] = 15
print(list1)
# Output : [1, 2, 3, 4, 5, 6, 15, 8, 9, 10]

x = list1[6]
print(x)
# Output : 15

x = 'john'
print(x)
# Output : 'john'

print(list1)
# Output : [1, 2, 3, 4, 5, 6, 15, 8, 9, 10]

# SLICING

print(list1[:])
# Output : [1, 2, 3, 4, 5, 6, 15, 8, 9, 10]

print(list1[3:])
# Output : [4, 5, 6, 15, 8, 9, 10]

print(list1[3:8])
# Output : [4, 5, 6, 15, 8]

print(list1[0:10:2])
# Output : [1, 3, 5, 15, 9]

print(list1[::-1])
# Output : [10, 9, 8, 15, 6, 5, 4, 3, 2, 1]

print(list1[-1:-11:-1])
# Output : [10, 9, 8, 15, 6, 5, 4, 3, 2, 1]

# Modifying objects through SLICING

list1[0:3:] = [10, 20, 30]  # Assigning Exact no. of objects
print(list1)
# Output : [10, 20, 30, 4, 5, 6, 15, 8, 9, 10]

list1[0:3] = [10, 20]       # Assigning Less no. of objects
print(list1)
# Output : [10, 20, 4, 5, 6, 15, 8, 9, 10]

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
list1[0:2:] = [10, 20, 30, 40, 50]  # Assigning More no. of objects
print(list1)
# Output : [10, 20, 30, 40, 50, 3, 4, 5, 6, 7, 8, 9, 10]

# list1[::3] = [11, 22, 33, 44]     # In Step, we need assign atmost accomodatable no. of objects

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: attempt to assign sequence of size 4 to extended slice of size 5

list1[::3] = [11, 22, 33, 44, 55]
print(list1)
# Output : [11, 20, 30, 22, 50, 3, 33, 5, 6, 44, 8, 9, 55]

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1[0:10:2] = [11, 22, 33, 44, 55]
print(list1)
# Output : [11, 2, 22, 4, 33, 6, 44, 8, 55, 10]
