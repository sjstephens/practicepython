#!/usr/bin/env python3
'''
Asks the user for a number and then prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''


if __name__ == "__main__":
    num = int(input("Enter a number and I will return all the divisors: \n"))
    num_list = list(range(1,num+1))
    print(f"list of numbers {num_list} \n")
    divisors = [x for x in num_list if num % x == 0]
    print(f"list of divisors for {num} is {divisors} \n")

    n = int(input("Enter a random number: \n"))
    print([e for e in range(1, n) if n % e == 0])

    
