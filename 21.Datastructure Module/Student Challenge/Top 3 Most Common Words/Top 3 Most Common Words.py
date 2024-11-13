# python program to find top 3 most common words in a multiline string literal

from collections import Counter
import re

f = open('D://Learn-Github-Repositories//Learn Python Programming - Beginner to Master//21.Datastructure Module//Student Challenge//text.txt', 'r')

text = f.read()

words = re.findall('\w+', text)

# creating Counter object from sequence 'words'
c = Counter(words)

print(c.most_common(3))
# Output : [('Python', 4), ('easy', 4), ('language', 4)]