#!/usr/bin/python

import sys
import re
import copy
import random 

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

dbgEn = True
def dbgPrint(text):
    if dbgEn:
        print(text)

inputFile = open(sys.argv[1], "r")
values = []
for line in inputFile.readlines():
    regex = re.match("(.*)", line)
    values.append(int(regex.group(0)))
inputFile.close()
values.sort(reverse=True)
print(values)

def getGroup1(grp1, remVals, idx, target, g1, g2):
    newGrp = list(grp1)
    newGrp.append(remVals[idx])
    if sum(newGrp) == target:
        for v in newGrp:
            g1.append(v)
        for v in remVals:
            if v not in g1:
                g2.append(v)
        return True
    elif idx + 1 >= len(remVals):
        return False
    else:
        return getGroup1(newGrp, remVals, idx+1, target, g1, g2) or getGroup1(grp1, remVals, idx+1, target, g1, g2)


def getGroup0(gList, myGrp, remVals, idx, maxSize):
    # construct this potential group, push to stack of groups
    newGrp = list(myGrp)
    newRemVals = list(remVals)
    newGrp.append(values[idx])
    newRemVals.remove(values[idx])

    if len(newGrp) > maxSize[0]:
        return

    grp1 = []
    grp2 = []
    if sum(newGrp)*2 == sum(newRemVals) and  getGroup1([], newRemVals, 0, sum(newGrp), grp1, grp2):
        maxSize[0] = len(newGrp)

        #print(f'{newGrp} (QE = {qe})   {grp1}    {grp2}')
        gList.append(newGrp)

    # recurse with one larger, next index (if index in range)
    elif idx + 1 < len(values):
        getGroup0(gList, newGrp, newRemVals, idx+1, maxSize)
    
    # recurse with same size, next index (if index in range)
    if idx + 1 < len(values):
        getGroup0(gList, myGrp, remVals, idx+1, maxSize)

def getQE(group):
    qe = 1
    for v in group:
        qe *= v
    return qe


print("==============")
print("=== Part 1 ===")
print("==============")
doPart1 = False
if doPart1:
    groups = []
    initialGroup = []
    remainingVals = list(values)
    maxSize = [len(values)]
    getGroup0(groups, initialGroup, remainingVals, 0, maxSize) 
        
    minQE = getQE(groups[0])
    for g in groups:
        if len(g) == maxSize[0]:
            if getQE(g) < minQE:
                minQE = getQE(g)
    print(f'Min QE = {minQE}')
    
print("==============")
print("=== Part 2 ===")
print("==============")
doPart2 = True

def getGroup2_P2(grp2, remVals, idx, target):
    newGrp = list(grp2)
    newGrp.append(remVals[idx])
    if sum(newGrp) == target:
        return True
    elif idx + 1 >= len(remVals):
        return False
    else:
        return getGroup2_P2(newGrp, remVals, idx+1, target) or getGroup2_P2(grp2, remVals, idx+1, target)


def getGroup1_P2(grp1, remVals, idx, target):
    newGrp = list(grp1)
    newGrp.append(remVals[idx])
    if sum(newGrp) == target:
        grp2 = []
        newRemVals = list(remVals)
        for v in newGrp:
            remVals.remove(v)
        return getGroup2_P2(grp2, newRemVals, 0, target)
    elif idx + 1 >= len(remVals):
        return False
    else:
        return getGroup1_P2(newGrp, remVals, idx+1, target) or getGroup1_P2(grp1, remVals, idx+1, target)


def getGroup0_P2(gList, myGrp, remVals, idx, maxSize):
    # construct this potential group, push to stack of groups
    newGrp = list(myGrp)
    newRemVals = list(remVals)
    newGrp.append(values[idx])
    newRemVals.remove(values[idx])

    if len(newGrp) > maxSize[0]:
        return

    grp1 = []
    grp2 = []
    grp3 = []
    if sum(newGrp)*3 == sum(newRemVals) and getGroup1_P2([], newRemVals, 0, sum(newGrp)):
        maxSize[0] = len(newGrp)
        gList.append(newGrp)

    # recurse with one larger, next index (if index in range)
    elif idx + 1 < len(values):
        getGroup0_P2(gList, newGrp, newRemVals, idx+1, maxSize)
    
    # recurse with same size, next index (if index in range)
    if idx + 1 < len(values):
        getGroup0_P2(gList, myGrp, remVals, idx+1, maxSize)



if doPart2:
    groups = []
    initialGroup = []
    remainingVals = list(values)
    maxSize = [len(values)]
    getGroup0_P2(groups, initialGroup, remainingVals, 0, maxSize) 
        
    minQE = getQE(groups[0])
    for g in groups:
        print(g)
        if len(g) == maxSize[0]:
            if getQE(g) < minQE:
                minQE = getQE(g)
    print(f'Min QE = {minQE}')
 
