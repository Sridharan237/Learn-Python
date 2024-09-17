# python program to implement relational operators (or) comparison operators on strings

s1 = 'alaska'
s2 = 'canada'
s3 = 'Alaska'
s4 = 'abcde'
s5 = 'abcdf'

print(s1 > s2)  # Output : False
print(s1 < s2)  # Output : True
print(s1 > s3)  # Output : True
print(s1 <= s3) # Output : False
print(s4 <= s5) # Output : True
print(s4 == s5) # Output : False
print(s4 != s5) # Output : True
print(s4[:len(s4)-1:] == s5[:len(s5)-1:])   # Output : True