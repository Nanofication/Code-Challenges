#EXERCISE QUESTIONS

"""

Solving python programming exercises posed by Zhiwehu

"""

"""
Question 1
Level 1

Question:
Write a program which will find all such numbers which are divisible by 7 but
are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence
on a single line.

"""

"""
Find numbers between two other numbers that are also included.
It is divisible by one number but not by the other.
"""
def FindRangeOfNumbers(minimum, maximum, isFactor, notFactor):
    for i in range(minimum, maximum):
        if (i % isFactor == 0) and (i % notFactor != 0):
            print str(i) + ", ",
    
#----------------------------------------#

"""

Question 2
Level 1

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

"""

"""
Computes the factorial of a given number
"""
def Factorial(number):
    if (number == 1):
        return 1
    return (number * Factorial(number - 1))

def main():
    #FindRangeOfNumbers(2000, 3200, 7, 5)
    print Factorial(5)
