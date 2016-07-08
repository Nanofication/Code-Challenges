#EXERCISE QUESTIONS

import math

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

#----------------------------------------#

"""
Question 6
Level 2

Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24

Hints:
If the output received is in decimal form, it should be rounded off to its
nearest value
(for example, if the output received is 26.0, it should be printed as 26)
In case of input data being supplied to the question,
it should be assumed to be a console input. 
"""

"""
Reads an input of numbers and stores them into a list
"""
def ReadInput():
    stringInputs = raw_input("Input numbers: ")
    numbers = list()
    
    groupOfNum = list(stringInputs.split(",")) #Store into a list
    for num in groupOfNum:
        numbers.append(int(num))
    return numbers

"""
Calculate the equation (Square root of [2* C * D)/H]
C is 50 and H is 30 and D is each number from the list of numbers
"""
def CalculateEquation(numbers):
    c = 50
    h = 30
    outputs = list()
    for i in numbers:
        outputs.append(round(math.sqrt(2 * c * float(i)/h)))
    return outputs

"""
Print the outputs
"""
def PrintOutputs(outputs):
    for i in outputs:
        print str(i) + ", ",
        
"""
Combines all three functions to solve question three
"""
def ResolveQuestionSix():
    numbers = ReadInput()
    outputs = CalculateEquation(numbers)
    PrintOutputs(outputs)

def main():
    FindRangeOfNumbers(2000, 3200, 7, 5)
    print Factorial(5)
