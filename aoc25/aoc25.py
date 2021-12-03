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


#inputFile = open(sys.argv[1], "r")
#program = []
#for line in inputFile.readlines():
    #instrRe = re.match("(\w*) *(.*)", line)
#    program.append(Instruction(instr, args))

#inputFile.close()

def getIdx(x, y):
    x = x - 1
    y = y - 1

    offset = 0

    # get offset in y direction first
    for i in range(0,y):
        offset += (i+1)

    print(f'y = {offset}')

    # add in offset in x-direction
    start_x_incr = y+2
    for i in range(0,x):
        offset += start_x_incr + i

    print(f'x,y = {offset}')

    return offset

def getCode(exponent):
    p1 = 252533
    p2 = 33554393

    factors = [p1 % p2]
    factor = 1
    expTerm = exponent >> 1
    while expTerm > 0:
        factors.append((factors[factor-1]*factors[factor-1]) % p2)
        factor += 1
        expTerm = expTerm >> 1
    
    value = 1
    expTerm = exponent
    factor = 0
    while expTerm > 0:
        if expTerm % 2 == 1:
            value *= factors[factor]

        factor+=1
        expTerm = expTerm >> 1

    value = value % p2

    return (value * 20151125) % p2

print("==============")
print("=== Part 1 ===")
print("==============")
doPart1 = True
if doPart1:
    idx = getIdx(3019,3010)

    code = getCode(idx)

    print(f'code = {code}')

    quit()
        
    
print("==============")
print("=== Part 2 ===")
print("==============")
doPart2 = True
if doPart2:
    quit()
 
