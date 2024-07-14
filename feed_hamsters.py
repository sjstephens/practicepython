#!/usr/bin/env python3
'''
Description:
Input:"H..H"
Output:Int (-1 if no all fed)
Constraints: OOI

'''
def minimumBuckets(hamsters: str) -> int:
    if hamsters is None or len(hamsters) == 0:
        print("No Hamsters, No Food.")
        return 1
    hamsters = list(hamsters)
    inputsize = len(hamsters)
    hamstersfed = 0
    print(hamsters, hamstersfed)
    for x in range(inputsize-2): # check for H.H
        if hamsters[x] == "H" and hamsters[x+1] == "." and hamsters[x+2] == "H":
            hamstersfed += 1
            hamsters[x] = "X"
            hamsters[x+2] = "X"
            print("H.H")
    for x in range(inputsize-1): # check for .H or H.
        if (hamsters[x] == "." and hamsters[x+1] == "H"):
            hamstersfed += 1
            hamsters[x+1] = "X"
        elif (hamsters[x] == "H" and hamsters[x+1] == "."):
            hamstersfed += 1
            hamsters[x] = "X"
        print(".H or H.")
    if "H" in hamsters:
        hamstersfed=-1

    print(hamsters, hamstersfed)
    return hamstersfed
        

if __name__ == '__main__':
    # List of hamsters and buckets
    usr_input = "H..H"
    #usr_input = ".HHH."
    #usr_input = ".H.H.."
    #usr_input = None
    #usr_input = ""

    fed_status = 0

    fed_status = minimumBuckets(usr_input)
    if (fed_status < 0):
        print("Not enought food!")
    else:
        print("All hamsters have been fed")
