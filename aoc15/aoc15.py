#!/usr/bin/python

import sys
import re
import itertools
import math

class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name       = name
        self.capacity   = capacity
        self.durability = durability
        self.flavor     = flavor
        self.texture    = texture
        self.calories   = calories

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument: filename!"


def mixtures(mixList, ingredientNum, amtRemaining, amountList, numIngredients):
    if ingredientNum == (numIngredients-1):
        mixList.append(amountList + [amtRemaining])
    else:
        for i in range(amtRemaining+1):
            mixtures(mixList, ingredientNum+1, amtRemaining-i, amountList + [i], numIngredients)


def getMixtures(numIngredients):
    mixList = []
    mixtures(mixList, 0, 100, [], numIngredients)
    return mixList


inputFile = open(sys.argv[1], "r")

ingredients = []
for line in inputFile.readlines():
    m = re.match("^(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)$", line)
    print m.groups()

    name = m.group(1)
    cap  = int(m.group(2))
    dur  = int(m.group(3))
    flav = int(m.group(4))
    text = int(m.group(5))
    cal  = int(m.group(6))

    ingredients.append(Ingredient(name, cap, dur, flav, text, cal))

inputFile.close()

mixtures = getMixtures(len(ingredients))

maxTotalP1 = 0
maxTotalP2 = 0
for m in mixtures:
    cCapacity   = 0
    cDurability = 0
    cFlavor     = 0
    cTexture    = 0
    cCalories   = 0
    for idx, amt in enumerate(m):
        cCapacity   += ingredients[idx].capacity   * amt
        cDurability += ingredients[idx].durability * amt
        cFlavor     += ingredients[idx].flavor     * amt
        cTexture    += ingredients[idx].texture    * amt
        cCalories   += ingredients[idx].calories   * amt

    if cCapacity   < 0: cCapacity   = 0
    if cDurability < 0: cDurability = 0
    if cFlavor     < 0: cFlavor     = 0
    if cTexture    < 0: cTexture    = 0

    cTotal = cCapacity * cDurability * cFlavor * cTexture

    # part 1
    if cTotal > maxTotalP1:
        maxTotalP1 = cTotal

    # part 2
    if cTotal > maxTotalP2 and cCalories == 500:
        maxTotalP2 = cTotal

print "============="
print "=== Part 1"
print "Best Score = {}".format(maxTotalP1)


print "============="
print "=== Part 2"
print "Best Score = {}".format(maxTotalP2)


