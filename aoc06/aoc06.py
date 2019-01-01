#!/usr/bin/python

import sys
import re

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Inst:
    def __init__ (self, inst, startLoc, endLoc):
        self.inst  = inst
        self.start = startLoc
        self.end   = endLoc

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

instructions = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    m = re.search("^(turn on|toggle|turn off) (\d+),(\d+) through (\d+),(\d+)", line)
    assert m, "invalid line = {}".format(line)

    inst = m.group(1)
    startLoc = Location(int(m.group(2)), int(m.group(3)))
    endLoc   = Location(int(m.group(4)), int(m.group(5)))
    instructions.append(Inst(inst,startLoc,endLoc))
inputFile.close()

grid = [[False for x in range(1000)] for y in range(1000)]
for i in instructions:
    for y in range(i.start.y, i.end.y+1):
        for x in range(i.start.x, i.end.x+1):
            if   i.inst == "turn on":  grid[y][x] = True
            elif i.inst == "turn off": grid[y][x] = False
            elif i.inst == "toggle" and grid[y][x] == False: grid[y][x] = True
            elif i.inst == "toggle" and grid[y][x] == True:  grid[y][x] = False
            else: assert 0

litLights = 0
for y in range(1000):
    for x in range(1000):
        if grid[y][x] == True: litLights+=1

print "==== Part 1 ====="
print "Lit Lights = {}".format(litLights)

grid = [[0 for x in range(1000)] for y in range(1000)]
for i in instructions:
    for y in range(i.start.y, i.end.y+1):
        for x in range(i.start.x, i.end.x+1):
            if   i.inst == "turn on":  grid[y][x] += 1 
            elif i.inst == "turn off": grid[y][x] -= 1
            elif i.inst == "toggle":   grid[y][x] += 2 
            else: assert 0

            if grid[y][x] < 0: grid[y][x]=0

totalBrightness = 0
for y in range(1000):
    for x in range(1000):
        totalBrightness += grid[y][x]

print "==== Part 2 ====="
print "Total Brightness = {}".format(totalBrightness)



