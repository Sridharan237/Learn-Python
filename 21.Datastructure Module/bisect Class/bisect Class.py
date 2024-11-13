# python program to use the bisect class

import bisect

l = [10, 20, 20, 30, 40, 50, 60, 70]

bisect.insort(l, 25)
print(l)
# Output : [10, 20, 20, 25, 30, 40, 50, 60, 70]

l.remove(25)

bisect.insort_left(l, 25)
print(l)
# Output : [10, 20, 20, 25, 30, 40, 50, 60, 70]

bisect.insort_left(l, 20)
print(l)
# Output : [10, 20, 20, 20, 25, 30, 40, 50, 60, 70]

bisect.insort_right(l, 20)
print(l)
# Output : [10, 20, 20, 20, 20, 25, 30, 40, 50, 60, 70]

print(bisect.bisect(l, 5))
# Output : 0

print(bisect.bisect(l, 20))
# Output : 5

print(bisect.bisect_left(l, 20))
# Output : 1

print(bisect.bisect_right(l, 20))
# Output : 5