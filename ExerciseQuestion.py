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

#----------------------------------------#
"""
Question 3
Level 1

Question:
With a given integral number n, write a program to generate a dictionary that
contains (i, i*i) such that is an integral number between 1 and n
(both included).
and then the program should print the dictionary.

Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""

"""

Maps the index in a dictionary to its squared value

"""
def MapToSquare(maxNum):
    squaredIndices = dict()
    for i in range(1, maxNum + 1):
        squaredIndices[i] = i * i
    print squaredIndices

#----------------------------------------#
"""
Question 4
Level 1

Question:
Write a program which accepts a sequence of comma-separated numbers from
console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""

"""

Read a sequence of numbers inputted by the user and separated by commas

"""
def ReadSequence():
    numbers = raw_input("Type numbers: ")
    ConvertToList(numbers)
    ConvertToTuple(numbers)
    
"""
Convert a sequence of numbers into a list
"""
def ConvertToList(sequenceNum):
    listOfNum = sequenceNum.split(",")
    print listOfNum

"""
Convert a sequence of numbers into a tuple
"""
def ConvertToTuple(sequenceNum):
    tupleOfNum = sequenceNum
    print tupleOfNum

#----------------------------------#
"""

Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters

"""


class WordManipulator():
    def __init__(self):
        self.word = ""

    def getString(self):
        self.word = raw_input()

    def printString(self):
        print self.word.upper()

def TestWordManipulatorFunctions():
    word = WordManipulator()
    word.getString()
    word.printString()


def main():
    FindRangeOfNumbers(2000, 3200, 7, 5)
    print Factorial(5)
