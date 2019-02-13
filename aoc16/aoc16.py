#!/usr/bin/python

import sys
import re
import itertools
import math

class AuntSue:
    def __init__(self, num):
        self.num        = num
        self.children   = -1
        self.cats       = -1
        self.samoyeds   = -1
        self.pomeranians= -1
        self.akitas     = -1
        self.vizslas    = -1
        self.goldfish   = -1
        self.trees      = -1
        self.cars       = -1
        self.perfumes   = -1

    def printSelf(self):
        print "Sue {}".format(self.num),
        print self.children, self.cats, self.samoyeds, self.pomeranians, self.akitas, self.vizslas, self.goldfish, self.trees, self.cars, self.perfumes



assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument: filename!"


inputFile = open(sys.argv[1], "r")

aunts = []
for line in inputFile.readlines():
    numRe         = re.search("^Sue (\d+):", line)
    childrenRe    = re.search("children: (\d+)", line)
    catsRe        = re.search("cats: (\d+)", line)
    samoyedsRe    = re.search("samoyeds: (\d+)", line)
    pomeraniansRe = re.search("pomeranians: (\d+)", line)
    akitasRe      = re.search("akitas: (\d+)", line)
    vizslasRe     = re.search("vizslas: (\d+)", line)
    goldfishRe    = re.search("goldfish: (\d+)", line)
    treesRe       = re.search("trees: (\d+)", line)
    carsRe        = re.search("cars: (\d+)", line)
    perfumesRe    = re.search("perfumes: (\d+)", line)

    aunt = AuntSue(int(numRe.group(1)))

    if childrenRe:    aunt.children    = int(childrenRe.group(1))
    if catsRe:        aunt.cats        = int(catsRe.group(1))
    if samoyedsRe:    aunt.samoyeds    = int(samoyedsRe.group(1))
    if pomeraniansRe: aunt.pomeranians = int(pomeraniansRe.group(1))
    if akitasRe:      aunt.akitas      = int(akitasRe.group(1))
    if vizslasRe:     aunt.vizslas     = int(vizslasRe.group(1))
    if goldfishRe:    aunt.goldfish    = int(goldfishRe.group(1))
    if treesRe:       aunt.trees       = int(treesRe.group(1))
    if carsRe:        aunt.cars        = int(carsRe.group(1))
    if perfumesRe:    aunt.perfumes    = int(perfumesRe.group(1))

    aunts.append(aunt)

inputFile.close()

targChildren    = 3
targCats        = 7
targSamoyeds    = 2
targPomeranians = 3
targAkitas      = 0
targVizslas     = 0
targGoldfish    = 5
targTrees       = 3
targCars        = 2
targPerfumes    = 1

potentialAunts = []
for a in aunts:
    potential = True
    if a.children    >= 0 and a.children    != targChildren:    potential = False
    if a.cats        >= 0 and a.cats        != targCats:        potential = False
    if a.samoyeds    >= 0 and a.samoyeds    != targSamoyeds:    potential = False
    if a.pomeranians >= 0 and a.pomeranians != targPomeranians: potential = False
    if a.akitas      >= 0 and a.akitas      != targAkitas:      potential = False
    if a.vizslas     >= 0 and a.vizslas     != targVizslas:     potential = False
    if a.goldfish    >= 0 and a.goldfish    != targGoldfish:    potential = False
    if a.trees       >= 0 and a.trees       != targTrees:       potential = False
    if a.cars        >= 0 and a.cars        != targCars:        potential = False
    if a.perfumes    >= 0 and a.perfumes    != targPerfumes:    potential = False

    if potential: potentialAunts.append(a)

assert len(potentialAunts) == 1, "{} aunts found!".format(len(potentialAunts))

print "============="
print "=== Part 1"
print "Aunt Sue = {}".format(potentialAunts[0].num)
print


potentialAunts = []
for a in aunts:
    potential = True
    if a.children    >= 0 and a.children    != targChildren:    potential = False
    if a.cats        >= 0 and a.cats        <= targCats:        potential = False
    if a.samoyeds    >= 0 and a.samoyeds    != targSamoyeds:    potential = False
    if a.pomeranians >= 0 and a.pomeranians >= targPomeranians: potential = False
    if a.akitas      >= 0 and a.akitas      != targAkitas:      potential = False
    if a.vizslas     >= 0 and a.vizslas     != targVizslas:     potential = False
    if a.goldfish    >= 0 and a.goldfish    >= targGoldfish:    potential = False
    if a.trees       >= 0 and a.trees       <= targTrees:       potential = False
    if a.cars        >= 0 and a.cars        != targCars:        potential = False
    if a.perfumes    >= 0 and a.perfumes    != targPerfumes:    potential = False

    if potential: potentialAunts.append(a)

assert len(potentialAunts) == 1, "{} aunts found!".format(len(potentialAunts))

print "============="
print "=== Part 2"
print "Aunt Sue = {}".format(potentialAunts[0].num)


