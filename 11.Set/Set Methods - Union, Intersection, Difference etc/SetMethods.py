# python program to implement set methods like => union, intersection, difference, symmetric_difference

A = {1, 2, 3, 5, 7}
B = {5, 7, 9, 10, 11}
print(A)
# Output : {1, 2, 3, 5, 7}

B
{5, 7, 9, 10, 11}
print(type(A))
# Output : <class 'set'>

print(dir(set))
# Output : ['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

print(A.union(B))
# Output : {1, 2, 3, 5, 7, 9, 10, 11}

print(A)
# Output : {1, 2, 3, 5, 7}

print(B)
# Output : {5, 7, 9, 10, 11}

A.update(B)
print(A)
{1, 2, 3, 5, 7, 9, 10, 11}
print(B)
# Output : {5, 7, 9, 10, 11}

A = {1, 2, 3, 5, 7}
B = {5, 7, 9, 10, 11}
print(A.intersection(B))
# Output : {5, 7}

print(B.intersection(A))
# Output : {5, 7}

A.intersection_update(B)
print(A)
# Output : {5, 7}

print(B)
# Output : {5, 7, 9, 10, 11}

B.intersection_update(A)
print(B)
# Output : {5, 7}

A = {1, 2, 3, 5, 7}
B = {5, 7, 9, 10, 11}
print(A.difference(B))
# Output : {1, 2, 3}

print(B.difference(A))
# Output : {9, 10, 11}

A.difference_update(B)
print(A)
# Output : {1, 2, 3}

A = {1, 2, 3, 5, 7}
B.difference_update(A)
print(B)
# Output : {9, 10, 11}

A = {1, 2, 3, 5, 7}
B = {5, 7, 9, 10, 11}
print(A.symmetric_difference(B))
# Output : {1, 2, 3, 9, 10, 11}

print(B.symmetric_difference(A))
# Output : {1, 2, 3, 9, 10, 11}

A.symmetric_difference_update(B)
print(A)
# Output : {1, 2, 3, 9, 10, 11}

A = {1, 2, 3, 5, 7}
B.symmetric_difference_update(A)
print(B)
# Output : {1, 2, 3, 9, 10, 11}





# set methods like => issubset, issuperset, isdisjoint

A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 11}
B = {1, 3, 5, 7, 9}

#C = {2, 4, 6, 8, 1 1}

#   File "<stdin>", line 1
#     C = {2, 4, 6, 8, 1 1}
#                      ^^^
# SyntaxError: invalid syntax. Perhaps you forgot a comma?

C = {2, 4, 6, 8, 11}
print(B.issubset(A))
# Output : True


#c.issubset(A)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'c' is not defined. Did you mean: 'C'?

print(C.issubset(A))
# Output : True

print(A.issubset(B))
# Output : False

print(A.issubset(C))
# Output : False

print(A.issuperset(B))
# Output : True

print(A.issuperset(C))
# Output : True

print(B.issuperset(A))
# Output : False

print(C.issuperset(A))
# Output : False

print(B.isdisjoint(C))
# Output : True

print(A.isdisjoint(B))
# Output : False

print(A.isdisjoint(C))
# Output : False
