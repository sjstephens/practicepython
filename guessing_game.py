#!/usr/bin/env python3
'''
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, 
then tell them whether they guessed too low, too high, or exactly right. 
    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken, 
    and when the game ends, print the count out.
'''
import random

def checkGuess(guess, rnum):
    print(rnum)
    if rnum > guess:
        print("Your guess is to low.")
    elif rnum < guess:
        print("Your guess is to high.")
    else: 
        print("Your guess is spot on.")
    return rnum == guess

if __name__ == "__main__":
    rnum = random.randint(1, 9)
    guess = "y"
    count = 0
    while guess.lower() != "n":
        guess = input("Guess a number between 1 and 9: ")
        count += 1
        if checkGuess(int(guess), rnum) == False:
            guess = input("Try agnother guess? (y/n): ")
    print(f"You played {count} times.")