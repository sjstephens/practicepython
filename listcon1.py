#!/usr/bin/env python3
'''
Given a list saved in a variable: 
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
Write one line of Python that takes this list a and makes a new 
list that has only the even elements of this list in it.
'''

if __name__ == "__main__":
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    evens = ([b for b in a if b % 2 == 0])
    print(evens)