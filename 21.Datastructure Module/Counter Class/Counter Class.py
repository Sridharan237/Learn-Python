# python program to implement counter class of collections module

from collections import Counter

L = ['Mark', 'Jonny', 'David', 'Mark', 'Jonny', 'Mark', 'James', 'Mathew']

c = Counter(L)
print(c)
# Output : Counter({'Mark': 3, 'Jonny': 2, 'David': 1, 'James': 1, 'Mathew': 1})

print(c['Mark'])
# Output : 3

print(c.get('Mark'))
# Output : 3

print(c.keys())
# Output : dict_keys(['Mark', 'Jonny', 'David', 'James', 'Mathew'])

print(c.values())
# Output : dict_values([3, 2, 1, 1, 1])

print(c.update({'Ajay':4}))
# Output : print(c)

# Output : Counter({'Ajay': 4, 'Mark': 3, 'Jonny': 2, 'David': 1, 'James': 1, 'Mathew': 1})

print(c.elements())
# Output : <itertools.chain object at 0x0000024A54F66DA0>

for i in c.elements():
    print(i)
'''Output : 
Mark
Mark
Mark
Jonny
Jonny
David
James
Mathew
Ajay
Ajay
Ajay
Ajay'''

'''print(c.pop())
# Output : Traceback (most recent call last):

  File "<stdin>", line 1, in <module>
TypeError: pop expected at least 1 argument, got 0'''

print(c.pop('Ajay'))
# Output : 4

print(c)
# Output : Counter({'Mark': 3, 'Jonny': 2, 'David': 1, 'James': 1, 'Mathew': 1})

print(c.popitem())
# Output : ('Mathew', 1)

print(c)
# Output : Counter({'Mark': 3, 'Jonny': 2, 'David': 1, 'James': 1})

print(c.most_common())
# Output : [('Mark', 3), ('Jonny', 2), ('David', 1), ('James', 1)]

print(c.most_common(1))
# Output : [('Mark', 3)]

print(c.most_common(2))
# Output : [('Mark', 3), ('Jonny', 2)]

c1 = c.copy()
print(c1)
# Output : Counter({'Mark': 3, 'Jonny': 2, 'David': 1, 'James': 1})

print(id(c))
# Output : 2518276319632

print(id(c1))
# Output : 2518277742000

'''print(id(*c1))
# Output : Traceback (most recent call last):

  File "<stdin>", line 1, in <module>
TypeError: id() takes exactly one argument (4 given)'''