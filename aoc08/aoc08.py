#!/usr/bin/python

import sys
import re

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"


inputFile = open(sys.argv[1], "r")
lines = inputFile.readlines()
inputFile.close()

totalCodeChars = 0
totalMemChars = 0
for line in lines:
    codeLine = line.strip()

    codeChars = len(codeLine)
    

    assert codeLine[0]=="\"", "line does not start with quote!"
    assert codeLine[-1]=="\"", "line does not endwith quote!"

    memChars = 0
    codeLineIter = iter(codeLine)
    for c in codeLineIter:
        if c == "\"":
            # start or end quote, continue on            
            continue
        elif c == "\\":
            nextChar = next(codeLineIter)
            if nextChar == "x":
                next(codeLineIter)
                next(codeLineIter)

        memChars+=1

    totalCodeChars += codeChars
    totalMemChars += memChars

print "============="
print "=== Part 1"
print "Code Characters   = {}".format(totalCodeChars)
print "Memory Characters = {}".format(totalMemChars)
print "Difference        = {}".format(totalCodeChars-totalMemChars)

### Start Part 2 ###
newTotalMemChars  = totalCodeChars
newTotalCodeChars = 0 
for line in lines:
    memLine = line.strip()

    codeChars = 2 # account for new leading/trailing "
    for c in memLine:
        if   c == "\"": codeChars+= 2
        elif c == "\\": codeChars += 2
        else:           codeChars += 1

    newTotalCodeChars += codeChars


print "============="
print "=== Part 2"
print "Memory Characters = {}".format(newTotalMemChars)
print "Code Characters   = {}".format(newTotalCodeChars)
print "Difference        = {}".format(newTotalCodeChars - newTotalMemChars)





