#!/usr/bin/env python3
'''
The median of a list of numbers is essentially its middle element after sorting. 
The same number of elements occur after it as before. Given a list of numbers 
with an odd number of elements, find the median?
Example:[1,2,3,4,5]
The sorted array . The middle element and the median is 3.
Parameters:
int arr[n]: an unsorted array of integers
Output: 
int: the median of the array
Constraints:
Input is between -10000 to 10000
Array length is odd
'''

def validateInput(data, valmsg):
    valid_input = True
    if len(data) == 0:
        valmsg = "You must enter an odd length of comma separated numbers."
        valid_input = False
    #if len(data) % 2 != 0:
        #valmsg = "Length of list must be an odd number."
       # valid_input = False
    return valid_input, valmsg

def findMedian(data):
    data = sorted(data) 
    n = len(data) 
    if n == 0: 
        print("no median for empty data")
        exit(1)
    if n % 2 == 0: 
        showmedian = (data[n // 2 - 1] + data[n // 2]) / 2 
    else: 
        showmedian = data[n // 2] 
    print(showmedian)

    return showmedian

# to call script directly
if __name__ == "__main__":
    # Accept odd number of integers and find the median
    valid_input = True
    while valid_input is True:
        err_msg = ""
        indata = input("Enter a list comma separated list of numbers and I'll return the median. \nType 'q' to quit\n")
        if indata.lower() == "q":
            print("Thanks for playing!")
            valid_input = False
        else:
            data_list = data_list = list(map(int, indata.split(',')))
            valid_input, err_msg = validateInput(data_list, err_msg)
            if  valid_input is True:
                showmedian = findMedian(data_list)
                print(f"Your median is {showmedian}.")
            else:
                print(err_msg)
                valid_input = False