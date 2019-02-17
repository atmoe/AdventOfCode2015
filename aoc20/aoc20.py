#!/usr/bin/python

import sys
import re
import copy
import random
import math

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

target = int(sys.argv[1])

doPart1 = False
if doPart1:
    house = 0
    houseFound = False
    while not houseFound:
        house += 1

        amount = 0
        for i in range(1,int(math.floor(math.sqrt(house))+1)):
            if house % i == 0:
                amount += i*10
                if house/i != i:
                    amount += (house/i)*10

        #if house % 100 == 0:
        #    print "House {} = {}".format(house, amount)
        houseFound = amount >= target

    print "============="
    print "=== Part 1"
    print "House Num = {}".format(house)
    print "============="

### Part 2 #######
house = 0
houseFound = False
while not houseFound:
    house += 1

    amount = 0
    for i in range(1,int(math.floor(math.sqrt(house))+1)):
        if house % i == 0:
            elf1 = i
            elf2 = house/i

            if house <= 50*elf1:
                amount += elf1*11

            if elf1 != elf2 and house <= 50*elf2:
                amount += elf2*11

    if house % 100 == 0:
        print "House {} = {}".format(house, amount)
    houseFound = amount >= target

print "============="
print "=== Part 2"
print "House Num = {}".format(house)
print "============="

