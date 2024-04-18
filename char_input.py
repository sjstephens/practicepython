#!/usr/bin/env python3
'''
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old. 
Note: for this exercise, the expectation is that you explicitly write out the year 
(and therefore be out of date the next year).
Extras:
Add on to the previous program by asking the user for another number 
and printing out that many copies of the previous message. 
(Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n is the same as pressing the ENTER button)
'''

# importing datetime module for today()  
from datetime import date
      

def calcFuture100(age):
    # Use date function to return year caller turns 100
    today = date.today()
    this_year = today.year
    birth_year = this_year - age
    century_year = birth_year + 100

    return century_year
    

if __name__ == "__main__":
    name = input("what is your name? \n")
    age = int(input("What is your current age? \n"))
    num = int(input("How many times should I print the message? \n"))
    year = calcFuture100(age)
    for i in range(num):
        print(f"Hi {name}, being {age} now, your will be 100 in {year}")