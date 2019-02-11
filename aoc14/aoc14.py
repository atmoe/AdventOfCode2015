#!/usr/bin/python

import sys
import re
import itertools
import math

class Reindeer:
    def __init__(self, name, speed, flyTime, restTime):
        self.name     = name
        self.speed    = speed
        self.flyTime  = flyTime
        self.restTime = restTime

        self.flying = True
        self.remaining = flyTime

        self.position = 0
        self.points = 0

    def update(self):
        self.remaining -= 1

        if self.flying:
            self.position += self.speed

        if self.remaining == 0:
            if self.flying:
                self.flying = False
                self.remaining = self.restTime 
            else:
                self.flying = True
                self.remaining = self.flyTime

    def printPos(self):
        print "{}\t@{}\tpts={}".format(self.name, self.position, self.points)


assert len(sys.argv) == 3, sys.argv[0] + " requires 2 arguments: filename and seconds!"

inputFile = open(sys.argv[1], "r")
seconds = int(sys.argv[2])

reindeer = []
for line in inputFile.readlines():
    m = re.match("^(\w+) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds\.$", line)
    #print m.groups()

    name  = m.group(1)
    speed = int(m.group(2))
    fly   = int(m.group(3))
    rest  = int(m.group(4))

    reindeer.append(Reindeer(name, speed, fly, rest))

inputFile.close()


for r in reindeer:
    r.printPos()

for i in range(1,seconds + 1):
    print "--------------"
    print "--- Time {}".format(i)
    print "--------------"
    for r in reindeer: r.update()

    maxDist = 0 
    for r in reindeer:
        if r.position > maxDist: maxDist = r.position
    for r in reindeer:
        if r.position == maxDist: r.points+=1

    for r in reindeer: r.printPos()

maxDist   = 0
maxPoints = 0
for r in reindeer:
    if r.position > maxDist:   maxDist   = r.position
    if r.points   > maxPoints: maxPoints = r.points

print "============="
print "=== Part 1"
print "Max Distance = {}".format(maxDist)


print "============="
print "=== Part 2"
print "Max Points = {}".format(maxPoints)


