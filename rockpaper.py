#!/usr/bin/env python3
'''
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, 
and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
'''
import random

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"
CHOICES = [ ROCK, PAPER, SCISSORS ]
BEATENBY = { ROCK: PAPER, PAPER: SCISSORS, SCISSORS: ROCK }

def pickwinner(yourhand, myhand):
    if yourhand == myhand:
        return "a tie"
    elif BEATENBY[myhand] == yourhand:
        return "you"
    else:
        return "me"

if __name__ == "__main__":
    print ("Welcome to the game of ROCK/PAPER/SCISSORS!")
    yourpick = ""
    while yourpick != "Q":
        yourpick = input(f"Please enter your choice {", ".join(CHOICES)}, or Q to Quit: ").lower()
        if (yourpick == "q") or (yourpick not in CHOICES):
            continue
        mypick = random.choice(CHOICES)
        print(f"I pick {mypick}")
        print(f"The winner is {pickwinner(yourpick, mypick)}")
        yourpick = ""  

