#!/usr/bin/env python3
'''
Write a program (function!) that takes a list and returns a 
new list that contains all the elements of the first list minus all the duplicates.

Extras:
Write two different functions to do this - one using a loop and constructing a list, 
and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a 
different function.
'''

def removedups(data):
    newlist = []
    for x in data:
        if x not in newlist:
            newlist.append(x) 
    return newlist

# to call script directly
if __name__ == "__main__":
   # Get a list from the user and remove the dups
   indata = input("Enter a comma separated list of values and I'll remove duplicates. \n")
   uniquelist = removedups(indata.strip().split(','))
   print(uniquelist)