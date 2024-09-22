# python program to implement list methods => (index, count, reverse, sort) and global collection function => sorted

# index method
L1 = [5, 6, 7, 5, 8, 9, 6, 10, 6]
print(L1.index(8))
# Output : 4
print(L1.index(10))
# Output : 7

# print(L1.index(100))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: 100 is not in list

print(L1.index(6, 2))
# Output : 6
print(L1.index(6, 1, 5))
# Output : 1

# count method
print(L1.count(6))
# Output : 3
print(L1.count(8))
# Output : 1
print(L1.count(100))
# Output : 0

# reverse method
L1.reverse()
print(L1)
# Output : [6, 10, 6, 9, 8, 5, 7, 6, 5]

# sort method
L1.sort()
print(L1)
# Output : [5, 5, 6, 6, 6, 7, 8, 9, 10]

L1.sort(reverse=True)
print(L1)
# Output : [10, 9, 8, 7, 6, 6, 6, 5, 5]

L1 = ['yy', 'jj', 'mm', 'BB', 'aa', 'ZZ']
L1.sort()
print(L1)
# Output : ['BB', 'ZZ', 'aa', 'jj', 'mm', 'yy']

print(ord('a'))
# Output : 97
print(ord('A'))
# Output : 65

L1.sort(key=str.lower)
print(L1)
# Output : ['aa', 'BB', 'jj', 'mm', 'yy', 'ZZ']
L1.sort(key=str.lower, reverse=True)
print(L1)
# Output : ['ZZ', 'yy', 'mm', 'jj', 'BB', 'aa']

# sorted - global collection function 
print(sorted(L1))
# Output : ['BB', 'ZZ', 'aa', 'jj', 'mm', 'yy']

# print(sorted(L1, key=ord, reverse=True))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: ord() expected a character, but string of length 2 found

print(sorted(L1, key=len, reverse=True))
# Output : ['ZZ', 'yy', 'mm', 'jj', 'BB', 'aa']

print(sorted(L1, key=len))
# Output : ['ZZ', 'yy', 'mm', 'jj', 'BB', 'aa']

print(sorted(L1, key=len, reverse=False))
# Output : ['ZZ', 'yy', 'mm', 'jj', 'BB', 'aa']

print(sorted(L1, key=len))
# Output : ['ZZ', 'yy', 'mm', 'jj', 'BB', 'aa']

print(sorted(L1, key=str.lower))
# Output : ['aa', 'BB', 'jj', 'mm', 'yy', 'ZZ']
