# python program to implement the string function - for changing cases : capitalize, title, lower, upper, swapcase, casefold 

s = 'hello dear'
print(s.capitalize())  # Output : 'Hello dear'
print(s)   # Output : 'hello dear'
s1 = s.capitalize()
print(s1)  # Output : 'Hello dear'
s = 'HELLO how Are YOU'
print(s.capitalize())  # Output : 'Hello how are you'
print(s)   # Output : 'HELLO how Are YOU'
print(s.upper())   # Output : 'HELLO HOW ARE YOU'
print(s.lower())   # Output : 'hello how are you'
print(s.swapcase())    # Output : 'hello HOW aRE you'
print(s.title())   # Output : 'Hello How Are You'
print(s.casefold())    # Output : 'hello how are you'

# Example - for difference between lower and casefold
s1 = 'heLLo'
s2 = 'HELLO'
print(s1 == s2)    # Output : False
print(s1.lower() == s2.lower())    # Output : True
s1 = 'Bu\u00DF'
print(s1)  # Output : 'Buß'
s2 = 'Buss'
print(s1.lower() == s2.lower())    # Output : False
print(s1.casefold() == s2.casefold())  # Output : True
s3 = '\u01c6'
print(s3)  # Output : 'ǆ'

# s4 = '\U01C6'
#   File "<stdin>", line 1
#     s4 = '\U01C6'
#          ^^^^^^^^
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 0-5: truncated \UXXXXXXXX escape

# Example - for digraph letter
s4 = '\u01C6'
print(s4)  # Output : 'ǆ'
print(s4.upper())  # Output : 'Ǆ'
print(s4.lower())  # Output : 'ǆ'
print(s4.title())  # Output : 'ǅ'