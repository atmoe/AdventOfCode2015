#!/usr/bin/python

import sys
import re
import itertools
import math

assert len(sys.argv) == 3, sys.argv[0] + " requires 2 arguments: filename and target!"

def combos(cList, target, length, combo, remainingBins):
    if len(combo) == length:
        if sum(combo) == target:
            cList.append(combo)
    else:
        for idx, b in enumerate(remainingBins):
            combos(cList, target, length, combo + [b], remainingBins[idx+1:])


def getCombos(target, bins):
    cList = []
    for i in range(len(bins)):
        combos(cList, target, i, [], bins)
    return cList


inputFile = open(sys.argv[1], "r")
target = int(sys.argv[2])

bins = []
for line in inputFile.readlines():
    m = re.search("^(\d+)$", line)
    bins.append(int(m.group(1)))

inputFile.close()

validCombos = getCombos(target, bins)

print "=== Part 1"
print "Combinations = {}".format(len(validCombos))
print

### Part 2 ###

minLen = len(bins)
for c in validCombos:
    if len(c) < minLen: minLen = len(c)

minCombos = 0
for c in validCombos:
    if len(c) == minLen: minCombos += 1


print "============="
print "=== Part 2"
print "Combinations = {}".format(minCombos)


