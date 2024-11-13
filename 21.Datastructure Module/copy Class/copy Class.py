# python program to use the copy class 

import copy

L = [10, 20, 30, 40, 50]

# shallow copy - copy()

L1 = copy.copy(L)

print(L1)
# Output : [10, 20, 30, 40, 50]

print(id(L1))
# Output : 2855164844928

print(id(L))
# Output : 2855161346304

print(id(L[0]))
# Output : 140705631378136

print(id(L1[0]))
# Output : 140705631378136




L = [10, 20, 30, 40, 50]

# deep copy - deepcopy()
L1 = copy.deepcopy(L)

print(L1)
# Output : [10, 20, 30, 40, 50]

print(id(L))
# Output : 2855165203264

print(id(L1))
# Output : 2855161346304

print(id(L[0]))
# Output : 140705631378136

print(id(L1[0]))
# Output : 140705631378136

# class for a person
class Person:
    def __init__(self, name):
        self.name = name

L = [Person('Ajay'), Person('Vijay'), Person('Arun'), Person('Venkat')]

print(L)
# Output : [<__main__.Person object at 0x00000298C51C8DD0>, <__main__.Person object at 0x00000298C51C8DA0>, <__main__.Person object at 0x00000298C51C8E00>, <__main__.Person object at 0x00000298C51C8E90>]

# deep copy - deepcopy()
L1 = copy.deepcopy(L)

print(id(L))
# Output : 2855165208192

print(id(L1))
# Output : 2855165203264

print(id(L[0]))
# Output : 2855165267408

print(id(L1[0]))
# Output : 2855165266304

print(L1)
# Output : [<__main__.Person object at 0x00000298C51C8980>, <__main__.Person object at 0x00000298C51C8EF0>, <__main__.Person object at 0x00000298C51C88F0>, <__main__.Person object at 0x00000298C51C8F80>]