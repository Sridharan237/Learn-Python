# python program to use the heapq class

import heapq

h = []  # empty listprint()

heapq.heappush(h, 10)
print(h)
# Output : [10]

heapq.heappush(h, 20)
heapq.heappush(h, 30)
heapq.heappush(h, 40)
heapq.heappush(h, 50)
heapq.heappush(h, 60)
heapq.heappush(h, 70)

print(h)
# Output : [10, 20, 30, 40, 50, 60, 70]

print(heapq.heappop(h))
# Output : 10
print(h)
# Output : [20, 40, 30, 70, 50, 60]
heapq.heappop(h)
20
heapq.heappop(h)
30
print(h)
# Output : [40, 50, 60, 70]


h = [10, 50, 30, 20, 70, 60, 40]

heapq.heapify(h)
print(h)
# Output : [10, 20, 30, 50, 70, 60, 40]

print(heapq.heappop(h))
# Output : 10

print(h)
# Output : [20, 40, 30, 50, 70, 60]

print(heapq.heappop(h))
# Output : 20

print(heapq.heappop(h))
# Output : 30

print(heapq.heappop(h))
# Output : 40

print(heapq.heappop(h))
# Output : 50

print(h)
# Output : [60, 70]

heapq.heappush(h, 50)
print(h)
# Output : [50, 70, 60]

print(heapq.nlargest(2, h))
# Output : [70, 60]

print(heapq.nsmallest(2, h))
# Output : [50, 60]