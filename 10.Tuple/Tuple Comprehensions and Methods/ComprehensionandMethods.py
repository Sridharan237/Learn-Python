# python program to implement tuple comprehension and methods

# tuple - comprehension - 2 ways => (1.tuple class constructor, 2.repeating a generator object)
l1 = [x for x in range(10)]
print(l1)
# Output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
t1 = (x for x in range(10))
print(t1)
# Output : <generator object <genexpr> at 0x00000280D7C87340>
t1 = tuple(x for x in range(10))    # 1.tuple class constructor
print(t1)
# Output : (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# t2 = *(x for x in range(10))
#   File "<stdin>", line 1
# SyntaxError: can't use starred expression here

# t3 = (*(x for x in range(10)))
#   File "<stdin>", line 1
#     t3 = (*(x for x in range(10)))
#           ^^^^^^^^^^^^^^^^^^^^^^^
# SyntaxError: cannot use starred expression here

t3 = (*(x for x in range(10)),)     # 2.repeating a generator object
print(t3)
# Output : (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
t4 = ( *(x for x in range(1, 10, 2)), )
print(t4)
# Output : (1, 3, 5, 7, 9)
t5 = ( *(x for x in 'python'), )        
print(t5)
# Output : ('p', 'y', 't', 'h', 'o', 'n')
t5 = ( *(x for x in 'PytHOn' if x.islower()), )
print(t5)
# Output : ('y', 't', 'n')
t6 = tuple((x for x in 'PytHOn' if x.islower()))
print(t6)
# Output : ('y', 't', 'n')
t6 = tuple(x for x in 'PytHOn' if x.islower())
print(t6)
# Output : ('y', 't', 'n')
t7 = tuple(x**2 for x in (1, 3, 5, 7, 9))
print(t7)
# Output : (1, 9, 25, 49, 81)
t8 = tuple(x**2 for x in [2, 4, 6, 8, 10])
print(t8)
# Output : (4, 16, 36, 64, 100)

# tuple - methods
t8 = (1, 2, 3, 4, 5, 4, 3, 2, 5)
print(t8)
# Output : (1, 2, 3, 4, 5, 4, 3, 2, 5)
print(t8.count(3))
# Output : 2
print(t8.count(100))
# Output : 0

# print(t8.index(100))
# # Output : Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: tuple.index(x): x not in tuple

print(t8.index(5))
# Output : 4
print(t8.index(5, 5))
# Output : 8

# print(t8.index(5, 4, 4))
#   Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: tuple.index(x): x not in tuple

print(t8.index(5, 4, 5))
# Output : 4