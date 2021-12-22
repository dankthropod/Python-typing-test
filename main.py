import time
import random
from getkey import getkey

def generateTest():
    mylines = []                              
    with open ('phrases.txt', 'rt') as myfile:  # Open phrases.txt for reading the typing tests
        for line in myfile:                   # For each line of text,
            mylines.append(line)              # add that line to the list.

    # Converting lines of list to select a random phrase
    listLen = len(mylines) - 1 
    return (mylines[random.randint(0,listLen)])

def speedCalc():
    # words / time passed (assuming it is 5)
    start = time.time()
    test = input(print(generateTest()))
    end = time.time()
    timePassed = (end - start) 
    generateTestLen = len(generateTest())
    return ((generateTestLen/5)/timePassed)*60


print(speedCalc())