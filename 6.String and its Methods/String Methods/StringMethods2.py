# python program to implement the string functions - for text alignment,  : ljust, rjust, center, lstrip, rstrip, strip

s = 'python'

# Methods for Text Alignment - ljust, rjust, center 
print(s.ljust(10))  # Output : python
print(s.ljust(10)) # Output : 'python    '
print(s.rjust(10)) # Output : '    python'
s.center(len(s)+1, '*') # Output : '*python'
print(s.center(10, '*'))   # Output : '**python**'
print(len(s))   # Output : 6
print(s.ljust(len(s))) # Output : 'python'
print(s.ljust(len(s)+1))   # Output : 'python '

s1 = '   ... ... +++ aaa python'

# Methods for Removing Characters - lstrip, rstrip, strip
print(s1.lstrip()) # Output : '... ... +++ aaa python'
print(s1)  # Output : '   ... ... +++ aaa python'
print(s1.lstrip('.'))  # Output : '   ... ... +++ aaa python'
s2 = s1.lstrip('.')    # s2 - '   ... ... +++ aaa python'
s2 = s1.lstrip()       # s2 - '... ... +++ aaa python'
print(s2)  # Output : '... ... +++ aaa python'
print(s2.lstrip('.'))  # Output : ' ... +++ aaa python'
print(s2.lstrip('.+')) # Output : ' ... +++ aaa python'
print(s2.lstrip()) # Output : '... ... +++ aaa python'
print(s2.lstrip('.+')) # Output : ' ... +++ aaa python'
s2.lstrip('.+ ')    # Output : 'aaa python'
s3 = '... +++ aaa python aaa ... +++'
print(s3.rstrip('+'))  # Output : '... +++ aaa python aaa ... '
print(s3.strip('.+a '))    # Output : 'python'