#!/usr/bin/python

import sys
import re
import itertools
import math

def permute(pList, prefixNames, remainingNames):
    if prefixNames is None: prefixNames = []
    if len(remainingNames) == 0:
        pList.append(prefixNames)
    else:
        for i in range(len(remainingNames)):
            permute(pList, prefixNames + [remainingNames[i]], remainingNames[0:i] + remainingNames[i+1:])


def getPermutations(names):
    permutations = []
    permute(permutations, None, names)
    return permutations


assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument: filename!"

inputFile = open(sys.argv[1], "r")

relations = {}
for line in inputFile.readlines():
    m = re.match("^(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)\.$", line)
    #print m.groups()

    person   = m.group(1)
    relation = m.group(4)
    amount   = int(m.group(3))
    if m.group(2) == "lose":
        amount *= -1

    if person not in relations: relations[person] = {}
    relations[person][relation] = amount

inputFile.close()


trials = getPermutations(relations.keys())
print "combos = {}".format(math.factorial(len(relations.keys())))
print "combos = {}".format(len(trials))

maxSum = 0
for people in trials:
    currSum = 0
    for idx, p in enumerate(people):
        n1 = people[(idx+1) % len(people)]
        n2 = people[idx-1]
        currSum += relations[p][n1] + relations[p][n2]

    if currSum > maxSum: maxSum = currSum


print "============="
print "=== Part 1"
print "Max Happiness = {}".format(maxSum)


### Part 2 ###

relations["me"] = {}
for k in relations.keys():
    relations["me"][k] = 0
    relations[k]["me"] = 0

trials = getPermutations(relations.keys())
print "combos = {}".format(math.factorial(len(relations.keys())))
print "combos = {}".format(len(trials))

maxSum = 0
for people in trials:
    currSum = 0
    for idx, p in enumerate(people):
        n1 = people[(idx+1) % len(people)]
        n2 = people[idx-1]
        currSum += relations[p][n1] + relations[p][n2]

    if currSum > maxSum: maxSum = currSum

print "============="
print "=== Part 2"
print "Max Happiness = {}".format(maxSum)


