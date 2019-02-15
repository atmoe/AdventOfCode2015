#!/usr/bin/python

import sys
import re
import copy

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

grid = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    numRow = []
    for c in list(line.strip()):
        if c == "#": numRow.append(1)
        if c == ".": numRow.append(0)

    grid.append(numRow)
inputFile.close()

for r in grid:
    print r

print

height = len(grid)
width  = len(grid[0])

lastGrid = copy.deepcopy(grid)
nextGrid = []
iterations = 100
for i in range(iterations):
    for y,row in enumerate(grid):
        nextGrid.append([])
        for x,light in enumerate(row):
            litNeighbors = 0

            minX = max(0, x-1)
            maxX = min(width-1,  x+1)

            if y-1 >= 0:
                litNeighbors += sum(lastGrid[y-1][minX:maxX+1])

            litNeighbors += sum(lastGrid[y][minX:maxX+1]) - lastGrid[y][x]

            if y+1 < height:
                litNeighbors += sum(lastGrid[y+1][minX:maxX+1])

            if lastGrid[y][x] == 1:
                if litNeighbors == 2 or litNeighbors == 3:
                    nextGrid[y].append(1)
                else:
                    nextGrid[y].append(0)
            else:
                if litNeighbors == 3:
                    nextGrid[y].append(1)
                else:
                    nextGrid[y].append(0)

    lastGrid = nextGrid
    nextGrid = []


numLights = 0
for r in lastGrid:
    numLights+=sum(r)

print "============="
print "=== Part 1"
print "Num Lights = {}".format(numLights)

#### Part 2 ###
lastGrid = copy.deepcopy(grid)
nextGrid = []


lastGrid[0][0] = 1
lastGrid[height-1][0] = 1
lastGrid[0][width-1] = 1
lastGrid[height-1][width-1] = 1

for i in range(iterations):
    for y,row in enumerate(grid):
        nextGrid.append([])
        for x,light in enumerate(row):
            litNeighbors = 0

            minX = max(0, x-1)
            maxX = min(width-1,  x+1)

            if y-1 >= 0:
                litNeighbors += sum(lastGrid[y-1][minX:maxX+1])

            litNeighbors += sum(lastGrid[y][minX:maxX+1]) - lastGrid[y][x]

            if y+1 < height:
                litNeighbors += sum(lastGrid[y+1][minX:maxX+1])

            if lastGrid[y][x] == 1:
                if litNeighbors == 2 or litNeighbors == 3:
                    nextGrid[y].append(1)
                else:
                    nextGrid[y].append(0)
            else:
                if litNeighbors == 3:
                    nextGrid[y].append(1)
                else:
                    nextGrid[y].append(0)

    nextGrid[0][0] = 1
    nextGrid[height-1][0] = 1
    nextGrid[0][width-1] = 1
    nextGrid[height-1][width-1] = 1

    lastGrid = nextGrid
    nextGrid = []

numLights = 0
for r in lastGrid:
    numLights+=sum(r)

print "============="
print "=== Part 2"
print "Best Score = {}".format(numLights)





