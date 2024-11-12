# python program to perform operations using the deque class of collections module

from collections import deque

L = [1, 2, 3, 4, 5]

# creating a deque object
q = deque(L)

print(q)
# Output : deque([1, 2, 3, 4, 5])

q.append(6)
print(q)
# Output : deque([1, 2, 3, 4, 5, 6])

q.appendleft(7)
print(q)
# Output : deque([7, 1, 2, 3, 4, 5, 6])

print(q.pop())
# Output : 6
print(q)
# Output : deque([7, 1, 2, 3, 4, 5])

print(q.popleft())
# Output : 7
print(q)
# Output : deque([1, 2, 3, 4, 5])

q.extend([10, 20, 30])
print(q)
# Output : deque([1, 2, 3, 4, 5, 10, 20, 30])

q.extendleft([11, 22, 33])
print(q)
# Output : deque([33, 22, 11, 1, 2, 3, 4, 5, 10, 20, 30])

print(q.count(1))
# Output : 1

print(q.index(1))
# Output : 3

q.rotate(2)
print(q)
# Output : deque([20, 30, 33, 22, 11, 1, 2, 3, 4, 5, 10])

q.remove(20)
print(q)
# Output : deque([30, 33, 22, 11, 1, 2, 3, 4, 5, 10])

q.insert(0, 20)
print(q)
# Output : deque([20, 30, 33, 22, 11, 1, 2, 3, 4, 5, 10])

q.reverse()
print(q)
# Output : deque([10, 5, 4, 3, 2, 1, 11, 22, 33, 30, 20])
