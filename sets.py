#!/usr/bin/env python3
'''
Write a program that returns a list that contains only the elements 
that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.
'''
import random
if __name__ == "__main__":

    # Use of Sets
    #a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    #b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    a = set(random.sample(range(1,30), 12))
    b = set(random.sample(range(1,30), 16))
    #unique_list = set(a + b)
    #print(f"this is a unique set of the two lists {sorted(unique_list)}")
    print(a)
    print(b)
    print(f"this is a unique set of the two lists {sorted(a.intersection(b))}")
       
 
    a = random.sample(range(1,30), 12)
    b = random.sample(range(1,30), 16)
    result = [i for i in a if i in b]

    a = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89}
    b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
    c = {3, 5, 13}
    print(a.union(b)) # Output: frozenset({1, 2, 3, 4, 5, 6})
    # intersection
    print(a.intersection(b)) # Output: frozenset({3, 4})
    # difference
    print(a.difference(b)) # Output: frozenset({1, 2})
    # symmetric_difference
    print(a.symmetric_difference(b)) # Output: frozenset({1, 2, 5, 6})
    # isdisjoint() method
    print(a.isdisjoint(c))  # Output: True
    # issubset() method
    print(c.issubset(a))  # Output: True
    # issuperset() method
    print(b.issuperset(c))  # Output: True
