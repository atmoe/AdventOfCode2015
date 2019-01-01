#!/usr/bin/python

import sys
import re

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getKey(self):
        return "{}_{}".format(self.x,self.y)
    
    def move(self, dir):
        if dir == "^": self.y -= 1
        if dir == "v": self.y += 1
        if dir == "<": self.x -= 1
        if dir == ">": self.x += 1

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

inputFile = open(sys.argv[1], "r")
directions = inputFile.readline()
inputFile.close()

currLoc = Location(0,0)
houses = {}
houses[currLoc.getKey()] = 1
for d in range(len(directions)):
    currLoc.move(directions[d])
    key = currLoc.getKey()

    if not key in houses.keys():
        houses[key] = 1
    else:
        houses[key] += 1

print "Num Houses Visited (Part 1) = {}".format(len(houses.keys()))

santaLoc = Location(0,0)
roboLoc  = Location(0,0)
houses = {}
houses[santaLoc.getKey()] = 1
for d in range(len(directions)):
    key = ""
    if d % 2 == 0:
        santaLoc.move(directions[d])
        key = santaLoc.getKey()
    else:
        roboLoc.move(directions[d])
        key = roboLoc.getKey()

    if not key in houses.keys():
        houses[key] = 1
    else:
        houses[key] += 1

print "Num Houses Visited (Part 2) = {}".format(len(houses.keys()))




