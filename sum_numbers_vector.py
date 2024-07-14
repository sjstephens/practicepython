#!/usr/bin/env python3
'''
Description:
Input:
Output:
Constraints:

'''
# importing numpy 
import numpy as np 

def vector_math(vector1, vector2):
    # adding both the vector 
    # a + b = (a1 + b1, a2 + b2, a3 + b3) 
    addition = vector1 + vector2 
    # printing addition vector 
    print(f"Vector Addition       : {str(addition)}") 
    # subtracting both the vector 
    # a - b = (a1 - b1, a2 - b2, a3 - b3) 
    subtraction = vector1 - vector2 
    # printing addition vector 
    print(f"Vector Subtraction   : {str(subtraction)}") 
    # multiplying  both the vector 
    # a * b = (a1 * b1, a2 * b2, a3 * b3) 
    multiplication = vector1 * vector2 
    # printing multiplication vector 
    print(f"Vector Multiplication : {str(multiplication)}") 
    # dividing  both the vector 
    # a / b = (a1 / b1, a2 / b2, a3 / b3) 
    division = vector1 / vector2 
    # printing division vector 
    print(f"Vector Division       : {str(division)}") 
    return

# to call script directly
if __name__ == "__main__":
   # creating a 1-D list (Horizontal) 
    list1 = [5, 6, 9] 
    # creating a 1-D list (Horizontal) 
    list2 = [1, 2, 3] 
    # creating first vector 
    vector1 = np.array(list1) 
    # printing vector1 
    print(f"First Vector          : {str(vector1)}") 
    # creating second vector 
    vector2 = np.array(list2) 
    # printing vector2 
    print(f"Second Vector         : {str(vector2)}") 
    vector_math(vector1,vector2)