# python program to implement iterators and generators

# iterators
# list iterators
L = [1, 2, 3, 4, 5]

Literator = iter(L)

print(Literator)
# Output : <list_iterator object at 0x000002779B356D70>
print(type(Literator))
# Output : <class 'list_iterator'>

print(next(Literator))   
# Output : 1
print(next(Literator))   
# Output : 1
print(next(Literator))   
# Output : 1
print(next(Literator))   
# Output : 1
print(next(Literator))   
# Output : 1

# print(next(iterator))   
# Exception : StopIteration - it meDKans the sequence 'L' has been fully iterated


# tuple iterators
T = (1, 2, 3, 4, 5)
Titerator = iter(T)

print(Titerator)
# Output : <tuple_iterator object at 0x000002779B38C1F0>
print(type(Titerator))
# Output : <class 'tuple_iterator'>
print(next(Titerator))
# Output : 1
print(next(Titerator))
# Output : 2
print(next(Titerator))
# Output : 3
print(next(Titerator))
# Output : 4
print(next(Titerator))
# Output : 5

# print(next(iterator))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration


# dictionarykey iterators - only returns keys
d = {'A':1, 'B':2, 'C':3}
DKiterator = iter(d)

print(DKiterator)
# Output : <dict_keyiterator object at 0x000002779B0FDBC0>
print(type(DKiterator))
# Output : <class 'dict_keyiterator'>

# print(next(d))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'dict' object is not an iterator

print(next(DKiterator))
# Output : A
print(next(DKiterator))
# Output : B
print(next(DKiterator))
# Output : C

# print(next(iterator))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

# --------------------------------------------------------------------------------------------------------

# generators
def Days():
    T = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')

    i = 0

    while True:
        x = T[i]
        i = (i+1) % 7
        yield x

d = Days()  # d - generator(iterator), Days() - generator function

print(next(d))  # Output : sunday
print(next(d))  # Output : monday
print(next(d))  # Output : tuesday
print(next(d))  # Output : wednesday
print(next(d))  # Output : thursday
print(next(d))  # Output : friday
print(next(d))  # Output : saturday
print(next(d))  # Output : sunday
print(next(d))  # Output : monday
print(next(d))  # Output : tuesday