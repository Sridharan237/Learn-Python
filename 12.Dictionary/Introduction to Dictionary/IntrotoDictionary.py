# python program to implement dictionary datatype - CRUD operations

# Create a dictionary
dict1 = {'abacus':'a calculator', 'bachelor':'unmarried person', 'cable':'strong rope'}
print(dict1)
# Output : {'abacus': 'a calculator', 'bachelor': 'unmarried person', 'cable': 'strong rope'}

# Read
print(dict1['abacus'])
# Output : 'a calculator'

print(dict1['bachelor'])
# Output : 'unmarried person'

print(dict1['cable'])
# Output : 'strong rope'

dict2 = {101:'John', 102:'Smith', 103:'Mark', 104:'David'}
print(dict2)
# Output : {101: 'John', 102: 'Smith', 103: 'Mark', 104: 'David'}

print(dict2[102])
# Output : 'Smith'

# Update
dict2[103] = 'Mathew'
print(dict2)
# Output : {101: 'John', 102: 'Smith', 103: 'Mathew', 104: 'David'}

# Create a new key-value pair
dict2[105] = 'Ajay'
print(dict2)
# Output : {101: 'John', 102: 'Smith', 103: 'Mathew', 104: 'David', 105: 'Ajay'}

# Delete a key-value pair
del dict2[103]
print(dict2)
# Output : {101: 'John', 102: 'Smith', 104: 'David', 105: 'Ajay'}

# Some more examples of dictionary
dict3 = {'apple':'red', 'grapes':'green', 'mango':'yellow'}
print(dict3)
# Output : {'apple': 'red', 'grapes': 'green', 'mango': 'yellow'}

dict4 = {'Name':'Ajay', 'Age':20, 'Address':'Delhi', 'Phno':9999888811}
print(dict4)
# Output : {'Name': 'Ajay', 'Age': 20, 'Address': 'Delhi', 'Phno': 9999888811}


# duplicate keys and values are also allowed but last updated value is taken
d = {1:'a', 2:'b', 1:'c'}
print(d)
# Output : {1: 'c', 2: 'b'}

d = {1:'a', 2:'b', 3:'b'}
print(d)
# Output : {1: 'a', 2: 'b', 3: 'b'}

