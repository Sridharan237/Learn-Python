# python program to use the functions provided by random module 

import random

# random function
print(random.random())
# Output : 0.39900395626306573

print(random.random())
# Output : 0.6418893647413728

print(random.random())
# Output : 0.42289728718502284

# uniform function
print(random.uniform(1, 10))
# Output : 7.214901630423267

print(random.uniform(1, 10))
# Output : 6.9920650566318505

print(random.uniform(1, 10))
# Output : 3.551700526115585

print(random.uniform(1, 10))
# Output : 4.721964537696148

# seed function
random.seed(10)
print(random.random())
# Output : 0.5714025946899135

print(random.random())
# Output : 0.4288890546751146


print(random.random())
# Output : 0.5780913011344704


random.seed(10)
print(random.random())
# Output : 0.5714025946899135

print(random.random())
# Output : 0.4288890546751146

print(random.random())
# Output : 0.5780913011344704

# randint function
print(random.randint(1, 10))
# Output : 4

print(random.randint(1, 10))
# Output : 8

print(random.randint(1, 10))
# Output : 8

print(random.randint(1, 10))
# Output : 5

print(random.randint(1, 10))
# Output : 3

# randrange function
print(random.randrange(1, 10, 2))
# Output : 1

print(random.randrange(1, 10, 2))
# Output : 9

print(random.randrange(1, 10, 2))
# Output : 7

print(random.randrange(1, 10, 2))
# Output : 5

print(random.randrange(1, 10, 2))
# Output : 1


print(range(1, 10, 2))
# Output : range(1, 10, 2)

print(list(range(1, 10, 2)))
# Output : [1, 3, 5, 7, 9]


L = ['Anita', 'Venkat', 'Prabhu', 'Varun']

# choice function
print(random.choice(L))
# Output : 'Prabhu'

print(random.choice(L))
# Output : 'Varun'

print(random.choice(L))
# Output : 'Venkat'

print(random.choice(L))
# Output : 'Prabhu'

# choices function
print(random.choices(L))
# Output : ['Prabhu']

print(random.choices(L, k=2))
# Output : ['Anita', 'Varun']

print(random.choices(L, k=2))
# Output : ['Varun', 'Varun']

print(random.choices(L, k=2))
# Output : ['Prabhu', 'Anita']

print(random.choices(L, k=2))
# Output : ['Anita', 'Anita']

print(random.choices(L, k=2))
# Output : ['Varun', 'Venkat']

# sample function
print(random.sample(L, k=2))
# Output : ['Prabhu', 'Anita']

print(random.sample(L, k=2))
# Output : ['Prabhu', 'Varun']

print(random.sample(L, k=2))
# Output : ['Varun', 'Venkat']

print(random.sample(L, k=2))
# Output : ['Varun', 'Anita']

# shuffle function
random.shuffle(L)
print(L)
# Output : ['Venkat', 'Anita', 'Varun', 'Prabhu']

random.shuffle(L)
print(L)
# Output : ['Varun', 'Venkat', 'Prabhu', 'Anita']

random.shuffle(L)
print(L)
# Output : ['Prabhu', 'Venkat', 'Anita', 'Varun']

# getstate function
state = random.getstate()

print(random.random())
# Output : 0.30116425319003204

print(random.random())
# Output : 0.6066772167227487

print(random.random())
# Output : 0.07203477273496783

print(random.random())
# Output : 0.9242676783734988

# setstate function
random.setstate(state)
print(random.random())
# Output : 0.30116425319003204

print(random.random())
# Output : 0.6066772167227487

print(random.random())
# Output : 0.07203477273496783

print(random.random())
# Output : 0.9242676783734988

# getrandbits function
print(random.getrandbits(3))
# Output : 0

print(random.getrandbits(3))
# Output : 1

print(random.getrandbits(3))
# Output : 3

print(random.getrandbits(3))
# Output : 4

print(random.getrandbits(3))
# Output : 7
