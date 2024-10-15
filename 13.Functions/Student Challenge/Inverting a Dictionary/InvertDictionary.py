# python program to implement a function which inverts a dictionary => inverting a dictionary means 'key to values' and 'values to keys'

# function which inverts a dictionary => inverting a dictionary means 'key to values' and 'values to keys'
def invertDictionary(dictionary):
    keys = dictionary.keys()
    values = dictionary.values()
    
    invertedDict = dict(zip(values, keys))
    
    return invertedDict

d = {'a':10, 'b':20, 'c':30, 'd':40, 'e':40}

print(invertDictionary(d))
# Output : {10: 'a', 20: 'b', 30: 'c', 40: 'e'}