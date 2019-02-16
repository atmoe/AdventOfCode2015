#!/usr/bin/python

import sys
import re
import copy
import random 

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

def getNewMolecules(m, repl):
    newMoleculeDict = {}
    for r in repl:
        for idx in range(len(m)):
            if m[idx:idx+len(r[0])] == r[0]:
                newM = m[0:idx] + r[1] + m[idx+len(r[0]):]
                newMoleculeDict[newM] = 1
    return newMoleculeDict.keys()

def getNewMoleculesRev(m, repl):
    newMoleculeDict = {}
    for r in repl:
        for idx in range(len(m)):
            if m[idx:idx+len(r[1])] == r[1]:
                newM = m[0:idx] + r[0] + m[idx+len(r[1]):]
                newMoleculeDict[newM] = 1
    return newMoleculeDict.keys()


def decompose(decomps, currMole, currSteps, repl, idxStack):
    print idxStack
    if currMole == "e":
        decomps.append(currSteps)
    else:
        for r in repl:
            for idx in range(len(currMole)):
                if currMole[idx:idx+len(r[1])] == r[1]:
                    decompose(decomps, currMole[0:idx] + r[0] + currMole[idx+len(r[1]):], currSteps+1, repl, idxStack + [idx])

def decomposeSteps(m, repl):
    decompositions = []

    decompose(decompositions, m, 0, repl, [])

    return min(decompositions)


replacements = []
molecule = ""

gatherReplacements = True

inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    if gatherReplacements:
        m = re.match("^(\w+) => (\w+)$", line)
        if m:
            replacements.append((m.group(1), m.group(2)))
        else:
            gatherReplacements = False
    else:
        molecule = line.strip()
inputFile.close()

#for r in replacements:
#    print r

newMolecules = getNewMolecules(molecule, replacements)

print "============="
print "=== Part 1"
print "=== Num Molecules = {}".format(len(newMolecules))
print "============="

#### Part 2 ###

#steps = decomposeSteps(molecule, replacements)

moleculeFound = False
attempt = 1
steps = 0
currMole = molecule
while not moleculeFound:
    lastMole = currMole

    for r in replacements:
        if r[1] in currMole:
            #print currMole,
            #print "->",
            currMole = currMole.replace(r[1], r[0], 1)
            #print currMole
            steps += 1

    if lastMole == currMole:
        print "Attempt = {}  (ended with: {})".format(attempt, currMole)
        currMole = molecule
        random.shuffle(replacements)
        steps = 0
        attempt+=1

    if currMole == "e":
        moleculeFound = True


print "============="
print "=== Part 2"
print "Num Steps = {}".format(steps)





