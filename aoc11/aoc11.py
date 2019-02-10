#!/usr/bin/python

import sys
import re
import itertools

def incrPwd(pwd):
    newPwd = ""

    lastOverflow = True
    for c in pwd[::-1]:
        if lastOverflow:
            lastOverflow = False
            cIncr = chr(ord(c)+1)
            if c == "z":
                cIncr = "a"
                lastOverflow = True

            newPwd = cIncr + newPwd
        else:
            newPwd = c + newPwd

    return newPwd

def hasStraight(pwd):
    for idx in range(len(pwd)-2):
        c1 = chr(ord(pwd[idx])+1)
        c2 = chr(ord(pwd[idx])+2)
        if pwd[idx+1] == c1 and pwd[idx+2] == c2:
            return True

    return False

def hasAllValidLetters(pwd):
    for c in pwd:
        if c == "i" or c == "l" or c == "o":
            return False
    return True

def hasTwoDoubles(pwd):
    numDoubles = 0
    lastWasDouble = False
    for idx in range(len(pwd)-1):
        if pwd[idx] == pwd[idx+1] and not lastWasDouble:
            numDoubles += 1
            lastWasDouble = True
        else:
            lastWasDouble = False
    return numDoubles >= 2


assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument: string!"


pwdMeetsCriteria = False
currPwd = sys.argv[1]

incrPwd(currPwd)
while not pwdMeetsCriteria:
#for i in range(5):
    currPwd = incrPwd(currPwd)
    #print "{}: {} {} {}".format(currPwd, hasStraight(currPwd), hasTwoDoubles(currPwd), hasAllValidLetters(currPwd))
    pwdMeetsCriteria = hasStraight(currPwd) and hasTwoDoubles(currPwd) and hasAllValidLetters(currPwd)

print "============="
print "=== Part 1"
print "Password = {}".format(currPwd)

print "============="
print "=== Part 2"




