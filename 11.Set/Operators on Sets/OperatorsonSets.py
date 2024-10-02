# python program to implement set operatos like => |, &, -, ^, <, <=, >, >=, ==, != , in, not in, is, is not

S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
A = {1, 2, 3, 5, 7}
B = {5, 7, 9, 10, 11}

print(A | B)
#Output : {1, 2, 3, 5, 7, 9, 10, 11}

print(A & B)
#Output : {5, 7}

print(A - B)
#Output : {1, 2, 3}

print(A ^ B)
#Output : {1, 2, 3, 9, 10, 11}

print(A < S)
#Output : True

print(A <= S)
#Output : True

print(S <= S)
#Output : True

print(S > A)
#Output : True

print(S > B)
#Output : False

print(A > S)
#Output : False

print(S <= A)
#Output : False

print(A <= S)
#Output : True

print(S == S)
#Output : True

print(S >= A)
#Output : True

print(S == A)
#Output : False

print(S != A)
#Output : True

print(10 in S)
#Output : True

print(11 in A)
#Output : False

print(11 not in A)
#Output : True

print({1, 2} in S)
#Output : False

# C = {{1, 2}, 3}

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'set'

C = [{1, 2}, 3, 4]
print({1, 2} in C)
#Output : True

C = ({1, 2}, 3, 4)
print({1, 2} in C)
#Output : True
