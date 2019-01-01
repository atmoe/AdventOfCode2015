#!/usr/bin/python

import sys
import re

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

strings = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    strings.append(line.strip())
inputFile.close()

naughtyCnt = 0
niceCnt    = 0
for s in strings:
    has3vowels       = False
    hasDoubleLetter  = False
    hasIllegalString = False

    # check for vowels
    m = re.search('(a|e|i|o|u).*(a|e|i|o|u).*(a|e|i|o|u)', s)
    if m:
        has3vowels = True

    # check for double letters
    for idx in range(len(s)-1):
        if s[idx] == s[idx+1]:
            hasDoubleLetter = True
            break

    # check for illegal strings
    m = re.search('(ab|cd|pq|xy)', s)
    if m:
        hasIllegalString = True

    if has3vowels and hasDoubleLetter and not hasIllegalString:
        niceCnt+=1
    else:
        naughtyCnt+=1

print "--- Part 1 ---"
print "Nice Strings    = {}".format(niceCnt)
print "Naughty Strings = {}".format(naughtyCnt)
print ""

naughtyCnt = 0
niceCnt    = 0
for s in strings:
    hasPair   = False
    hasRepeat = False

    # check for pairs
    for idx in range(len(s)-1):
        currSet = s[idx:idx+2]
        for idx2 in range(idx+2, len(s)-1):
            if currSet == s[idx2:idx2+2]:
                hasPair = True
                break

    # check for repeats
    for idx in range(len(s)-2):
        if s[idx] == s[idx+2]:
            hasRepeat = True
            break

    if hasPair and hasRepeat:
        niceCnt+=1
    else:
        naughtyCnt+=1
        
print "--- Part 2 ---"
print "Nice Strings    = {}".format(niceCnt)
print "Naughty Strings = {}".format(naughtyCnt)

