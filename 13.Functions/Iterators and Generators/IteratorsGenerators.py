# python program to implement iterators and generators

# iterators
L = [1, 2, 3, 4, 5]

iterator = iter(L)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))   # Exception : StopIteration - it means the sequence 'L' has been fully iterated

# generators
def Days():
    T = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')

    i = 0

    while True:
        x = T[i]
        i = (i+1) % 7
        yield x

d = Days()

print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))

