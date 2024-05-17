#!/usr/bin/env python3
'''
Task #1 divisors
Asks the user for a number and then prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''
'''
Task 2)
Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.). 
'''
def getinteger(prompt = "Enter a number: "):
    return int(input(prompt))

def getdivisors(num):
    # Get divisors if number is not prime
    num_list = list(range(2,num))
    a = [x for x in num_list if num % x == 0]
    return a

if __name__ == "__main__":
    num = getinteger("Enter a potential prime number: ")
    a = getdivisors(num)
    if a:
        print(f"{num} is not prime number, divisors are {a}.")
    else:
        print(f"{num} is a prime number")

    ''' Task #1
    num = int(input("Enter a number and I will return all the divisors: \n"))
    num_list = list(range(1,num+1))
    print(f"list of numbers {num_list} \n")
    divisors = [x for x in num_list if num % x == 0]
    print(f"list of divisors for {num} is {divisors} \n")

    n = int(input("Enter a random number: \n"))
    print([e for e in range(1, n) if n % e == 0])
    '''
    
