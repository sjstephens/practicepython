#!/usr/bin/env python3
'''
Take a list and print out all the elements of the list that are less than 5.
Extras:
Instead of printing the elements one by one, 
make a new list that has all the elements less than 5 from this list in it 
and print out this new list. Write this in one line of Python.
Ask the user for a number and return a list that contains 
only elements from the original list a that are smaller than that number given by the user.
'''

if __name__ == "__main__":
    test_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print("Printing the list of numbers less than 5. \n")
    new_list = []
    for i in test_list:
        if i < 5:
            new_list.append(i)
            print(i)
    print(f"This is the new list: {new_list}. \n")
    num = int(input("Enter a number and I'll return the list of everything below that number. \n"))
    print( [x for x in test_list if x < num] )

