# python program to implement dictionary methods for adding => (copy, update, setdefault, fromkeys) and deleting => (pop, popitem, clear)

dict1 = {101:'Production', 102:'Accounts', 103:'Sales & Marketing', 104:'Inventory'}
print(dict1)
# Output : {101: 'Production', 102: 'Accounts', 103: 'Sales & Marketing', 104: 'Inventory'}

# copy()
dict2 = dict1.copy()
print(id(dict1))
# Output : 2099847607744

print(id(dict2))
# Output : 2099850193280

print(id(dict2[101]))
# Output : 2099850251696

print(id(dict1[101]))
# Output : 2099850251696

dict1[101] = 'Software'
print(dict1)
# Output : {101: 'Software', 102: 'Accounts', 103: 'Sales & Marketing', 104: 'Inventory'}

print(dict2)
# Output : {101: 'Production', 102: 'Accounts', 103: 'Sales & Marketing', 104: 'Inventory'}

print(id(dict1[101]))
# Output : 2099850290544

print(id(dict2[101]))
# Output : 2099850251696

print(dict1)
# Output : {101: 'Software', 102: 'Accounts', 103: 'Sales & Marketing', 104: 'Inventory'}

# update
dict2 = {105:'Designing', 106:'Packaging'}
dict1.update(dict2)
print(dict1)
# Output : {101: 'Software', 102: 'Accounts', 103: 'Sales & Marketing', 104: 'Inventory', 105: 'Designing', 106: 'Packaging'}

print(dict1.get(102))
# Output : 'Accounts'

print(dict1.get(110))
# Output : print(print(dict1.get(110)))

# Output : None

# setdefault
print(dict1.setdefault(102))
# Output : 'Accounts'

dict1.setdefault(110)
print(dict1)
# Output : {101: 'Software', 102: 'Accounts', 103: 'Sales & Marketing', 104: 'Inventory', 105: 'Designing', 106: 'Packaging', 110: None}

dict1.setdefault(110)
print(dict1.setdefault(111, 'Advertisement'))
# Output : 'Advertisement'

print(dict1)
# Output : {101: 'Software', 102: 'Accounts', 103: 'Sales & Marketing', 104: 'Inventory', 105: 'Designing', 106: 'Packaging', 110: None, 111: 'Advertisement'}

print(dict1)
# Output : {101: 'Software', 102: 'Accounts', 103: 'Sales & Marketing', 104: 'Inventory', 105: 'Designing', 106: 'Packaging', 110: None, 111: 'Advertisement'}

dict3 = {}
print(type(dict3))
# Output : <class 'dict'>

# fromkeys()
L = [11, 22, 33, 44]
print(dict3.fromkeys(L))
# Output : {11: None, 22: None, 33: None, 44: None}

print(dict3.fromkeys(L, 100))
# Output : {11: 100, 22: 100, 33: 100, 44: 100}

print(dict3.fromkeys(L, 'hello'))
# Output : {11: 'hello', 22: 'hello', 33: 'hello', 44: 'hello'}

print(dict3)
# Output : {}

print(dict2)
# Output : {105: 'Designing', 106: 'Packaging'}

print(dict1)
# Output : {101: 'Software', 102: 'Accounts', 103: 'Sales & Marketing', 104: 'Inventory', 105: 'Designing', 106: 'Packaging', 110: None, 111: 'Advertisement'}

# pop
print(dict1.pop(102))
# Output : 'Accounts'

print(dict1)
# Output : {101: 'Software', 103: 'Sales & Marketing', 104: 'Inventory', 105: 'Designing', 106: 'Packaging', 110: None, 111: 'Advertisement'}

# print(dict1.pop(112))
# Output : Traceback (most recent call last):

#   File "<stdin>", line 1, in <module>
# KeyError: 112

print(dict1.pop(112, 'Key Not Found'))
# Output : 'Key Not Found'

# popitem
print(dict1.popitem())
# Output : (111, 'Advertisement')

print(dict1.popitem())
# Output : (110, None)

print(dict1)
# Output : {101: 'Software', 103: 'Sales & Marketing', 104: 'Inventory', 105: 'Designing', 106: 'Packaging'}

# clear
dict1.clear()
print(dict1)
# Output : {}
