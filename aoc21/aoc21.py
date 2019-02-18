#!/usr/bin/python

import sys
import re
import copy
import random 

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

class Player:
    def __init__(self, damage, armor, cost):
        self.damage = damage
        self.armor  = armor
        self.hp     = 100
        self.cost   = cost

    def printMe(self):
        print "{}: {} {} {}".format(self.cost, self.damage, self.armor, self.hp)

    def isDead(self):
        return self.hp <= 0

    def attacked(self, damage):
        self.hp -= max(1, (damage - self.armor))
        #print "The boss deals {}-{} = damage, player at {} hp".format(damage, self.armor, self.hp)

class Boss:
    def __init__(self, hp, damage, armor):
        self.damage = damage
        self.armor  = armor
        self.hp     = hp

    def printMe(self):
        print "boss: {} {} {}".format(self.damage, self.armor, self.hp)

    def isDead(self):
        return self.hp <= 0

    def attacked(self, damage):
        self.hp -= max(1, (damage - self.armor))
        #print "The player deals {}-{} = damage, boss at {} hp".format(damage, self.armor, self.hp)

inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    hp = re.match("^Hit Points: (\d+)", line)
    d  = re.match("^Damage: (\d+)", line)
    a  = re.match("^Armor: (\d+)", line)
    if hp: bossHP     = int(hp.group(1))
    if d:  bossDamage = int(d.group(1))
    if a:  bossArmor  = int(a.group(1))
inputFile.close()



# gold, damage
weapons = {}
weapons["Dagger"]     = ( 8, 4)
weapons["Shortsword"] = (10, 5)
weapons["Warhammer"]  = (25, 6)
weapons["Longsword"]  = (40, 7)
weapons["Greataxe"]   = (74, 8)

# gold, armor
armor = {}
armor["None"]       = (  0, 0)
armor["Leather"]    = ( 13, 1)
armor["Chainmail "] = ( 31, 2)
armor["Splintmail"] = ( 53, 3)
armor["Bandedmail"] = ( 75, 4)
armor["Platemail"]  = (102, 5)

# gold, damage, armor
rings = {}
rings["Damage 1"]  = ( 25, 1, 0)
rings["Damage 2"]  = ( 50, 2, 0)
rings["Damage 3"]  = (100, 3, 0)
rings["Defense 1"] = ( 20, 0, 1)
rings["Defense 2"] = ( 40, 0, 2)
rings["Defense 3"] = ( 80, 0, 3)

# generate all player combos
players = []

for w in weapons.keys():
    for a in armor.keys():
        # no rings
        dVal1 = weapons[w][1]
        aVal1 = armor[a][1]
        cost1 = weapons[w][0] + armor[a][0]
        players.append(Player(dVal1, aVal1, cost1))
        #print "{}: {} {}".format(cost1, w, a)

        # 1 ring
        ringList = rings.keys()
        for idx,r in enumerate(ringList):
            dVal2 = dVal1 + rings[r][1]
            aVal2 = aVal1 + rings[r][2]
            cost2 = cost1 + rings[r][0]
            players.append(Player(dVal2, aVal2, cost2))
            #print "{}: {} {} {}".format(cost2, w, a, r)

            # 2 rings
            for r2 in ringList[idx+1:]:
                dVal3 = dVal2 + rings[r2][1]
                aVal3 = aVal2 + rings[r2][2]
                cost3 = cost2 + rings[r2][0]
                players.append(Player(dVal3, aVal3, cost3))
                #print "{}: {} {} {} {}".format(cost3, w, a, r, r2)

players.sort(key=lambda c: c.cost)

for p in players:
    #print "----------------"
    boss = Boss(bossHP, bossDamage, bossArmor)
    while not (p.isDead() or boss.isDead()):
        boss.attacked(p.damage)

        if not boss.isDead():
            p.attacked(boss.damage)

    if not p.isDead():
        lowestCost = p.cost
        break

print "============="
print "=== Part 1"
print "Min Gold = {}".format(lowestCost)
print "============="


players.sort(key=lambda c: c.cost, reverse=True)

for p in players:
    #print "----------------"
    boss = Boss(bossHP, bossDamage, bossArmor)
    while not (p.isDead() or boss.isDead()):
        boss.attacked(p.damage)

        if not boss.isDead():
            p.attacked(boss.damage)

    if p.isDead():
        maxCost = p.cost
        break

print "============="
print "=== Part 1"
print "Max Gold = {}".format(maxCost)
print "============="
