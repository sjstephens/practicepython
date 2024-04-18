#!/usr/bin/env python3
'''
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old. 
Note: for this exercise, the expectation is that you explicitly write out the year 
(and therefore be out of date the next year).
'''

# importing datetime module for now()  
from datetime import date
      

def calcFuture100(age):
    # using now() to get current time  
    today = date.today()
    this_year = today.year
    birth_year = this_year - age
    century_year = birth_year + 100

    return century_year
    

if __name__ == "__main__":
    name = input("what is your name? \n")
    age = input("What is your current age? \n")
    year = calcFuture100(int(age))
    print(f"Hi {name}, being {age} now, your will be 100 in {year}")