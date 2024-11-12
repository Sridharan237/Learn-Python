# python program to use the attributes and methods provided by array class in array module
import array
print(dir(array))
# Output : ['ArrayType', '__doc__', '__loader__', '__name__', '__package__', '__spec__', '_array_reconstructor', 'array', 'typecodes']

print(dir(array.array))
# Output : ['__add__', '__buffer__', '__class__', '__class_getitem__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__release_buffer__', '__repr__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'buffer_info', 'byteswap', 'count', 'extend', 'frombytes', 'fromfile', 'fromlist', 'fromunicode', 'index', 'insert', 'itemsize', 'pop', 'remove', 'reverse', 'tobytes', 'tofile', 'tolist', 'tounicode', 'typecode']

a1 = array.array('i', [1, 2, 3, 4, 5])
print(a1)
# Output : array('i', [1, 2, 3, 4, 5])

for x in a1:
    print(x)
'''# Output :    
1
2
3
4
5'''

s = b'abcdef'
print(s)
# Output : b'abcdef'

a2 = array.array('b', s)

print(a2)
# Output : array('b', [97, 98, 99, 100, 101, 102])

print(a2[0])
# Output : 97

print(a2[::-1])
# Output : array('b', [102, 101, 100, 99, 98, 97])

a2.append(103)
print(a2)
# Output : array('b', [97, 98, 99, 100, 101, 102, 103])

print(a2.count(97))
# Output : 1
print(a2[::-1])
# Output : array('b', [103, 102, 101, 100, 99, 98, 97])

a2.extend([104, 105, 106])
print(a2)
# Output : array('b', [97, 98, 99, 100, 101, 102, 103, 104, 105, 106])


'''print(a2.index(250))
# Output : 
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print(a2.index(250))
ValueError: array.index(x): x not in array'''


print(a2.index(106))
# Output : 9

print(a2.itemsize)
# Output : 1


print(a2.pop())
# Output : 106


print(a2)
# Output : array('b', [97, 98, 99, 100, 101, 102, 103, 104, 105])


print(a2.pop(1))
# Output : 98

print(a2)
# Output : array('b', [97, 99, 100, 101, 102, 103, 104, 105])

a2.remove(100)
print(a2)
# Output : array('b', [97, 99, 101, 102, 103, 104, 105])

a2.insert(1, 98)
print(a2)
# Output : array('b', [97, 98, 99, 101, 102, 103, 104, 105])

a2.reverse()
print(a2)
# Output : array('b', [105, 104, 103, 102, 101, 99, 98, 97])

print(a2.typecode)
# Output : 'b'