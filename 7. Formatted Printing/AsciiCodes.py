# python program to implement builtin functions like : ord, chr

s = 'A'
print(ord(s))  # Output : 65

s = ''
# print(ord(s))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: ord() expected a character, but string of length 0 found

s = ' '
print(ord(s))  # Output : 32

s = '   '
# print(ord(s))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: ord() expected a character, but string of length 3 found

print(chr(65)) # Output : 'A'
print(chr(32)) # Output : ' '