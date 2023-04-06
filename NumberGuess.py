"""
Python Exercise
Number Guess

Wanna play a game? In this project, we’ll build a program that rolls a pair of dice and asks the user to guess the sum. If the user’s guess is equal to the total value of the dice roll, the user wins! Otherwise, the computer wins.

The program should do the following:
  Roll a pair of dice.
  Add the values of the roll.
  Ask the user to guess a number.
  Compare the user’s guess to the total value.
  Determine the winner (user or computer).

python NumberGuess.py
"""

from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Guess a number: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum possible value is: %d" % max_val
  guess = get_user_guess()
  if guess > max_val:
    print "invalid guess"
  else: print "rolling..."
  sleep(2)
  print "the 1st roll is %d" % (first_roll)
  sleep(1)
  print "the 2nd roll is %d" % (second_roll)
  sleep(1)
  total_roll = first_roll + second_roll
  print total_roll
  print "result"
  sleep(1)
  if guess == total_roll:
   print "you've won tickets to listen to my dirt road diary!"
  else: print "you didn't win unfortunatly, however you don't get to leave empty handed..."
  sleep(2)
  print "you get to have a handful of deez nutz"
  
roll_dice(6)



