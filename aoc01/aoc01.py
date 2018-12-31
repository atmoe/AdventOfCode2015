#!/usr/bin/python

import sys;

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

inputFile = open(sys.argv[1], "r")
line = inputFile.readline()
inputFile.close()

floor=0
firstBasementChar = -1
for i in range(len(line)):
    if line[i] == "(": floor += 1
    if line[i] == ")": floor -= 1

    if floor == -1 and firstBasementChar < 0:
        firstBasementChar = i + 1

print "first basement character = {}".format(firstBasementChar)
print "final floor = {}".format(floor)

