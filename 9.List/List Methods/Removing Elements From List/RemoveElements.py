# python program to implement list methods to remove elements from a list like : (pop, remove, clear, del->built-in keyword)

# pop method
L = [1, 2, 3, 4, 5]
print(L)
# Output : [1, 2, 3, 4, 5]
print(L.pop())
# Output : 5
print(L)
# Output : [1, 2, 3, 4]
print(L.pop(1))
# Output : 2
print(L)
# Output : [1, 3, 4]
print(L.pop(1))
# Output : 3
print(L)
# Output : [1, 4]

# pop using slice operator (slicing operation)
# pop() - By default will delete the last element and returns it
L = [1, 2, 3, 4, 5]
print(L)
# Output : [1, 2, 3, 4, 5]
L[len(L)-1:] = []
print(L)
# Output : [1, 2, 3, 4]
x = L[1:1] = []
print(x)
# Output : []
print(L)
# Output : [1, 2, 3, 4]
L[1:2] = []
print(L)
# Output : [1, 3, 4]
print(L[len(L)-1:len(L)-1])
# Output : []
L[len(L)-1:len(L)] = []
print(L)
# Output : [1, 3]

# del - built-in keyword -> to free up memory - (actually deletes the references of objects specified - especially int, float, list, dictionary)
del L[1]
print(L)
# Output : [1]
del L
# print(L)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'L' is not defined

# remove method
L = [1, 2, 3, 4, 5]
L.remove(3)
print(L)
# Output : [1, 2, 4, 5]
L = [5, 6, 7, 6, 9]
L.remove(6)
print(L)
# Output : [5, 7, 6, 9]

# L.remove(100)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: list.remove(x): x not in list

# clear method
L.clear()
print(L)
# Output : []

# clear method - using del->built-in keyword and slice operator(slicing operator)
del L[:]
print(L)
# Output : []

# clear method - using slice operator(slicing operator)
L = [1, 2, 3, 4, 5]
L[:] = []
print(L)
# Output : []
L[:] = []
print(L)
# Output : []