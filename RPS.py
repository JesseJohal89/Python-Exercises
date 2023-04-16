#1
"""
Rock, Paper, Scissors
In this project, we’ll build Rock-Paper-Scissors!

The program should do the following:

Prompt the user to select either Rock, Paper, or Scissors.
Instruct the computer to randomly select either Rock, Paper, or Scissors.
Compare the user’s choice and the computer’s choice.
Determine a winner (the user or the computer).
Inform the user who the winner is.

python RPS.py
"""

#2
from random import randint

#3
options = ["ROCK", "PAPER", "SCISSORS"]

#4
message = {
  "tie" : "Yawn it's a tie!",
  "won" : "Yay you won!",
  "lost" : "Aww you lost!"
}

#5 + 6 + 7 + 8 + 9 + 10 + 11
def decide_winner(user_choice, computer_choice):
  print str(user_choice)
  print str(computer_choice)
  if user_choice == computer_choice:
    print message["tie"]
  elif user_choice == options[0] and computer_choice == option[2]:
    print message["won"]
  elif user_choice == options[1] and computer_choice == option[0]:
    print message["won"]
  elif user_choice == options[2] and computer_choice == option[1]:
    print message["won"]
  else: print message["lost"]

#12 + 13 + 14 + 15 + 16
def play_RPS():
  user_choice = raw_input("Enter Rock, Paper, or Scissors: ")
  user_choice = user_choice.upper
  computer_choice = options[randint(0,2)]
  decide_winner(user_choice, computer_choice)

#17
play_RPS()
