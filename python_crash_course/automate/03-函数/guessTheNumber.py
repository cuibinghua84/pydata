# -*- coding: utf-8 -*-
"""
@author: 东风
@file: guessTheNumber.py
@time: 2019/12/6 17:07
"""

import random
secretNumber = random.randint(1, 20)
# print(secretNumber)
print('I am thinking of a number between 1 and 20.')

for guessesTaken in range(1, 7):
    print('Take a guess.')
    # print(guessesTaken)
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))

