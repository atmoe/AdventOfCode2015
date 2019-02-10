#!/usr/bin/python

import sys
import re
import itertools


assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument: filename!"

inputFile = open(sys.argv[1], "r")

total = 0
for line in inputFile.readlines():
    m = re.findall("-?\d+", line)
    for n in m:
        total += int(n)

inputFile.close()

print "============="
print "=== Part 1"
print "Total = {}".format(total)

inputFile = open(sys.argv[1], "r")

total = 0

allRedObjs     = []
nonOverlapReds = []
uniqRedObjs    = []
for line in inputFile.readlines():
    # Find Reds
    for idx in range(len(line)):
        if idx < len(line)-5:
            if line[idx:idx+6] == ":\"red\"":

                # get start of obj
                objStart = idx
                numBrack = 1
                while numBrack != 0:
                    objStart-=1
                    if line[objStart] == "}": numBrack+=1
                    if line[objStart] == "{": numBrack-=1

                 # get end of obj
                objEnd = idx
                numBrack = 1
                while numBrack != 0:
                    objEnd+=1
                    if line[objEnd] == "}": numBrack-=1
                    if line[objEnd] == "{": numBrack+=1

                allRedObjs.append([objStart, objEnd])

    # find non overlapping reds
    for r in allRedObjs:
        contained = False
        for r2 in allRedObjs:
            if r[0] > r2[0] and r[1] < r2[1]:
                contained = True

        if not contained:
            nonOverlapReds.append(r)

    # find unique reds
    for r in nonOverlapReds:
        exists = False
        for r2 in uniqRedObjs:
            if r[0] == r2[0] and r[1] == r2[1]:
                exists = True

        if not exists: 
            uniqRedObjs.append(r)

    # remove unique reds
    newLine = line
    #print newLine
    for r in reversed(uniqRedObjs):
        #print "{} {}".format(r[0], r[1])
        newLine = newLine[:r[0]-1+1] + newLine[r[1]+1:]

    #print newLine

    # do same as above
    m = re.findall("-?\d+", newLine)
    for n in m:
        total += int(n)

    # sanity check
    charsRemoved = 0
    for r in uniqRedObjs:
        charsRemoved += (r[1] - r[0] + 1)
    #print "line len: {} new line len: {}  removed: {}  new+removed {}".format(len(line), len(newLine), charsRemoved, charsRemoved+len(newLine))

inputFile.close()


print "============="
print "=== Part 2"
print "Total = {}".format(total)


