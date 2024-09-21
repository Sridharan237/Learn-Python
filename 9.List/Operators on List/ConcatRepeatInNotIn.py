# python program to implement list operators like -> +, *, in, not in => on list

# Concatenation (+)
list1 = [1, 2, 3]
list2 = [8, 9, 10]
print(list1+list2)
# Output : [1, 2, 3, 8, 9, 10]

print(list1)
# Output : [1, 2, 3]

print(list2)
# Output : [8, 9, 10]

list3 = list1 + list2
print(list3)
# Output : [1, 2, 3, 8, 9, 10]

print(list1)
# Output : [1, 2, 3]

print(list2)
# Output : [8, 9, 10]

# print(list1 + 4)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate list (not "int") to list

print(list1 + [4])
# Output : [1, 2, 3, 4]

print(list1)
# Output : [1, 2, 3]

# extend-list method to add more than one element at last to an existing list
list1.extend([4, 5, 6])
print(list1)
# Output : [1, 2, 3, 4, 5, 6]

print(list2)
# Output : [8, 9, 10]

list2 = list2 + [11, 12, 13]
print(list2)
# Output : [8, 9, 10, 11, 12, 13]

print(list1)
# Output : [1, 2, 3, 4, 5, 6]

print(list2)
# Output : [8, 9, 10, 11, 12, 13]

list1 = [1, 2, 3]
print(list1)
# Output : [1, 2, 3]

# Repetition (*)
print(list1 * 2)
# Output : [1, 2, 3, 1, 2, 3]

print(list1)
# Output : [1, 2, 3]

print(list1 * 3)
# Output : [1, 2, 3, 1, 2, 3, 1, 2, 3]

print(list1)
# Output : [1, 2, 3]

# print(list1 * 2.5)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can't multiply sequence by non-int of type 'float'

print(list1)
# Output : [1, 2, 3]

# Membership Operators (in, not in)
print(1 in list1)
# Output : True

print(3 in list1)
# Output : True

print(5 in list1)
# Output : False

print(5 not in list1)
# Output : True

if 5 in list1:
     print('Found 5')
else:
     print('Not Found 5')
# Output : Not Found 5