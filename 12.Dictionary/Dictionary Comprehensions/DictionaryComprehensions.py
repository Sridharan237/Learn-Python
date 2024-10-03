# python program to implement dictionary comprehensions

dict1 = dict()
print(dict1)
# Output : {}

dict1 = {}
print(dict1)
# Output : {}

print(type(dict1))
# Output : <class 'dict'>

dict1['apple'] = 'red'
dict1['mango'] = 'yellow'
print(dict1)
# Output : {'apple': 'red', 'mango': 'yellow'}

for x in range(1, 6):
    dict1[x] = x**2
    
print(dict1)
# Output : {'apple': 'red', 'mango': 'yellow', 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

dict5 = {}
print(type(dict5))
# Output : <class 'dict'>

dict5
{}
for x in range(1, 6):
    dict5[x] = 2*x

print(dict5)
# Output : {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

# Dictionary Comprehensions
dict2 = dict( ( (1, 2), (2, 4), (3, 6) ) )
print(dict2)
# Output : {1: 2, 2: 4, 3: 6}

dict2 = dict( ( [1, 11], [2, 22], [3, 33] ) )
print(dict2)
# Output : {1: 11, 2: 22, 3: 33}

dict2 = dict( ('ab', 'bc', 'cd') )
print(dict2)
# Output : {'a': 'b', 'b': 'c', 'c': 'd'}

# dict2 = dict( ( [1, 11, 111], [2, 22, 222], [3, 33, 333] ) )
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: dictionary update sequence element #0 has length 3; 2 is required

L1 = [(1, 2), (5, 6), (8, 9)]
dict2 = dict(L1)
print(dict2)
# Output : {1: 2, 5: 6, 8: 9}

L1 = ['A', 'B', 'C']
L2 = ['Apple', 'Ball', 'Cat']
dict3 = dict(zip(L1, L2))
print(dict3)
# Output : {'A': 'Apple', 'B': 'Ball', 'C': 'Cat'}

set1 = {7, 8, 9}
str1 = 'AJK'
dict3 = dict(zip(set1, str1))
print(dict3)
# Output : {8: 'A', 9: 'J', 7: 'K'}

dict3 = dict( zip( [10, 20, 30], [101, 102, 103, 104, 105] ) )
print(dict3)
# Output : {10: 101, 20: 102, 30: 103}

L1 = ['A', 'B', 'C']
print(enumerate(L1))
# Output : <enumerate object at 0x00000188E057DCB0>

print(list(enumerate(L1)))
# Output : [(0, 'A'), (1, 'B'), (2, 'C')]

print(zip([1, 2, 3], ['A', 'B', 'C']))
# Output : <zip object at 0x00000188E095A900>

print(list(zip([1, 2, 3], ['A', 'B', 'C'])))
# Output : [(1, 'A'), (2, 'B'), (3, 'C')]

for item in enumerate(L1):
    print(item)

''' Output : 
(0, 'A')
(1, 'B')
(2, 'C')
'''

dict4 = dict( enumerate(L1) )
print(dict4)
# Output : {0: 'A', 1: 'B', 2: 'C'}

print(type(dict4))
# Output : <class 'dict'>

dict5 = { x:x**2 for x in range(1, 6) }
print(dict5)
# Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

dict6 = { (x, x**2) for x in range(1, 6) }
print(dict6)
# Output : {(2, 4), (4, 16), (1, 1), (3, 9), (5, 25)}

print(type(dict6))
# Output : <class 'set'>

# dict7 = { [x, x**2] for x in range(1, 6) }
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'list'

dict7 = dict( (x, x**2) for x in range(1, 6) )
print(dict7)
# Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

dict8 = dict( [x, x**2] for x in range(1, 6) )
print(dict8)
# Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

L1 = [1, 2, 3]
L2 = ['A', 'B', 'C']
for x, y in zip(L1, L2):
    print(x, y)
''' Output : 
1 A
2 B
3 C
'''

# for x, y in zip(L1, L2):
#     x, y
''' Output : 
# (1, 'A')
# (2, 'B')
# (3, 'C')
'''

dict8 = dict( (x, y) for x, y in zip(L1, L2) )
print(dict8)
# Output : {1: 'A', 2: 'B', 3: 'C'}

dict8 = { x:y for x, y in zip(L1, L2) }
print(dict8)
# Output : {1: 'A', 2: 'B', 3: 'C'}

for x, y in enumerate(L2):
    print(x, y)
'''
0 A
1 B
2 C
'''

# for x, y in enumerate(L2):
#     x, y
# ''' Output : 
# (0, 'A')
# (1, 'B')
# (2, 'C')
# '''

dict9 = dict( (x, y) for x, y in enumerate(L2) )
print(dict9)
# Output : {0: 'A', 1: 'B', 2: 'C'}

dict9 = { x:y for x, y in enumerate(L2) }
print(dict9)
# Output : {0: 'A', 1: 'B', 2: 'C'}
