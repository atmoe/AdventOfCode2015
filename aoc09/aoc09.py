#!/usr/bin/python

import sys
import re
import itertools


assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"


distances = {}
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    m = re.search("^(\w+) to (\w+) = (\d+)", line)
    assert m, "invalid input line = {}".format(line)

    loc1 = m.group(1)
    loc2 = m.group(2)
    dist = int(m.group(3))

    if not loc1 in distances.keys(): distances[loc1] = {}
    distances[loc1][loc2] = dist

    if not loc2 in distances.keys(): distances[loc2] = {}
    distances[loc2][loc1] = dist
inputFile.close()

for d1 in distances.keys():
    for d2 in distances[d1].keys():
        print "{} -> {} = {}".format(d1, d2, distances[d1][d2])


minDist = 100000000000
maxDist = 0
for p in itertools.permutations(distances.keys()):

    pDist = 0
    for idx in range(len(p)-1):
        loc1 = p[idx]
        loc2 = p[idx+1]
        pDist += distances[loc1][loc2]

    if pDist < minDist: minDist = pDist
    if pDist > maxDist: maxDist = pDist

print "============="
print "=== Part 1"
print "Minimum Distance = {}".format(minDist)
print "============="
print "=== Part 2"
print "Maximum Distance = {}".format(maxDist)




