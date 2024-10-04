# python program to iterate over a dictionary

dict1 = {101:'Production', 102:'Accounts', 103:'Sales & Marketing', 104:'Inventory'}
print(dict1)
# Output : {101: 'Production', 102: 'Accounts', 103: 'Sales & Marketing', 104: 'Inventory'}

for x in dict1:
     print(x)
''' Output : 
101
102
103
104
'''

for x in dict1:
     print(x, dict1[x])
''' Output :
101 Production
102 Accounts
103 Sales & Marketing
104 Inventory
'''

for x in dict1:
     print(x, dict1.get(x))
''' Output :
101 Production
102 Accounts
103 Sales & Marketing
104 Inventory
'''

print(dict1[102])
# Output : 'Accounts'

print(dict1.get(102))
# Output : 'Accounts'

# print(dict1[106])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 106

dict1.get(106)
# Output : Nothing

print(print(dict1.get(106)))
# Output : None

print(dict1.get(106, "Invalid key"))
# Output : 'Invalid key'

print(dict1.keys())
# Output : dict_keys([101, 102, 103, 104])

print(dict1.values())
# Output : dict_values(['Production', 'Accounts', 'Sales & Marketing', 'Inventory'])

print(dict1.items())
# Output : dict_items([(101, 'Production'), (102, 'Accounts'), (103, 'Sales & Marketing'), (104, 'Inventory')])

for k in dict1.keys():
     print(k, dict1[k])
''' Output : 
101 Production
102 Accounts
103 Sales & Marketing
104 Inventory
'''

for v in dict1.values():
     print(v)
''' Output : 
Production
Accounts
Sales & Marketing
Inventory
'''

for item in dict1.items():
     print(item)

''' Output : 
(101, 'Production')
(102, 'Accounts')
(103, 'Sales & Marketing')
(104, 'Inventory')
'''

for x, y in dict1.items():
     print(x, y)

''' Output : 
101 Production
102 Accounts
103 Sales & Marketing
104 Inventory
'''

for (x, y) in dict1.items():
     print(x, y)
''' Output : 
101 Production
102 Accounts
103 Sales & Marketing
104 Inventory
'''

for [x, y] in dict1.items():
     print(x, y)
''' Output : 
101 Production
102 Accounts
103 Sales & Marketing
104 Inventory
'''