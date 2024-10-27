# python program to implement the method resolution - for all types of inheritances


# Example 1 => single (or) single level inheritance
'''class A:
    pass

class B(A):
    def show(self):
        print('child class B')
        
# creating object for class B
b = B()

print(B.mro())
# Output : [<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]'''

# Example 2 => multilevel inheritance
'''class A:
    pass

class B(A):
    pass
        
class C(B):
    def show(self):
        print('child class B')
        
# creating object for class B
# c = C()

print(C.mro())
# Output : [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]'''

# Example 3 => hierarchical inheritance
'''class A:
    pass

class B(A):
    pass
        
class C(A):
    def show(self):
        print('child class B')

print(B.mro())
# Output : [<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

print(C.mro())
# Output : [<class '__main__.C'>, <class '__main__.A'>, <class 'object'>]'''

# Example 4 =>  multiple inheritance
'''class A:
    pass

class B:
    pass
        
class C(A, B):
    def show(self):
        print('child class B')

print(C.mro())
# Output : [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]'''

# Example 5 => modified version of multiple inheritance
'''class A:
    pass

class B(A):
    pass

class X:
    pass

class Y(X):
    pass
        
class C(B, Y):
    def show(self):
        print('child class B')

print(C.mro())
# Output : [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.Y'>, <class '__main__.X'>, <class 'object'>]'''

# Example 6 => Hybrid inheritance
'''class P:
    pass

class A(P):
    pass

class B(A):
    pass

class X(P):
    pass

class Y(X):
    pass
        
class C(B, Y):
    def show(self):
        print('child class B')

print(C.mro())
# Output : [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.Y'>, <class '__main__.X'>, <class '__main__.P'>, <class 'object'>]'''