#!/usr/bin/env python3
'''
Return the first and last values in a list of numbers.
'''
def getinteger(prompt = "Enter a number: "):
    return int(input(prompt))

def getvalue(nlist, idx = 0):
    return nlist[idx]

# to call script directly
if __name__ == "__main__":
   cnt_list = getinteger("How many numbers in the list? ")
   num_list = list(range(1, cnt_list, 5))

   print(num_list)
   print(f"first {getvalue(num_list)}, last {getvalue(num_list, -1)}.")