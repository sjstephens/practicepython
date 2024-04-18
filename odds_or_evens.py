#!/usr/bin/env python3
'''
Ask the user for a number. 
Depending on whether the number is even or odd, print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?

Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: 
one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. 
If not, print a different appropriate message.
'''

if __name__ == "__main__":
    first_num = int(input("Enter a number and I'll tell you if it is odd or even. \n"))
    if first_num % 2 == 0:
        print("Number is even.")
    else:
        print("Number is odd.")
    divisor = int(input("Enter your own divisor and I'll check that. \n"))
    if first_num % divisor == 0:
        print(f"{first_num} is divisible by {divisor}. \n")
    else:
        print(f"{first_num} is not divisible by {divisor}. \n")