# python program to implement string methods like : startswith, endswith, removeprefix, removesuffix, partition, rpartition

s = 'python is very easy'

print(s.startswith('python'))  # Output : True
print(s.startswith('py'))  # Output : True
print(s.startswith('is'))  # Output : False
print(s.startswith('is', 7))   # Output : True
print(s.startswith('is', 7, 8))    # Output : False
print(s.startswith('is', 7, 9))    # Output : True
print(s.endswith('easy'))  # Output : True
print(s.endswith('sy'))    # Output : True
s = 'abcd@gmail.com'
print(s.endswith('gmail.com')) # Output : True

s = 'python programming'
print(s.removeprefix('python'))    # Output : ' programming'
print(s.removeprefix('java'))  # Output : 'python programming'
print(s.removesuffix('ming'))  # Output : 'python program'

s = 'python is very easy'
print(s.partition('is'))   # Output : ('python ', 'is', ' very easy')
print(s.partition('hello'))    # Output : ('python is very easy', '', '')
print(s.partition('iam'))  # Output : ('python is very easy', '', '')
print(s.partition('v'))    # Output : ('python is ', 'v', 'ery easy')
print(s.rpartition('very'))    # Output : ('python is ', 'very', ' easy')
print(s.rpartition('hello'))   # Output : ('', '', 'python is very easy')