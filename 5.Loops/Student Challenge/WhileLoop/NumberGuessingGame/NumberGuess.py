# python program to implement a number guessing game (1-10) using while loop

import random

n = random.randint(1, 10)   # random number in the range-[1, 10]

print('='*5, 'Number Guessing Game', '='*5)

guess = 0

while guess != n:
    guess = int(input('Enter a number between(1-10) : '))

    if guess > n:
        print('Your number is greater')
    elif guess < n:
        print('Your number is smaller')
    else:
        print('You win!')   # Correct Guess