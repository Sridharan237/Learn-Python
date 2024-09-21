# python program to implement list creation, creating a list with heterogeneous objects, modifying the elements in a list

MyList = ['john', 'smith', 'david', 'mark', 'eric', 'smith']

print(MyList)   # Output : ['john', 'smith', 'david', 'mark', 'eric', 'smith']
print(print(MyList))    # Output : ['john', 'smith', 'david', 'mark', 'eric', 'smith'], None ->Because, return type of print() function is None
print(MyList[0])    # Output : 'john'
print(MyList[2])    # Output : 'david'
print(MyList[4])    # Output : 'eric'
print(MyList[0])    # Output : john
list1 = [1, 2, 3, 4, 5]
print(list1)    # Output : [1, 2, 3, 4, 5]

# list2 = list(1, 2, 3, 4, 5)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: list expected at most 1 argument, got 5

# List Creation
# method-1
list2 = list(list1)
print(list2)    # Output : [1, 2, 3, 4, 5]

# method-2
list2 = list((1, 2, 3, 4, 5))
print(list2)    # Output : [1, 2, 3, 4, 5]

# Creating a list of heterogeneous objects
MyList = ['john', 15, 14.6, True, 'steven', 5+7j]
print(MyList)   # Output : ['john', 15, 14.6, True, 'steven', (5+7j)]

# Modifying objects in a list - index, append
MyList[0] = 30
print(MyList)   # Output : [30, 15, 14.6, True, 'steven', (5+7j)]
MyList[4] = 'john'
print(MyList)   # Output : [30, 15, 14.6, True, 'john', (5+7j)]

MyList.append(50)
print(MyList)   # Output : [30, 15, 14.6, True, 'john', (5+7j), 50]

print(len(MyList))  # Output : 7

MyList.append(300)
print(MyList)   # Output : [30, 15, 14.6, True, 'john', (5+7j), 50, 300]

# len() -> returns the length of a list
print(len(MyList))  # Output : 8