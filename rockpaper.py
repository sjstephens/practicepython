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

def getchoice(prompt = "Enter a number: "):
    return input(prompt)

def pickwinner(hand1, hand2):
    if hand1 == hand2:
        winner = "a tie!"
    elif hand1 == "rock" and hand2 == "scissors":
        winner = "you!"
    elif hand1 == "scissors" and hand2 == "paper":
        winner = "you!"
    elif hand1 == "Paper" and hand2 == "rock":
        winner = "you!"
    else:
        winner = "me!"
    return winner

if __name__ == "__main__":
    print ("Welcome to the game of ROCK/PAPER/SCISSORS!")
    choices = ["rock", "paper", "scissors"]
    yourpick = ""
    while yourpick != "q":
        yourpick = getchoice("Please enter your choice (rock, paper, scissors), q to quit: ")
        if (yourpick == "q") or (yourpick not in choices):
            continue
        mypick = random.choice(choices)
        print(f"I pick {mypick}")
        print(f"The winner is {pickwinner(yourpick, mypick)}")
        yourpick = None  

