# python program to implement list comprehension

L = []  # empty list - creation
# (or) L = list() # empty list
print(L)
# Output : []

for x in range(10):
    L.append(x)
print(L)
# Output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

x = [5 if 5 > 3 else 3]
print(x)
# Output : [5]

# x = [x for x in (5, 6, 7, 8) if x > 6 else 'odd']
#   File "<stdin>", line 1
#     x = [x for x in (5, 6, 7, 8) if x > 6 else 'odd']
#                                           ^^^^
# SyntaxError: invalid syntax

# x = [x for x in (5, 6, 7, 8) if x > 6 'odd']
#   File "<stdin>", line 1
#     x = [x for x in (5, 6, 7, 8) if x > 6 'odd']
#                                           ^^^^^
# SyntaxError: invalid syntax

x = [x for x in (5, 6, 7, 8) if x > 6]
print(x)
# Output : [7, 8]

L1 = [x for x in range(10)]
print(L1)
# Output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

L2 = [x**2 for x in range(1, 6)]
print(L2)
# Output : [1, 4, 9, 16, 25]

L3 = [x for x in (10, 5, 7, 8, 12, 3) if x%2==0]
print(L3)
# Output : [10, 8, 12]

L4 = [x.lower() for x in 'Python']
print(L4)
# Output : ['p', 'y', 't', 'h', 'o', 'n']

L5 = [x for x in 'abc123&-*(_def' if x.isalpha()]
print(L5)
# Output : ['a', 'b', 'c', 'd', 'e', 'f']

data = input('Enter names:')
# INPUT : Enter names:james john smith akash
L6 = data.split()
print(L6)
# Output : ['james', 'john', 'smith', 'akash']

L6 = input('Enter names:').split()
# INPUT : Enter names:arun vijay muthu sakthi parotta
print(L6)
# Output : ['arun', 'vijay', 'muthu', 'sakthi', 'parotta']