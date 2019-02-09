#!/usr/bin/python

import sys
import re
import itertools


assert len(sys.argv) == 3, sys.argv[0] + " requires 2 arguments: string and iterations!"


inputStr   = sys.argv[1]
iterations = int(sys.argv[2])

currStr = inputStr
for i in range(iterations):
    curNum = currStr[0]
    numNum = 0
    newStr = ""
    for c in currStr:
        if c == curNum:
            numNum+=1
            continue
        else:
            newStr += str(numNum) + curNum
            numNum = 1
            curNum = c

    newStr += str(numNum) + curNum

    #print "iteration {}: {}".format(i, newStr)

    currStr = newStr

print "============="
print "=== Part 1"
print "Length = {}".format(len(currStr))

print "============="
print "=== Part 2"




