# python program to find top 3 most common words in a multiline string literal

from collections import Counter

text = '''Python is an easy programmers language.
Python syntax is like the English language.
Python language is easy to learn and adapt to compared with Java and C.
In Python language, the same task can be performed using fewer lines of code.
its easy learning and easy to code.'''

L = text.replace('.', '').split()

# creating Counter object from sequence L
c = Counter(L)

print(c.most_common(3))
# Output : [('Python', 4), ('easy', 4), ('is', 3)]