# python program to implement the string methods(str builin class - member functions) -> find, rfind, index, rindex, count

s = 'hello, how are you'
 
print(s.find('o'))  # Output : 4
print(s.find('o', 5))   # Output : 8
print(s.find('o', 13))  # Output : 16
print(s.find('o', 5, 8))    # Output : -1 -> (Not Found)
print(s.find('o', 5, 9))    # Output : 8

print(s.rfind('you'))   # Output : 15
print(s.rfind('o', 15)) # Output : 16
print(s.rfind('woh'))   # Output : -1 -> (Not Found)
print(s.rfind('woh', 5, 10))    # Output : -1 -> (Not Found)

print(s.index('o')) # Output : 4
print(s.index('o', 5))  # Output : 8
print(s.index('o', 13)) # Output : 16

# print(s.index('o', 5, 8))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: substring not found

# print(s.rindex('woh'))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: substring not found

print(s.rindex('o', 15, 20))    # Output : 16

# print(s.rindex('k', 15, 100))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: substring not found

print(s.rindex('o', 15, 100))   # Output : 16

print(s.count('hello')) # Output : 1
print(s.count(',')) # Output : 1
# 

print(s.count(''))  # Output : 19
print(s.count(' ')) # Output : 3