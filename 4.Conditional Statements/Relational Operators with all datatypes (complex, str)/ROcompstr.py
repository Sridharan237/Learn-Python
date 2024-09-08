# python program to implement relational operators on complex and str datatypes

# 1.complex
# print((5 +2j) < (10+5j))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: '<' not supported between instances of 'complex' and 'complex'

c1 = 5 + 2j
c2 = 10 + 5j

print(c1 == c2)     # False

print(c1 != c2)     # True

# 2.str
print('America' < 'Brazil')     # True

print('antartica' < 'America')  # False

print('brazil' > 'Brazil')      # True

print('america' == 'America')   # False

print('america' != 'America')   # True

