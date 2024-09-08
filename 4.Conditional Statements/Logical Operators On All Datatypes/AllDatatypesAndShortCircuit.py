# python program to implement logical operators can handle all datatypes in all different combinations and to implement short circuit operation

# logical operators with all datatypes
print(5 and 6)          # Output : 6
print(-5 and 6)         # Output : 6
print(5 or 6)           # Output : 5
print('' or 6)          # Output : 6
print('' or 0)          # Output : 0
print(5+2j and 10+5j)   # Output : (10+5j)
print(5+2j and 0j)      # Output : 0j
print(0+0j and 0j)      # Output : 0j
print('hi' and 5)       # Output : 5
print(5 and 'hi')       # Output : hi
print('hi' and 'bye')   # Output : bye
print('bye' and True)   # Output : True

# short circuit - means the breaking of logical operators like and, or to not to move to the next given operand is called short circuit (or) butterfly effect
print(5 and 6)          # Output : 6
print(5 and 0)          # Output : 0
print(0 and 5)          # Output : 0
print(0 and '')         # Output : 0
print(5 or 6)           # Output : 5
print(5 or 0)           # Output : 5
print(0 or 5)           # Output : 5
print(0 or '')          # Output : '' -> (empty string)
print('' or 'hi')       # Output : hi
print('hi' or 'bye')    # Output : hi
print('hi' or '')       # Output : hi