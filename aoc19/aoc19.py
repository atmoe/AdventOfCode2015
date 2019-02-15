#!/usr/bin/python

import sys
import re
import copy

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

def getNewMolecules(m, repl):
    newMoleculeDict = {}
    for r in repl:
        for idx in range(len(m)):
            if m[idx:idx+len(r[0])] == r[0]:
                newM = m[0:idx] + r[1] + m[idx+len(r[0]):]
                newMoleculeDict[newM] = 1
    return newMoleculeDict.keys()


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

'''
lastMolecules = ["e"]

moleculeFound = False
steps = 0
while not moleculeFound:
    print "--- Step {} = {}".format(steps, len(lastMolecules))
    #for m in lastMolecules:
    #    print m

    assert len(lastMolecules) != 0, "ran out of molecules!"

    nextMolecules = {}
    for m in lastMolecules:
        for mNew in getNewMolecules(m,replacements):
            if len(mNew) < len(molecule):
                nextMolecules[mNew] = True
            elif len(mNew) == len(molecule):
                moleculeFound = (mNew == molecule) or moleculeFound

    lastMolecules = nextMolecules.keys()

    steps += 1
'''

numMatches = 0
for idx,r1 in enumerate(replacements):
    for r2 in replacements[0:idx]+replacements[idx+1:]:
        if re.search(r2[1],r1[1]):
            numMatches+=1
            print "match:"
            print r1
            print r2
assert numMatches == 0, "part 2 only works if reverse mappings are unique"

print "============="
print "=== Part 2"
print "Num Steps = {}".format(0)





