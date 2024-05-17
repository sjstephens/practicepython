#!/usr/bin/env python3
'''
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
 >>> a = [5, 10, 15, 20, 25, 30, 35, 40]
>>> a[1:4]
[10, 15, 20]
>>> a[6:]
[35, 40]
>>> a[:-1]
[5, 10, 15, 20, 25, 30, 35]
 >>> a = [5, 10, 15, 20, 25, 30, 35, 40]
>>> a[1:5:2]
[10, 20]
>>> a[3:0:-1]
[15, 10, 5]
'''

if __name__ == "__main__":
    word = input("Enter a possible palindrome word: ")
    y = []
    wlen = len(word) - 1
    for x in range(wlen + 1):
        y.append(word[wlen-x])
    new_word = ''.join(y)
    if word == new_word:
        print(f"{new_word} is a palindrome of {word}")
    else:
        print(f"{new_word} is not a palindrome of {word}")
    
# Correct answer - String word reversal
# print(s.lower() == s.lower()[::-1])
wrd=input("Please enter a word: ")
wrd=str(wrd.lower())
rvs=wrd[::-1]
print(rvs)
if wrd == rvs:
    print(f"{rvs} is a palindrome of {wrd}")
else:
    print(f"{rvs} is not a palindrome of {wrd}")