# python program to implement set methods for adding (add, update, copy) and deleting (pop, discard, remove, clear)

s = {10, 20, 30, 40, 50}
print(s)
# Output : {50, 20, 40, 10, 30}

s.add(60)
print(s)
# Output : {50, 20, 40, 10, 60, 30}

s.add('james')
print(s)
# Output : {50, 'james', 20, 40, 10, 60, 30}

s.update('python')
print(s)
# Output : {'n', 10, 20, 30, 't', 'james', 'o', 'p', 40, 'h', 50, 'y', 60}

s.update((1, 2, 3))
print(s)
# Output : {1, 2, 3, 'n', 10, 20, 30, 't', 'james', 'o', 'p', 40, 'h', 50, 'y', 60}

s.update([11, 22, 33])
print(s)
# Output : {1, 2, 3, 'n', 10, 11, 20, 22, 30, 't', 33, 'james', 'o', 'p', 40, 'h', 50, 'y', 60}

s1 = {1, 2, 3}
print(s)
# Output : {1, 2, 3, 'n', 10, 11, 20, 22, 30, 't', 33, 'james', 'o', 'p', 40, 'h', 50, 'y', 60}

print(s1)
# Output : {1, 2, 3}

s2 = s1.copy()
print(s2)
# Output : {1, 2, 3}

print(id(s1))
# Output : 2765316142496

print(id(s2))
# Output : 2765316831968

s = {10, 20, 30, 40, 50}
print(s)
# Output : {50, 20, 40, 10, 30}

print(s.pop())
# Output : 50

print(s)
# Output : {20, 40, 10, 30}

print(s.pop())
# Output : 20

print(s)
# Output : {40, 10, 30}

print(s.pop())
# Output : 40

print(s)
# Output : {10, 30}

s.discard(10)
print(s)
# Output : {30}

s.discard(100)
print(s)
# Output : {30}

s.remove(30)
print(s)
# Output : set() -> empty set

print(s)
set()
s.update((10, 20, 30))
print(s)
# Output : {20, 10, 30}

# s.remove(100)

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 100

s.clear()
print(s)
# Output : set() -> empty set
