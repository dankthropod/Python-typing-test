#!/usr/bin/env python

import time
import random
import string
import sys
import string
import sys

#from getkey import getkey

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

    return generateTest(), timePassed, ((generateTestLen/5)/timePassed)*60

def spellCheck():
    test, timePassed, wpm = speedCalc()
    diff = 0
    correctChars = 0

    file_A = generateTest()
    file_B = test

    #read_A=open(file_A,'r').read()
    #read_B=open(file_B,'r').read()

    for char_a, char_b in zip(file_A, file_B):
        if char_a == char_b:
            correctChars = correctChars+1
    file_A_len = len(file_A)

    correctPercent = (correctChars/file_A_len)*100

    errors = file_A_len - correctChars
    errorRate = errors/timePassed

    netWPM = wpm - errorRate

    return correctPercent, errors, netWPM

correctPercent, errors, netWPM = spellCheck()
print(correctPercent)
print(errors)
print(netWPM)