#!/usr/bin/python

import sys
import re
import copy
import random 

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

dbgEn = False

def spellCost(spell):
    if spell == "Missile":
        return 53
    elif spell == "Drain":
        return 73
    elif spell == "Shield":
        return 113
    elif spell == "Poison":
        return 173
    elif spell == "Recharge":
        return 229 

def canCastSpell(spell, splSeq):
    return (spell != "Poison"   or not "Poison"   in splSeq[-2:]) and \
           (spell != "Shield"   or not "Shield"   in splSeq[-2:]) and \
           (spell != "Recharge" or not "Recharge" in splSeq[-2:])

class Player:
    def __init__(self, hp, mana):
        self.hp        = hp 
        self.mana      = mana
        self.armor     = 0
        self.manaspent = 0

    def printMe(self):
        if dbgEn:
            print("Player has {} HP, {} Armor, {} Mana".format(self.hp, self.armor, self.mana))

    def isDead(self):
        return self.hp <= 0 or self.mana <= 0

    def updateArmor(self, armor):
        self.armor = armor

    def addMana(self, mana):
        self.mana += mana 

    def spendMana(self, mana):
        self.mana      -= mana 
        self.manaspent += mana

    def heal(self, hp):
        self.hp += hp  

    def attacked(self, damage):
        d = max(1, (damage - self.armor))
        self.hp -= d
        if dbgEn:
            print("The boss deals {} damage, player at {} hp".format(d, self.hp))

class Boss:
    def __init__(self, hp, damage):
        self.damage = damage
        self.hp     = hp

    def printMe(self):
        if dbgEn:
            print("Boss has {} HP".format(self.hp))

    def isDead(self):
        return self.hp <= 0

    def attacked(self, damage):
        self.hp -= damage

class SpellSeq:
    def __init__(self):
        self.spells = []
        self.cost = 0

    def addSpell(self, spell):
        assert (spell != "Poison"   or not "Poison"   in self.spells[-2:]), "invalid Poison!"
        assert (spell != "Shield"   or not "Shield"   in self.spells[-2:]), "invalid Shield!"
        assert (spell != "Recharge" or not "Recharge" in self.spells[-2:]), "invalid Recharge!"

        self.spells.append(spell)
        self.cost += spellCost(spell)

    def printSeq(self):
        print(f'{self.cost}: {self.spells}')

def simulate(boss, player, spells, hardMode):
    m_spells = list(spells)
    shieldCount = 0
    poisonCount = 0
    rechargeCount = 0
    turn = "Player"

    while not (player.isDead() or boss.isDead() or (turn == 'Player' and len(m_spells) == 0)):
        if dbgEn:
            print(f'--- {turn} Turn ---')
            player.printMe()
            boss.printMe()

        if hardMode and turn == "Player":
            player.attacked(1)
            if player.isDead():
                break

        # --- Apply Shield ---
        if shieldCount > 0:
            shieldCount -= 1
            if shieldCount == 0:
                player.updateArmor(0)
            if dbgEn:
                print(f'Shield Timer: {shieldCount}')

        # --- Apply Poison ---
        if poisonCount > 0:
            poisonCount -= 1
            boss.attacked(3)
            if dbgEn:
                print(f'Poison Timer: {poisonCount}')

        # --- Apply Recharge ---
        if rechargeCount > 0:
            rechargeCount -= 1
            player.addMana(101)
            if dbgEn:
                print(f'Recharge Timer: {rechargeCount}')

        if player.isDead() or boss.isDead():
            if dbgEn:
                print(f'')
            break

        # --- Play Turn ---
        if turn == "Player":
            # Cast Next Spell
            spell = m_spells.pop(0)
            assert spell != "Shield"   or shieldCount==0, f'{spell} cannot be cast'
            assert spell != "Poison"   or poisonCount==0, f'{spell} cannot be cast'
            assert spell != "Recharge" or rechargeCount==0, f'{spell} cannot be cast'

            if dbgEn:
                print(f'Player casting {spell}')

            player.spendMana(spellCost(spell))
            if player.isDead():
                break

            if spell == "Shield":
                player.updateArmor(7)
                shieldCount = 6
            elif spell == "Poison":
                poisonCount = 6
            elif spell == "Recharge":
                rechargeCount = 5
            elif spell == "Missile":
                boss.attacked(4)
            elif spell == "Drain":
                boss.attacked(2)
                player.heal(2)

            turn = "Boss"
        else:
            player.attacked(boss.damage)
            turn = "Player"

        if dbgEn:
            print(f'')

    if player.isDead():
        if dbgEn:
            print('Player Died')
        return "playerDied"
    elif boss.isDead():
        if dbgEn:
            print('Boss Died')
        return "bossDied"
    elif len(m_spells) == 0:
        if dbgEn:
            print('Ran out of Spells')
        return "outOfSpells"

inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    hp = re.match("^Hit Points: (\d+)", line)
    d  = re.match("^Damage: (\d+)", line)
    if hp: bossHP     = int(hp.group(1))
    if d:  bossDamage = int(d.group(1))
inputFile.close()

print("==============")
print("=== Part 1 ===")
print("==============")
doPart1 = True
if doPart1 == True:
    spellSequences = []
    for s in ["Missile", "Poison", "Drain", "Shield", "Recharge"]:
        seq = SpellSeq()
        seq.addSpell(s)
        spellSequences.append(seq)
    
    spellSequences.sort(key=lambda x: x.cost, reverse=True)
    
    ## test code
    #boss   = Boss(bossHP, bossDamage)
    #player = Player(50, 500)
    #seq = SpellSeq()
    #seq.addSpell("Shield")
    #seq.addSpell("Missile")
    #seq.addSpell("Missile")
    #seq.addSpell("Shield")
    #rtnCode = simulate(boss, player, seq.spells)
    #quit()
    
    minMana = 10000
    while len(spellSequences) > 0:
        seq = spellSequences.pop()
        if dbgEn:
            print(minMana)
            seq.printSeq()

        if seq.cost > minMana:
            continue
    
        boss   = Boss(bossHP, bossDamage)
        player = Player(50, 500)
        rtnCode = simulate(boss, player, seq.spells, False)
    
        if rtnCode == "playerDied":
            continue
    
        if rtnCode == "bossDied":
            if minMana > player.manaspent:
                minMana = player.manaspent
            continue
    
        if rtnCode == "outOfSpells":
            #  Generate new spell sequences
            for spl in ["Missile", "Poison", "Drain", "Shield", "Recharge"]:
                if canCastSpell(spl, seq.spells):
                    newSeq = copy.deepcopy(seq)
                    newSeq.addSpell(spl)
                    spellSequences.append(newSeq)
    
            #spellSequences.sort(key=lambda x: x.cost, reverse=True)
            spellSequences.sort(key=lambda x: x.cost, reverse=False)
            continue
    
        assert False, "invalid return code"
    
    print("Min Mana = {}".format(minMana))
    
print("==============")
print("=== Part 2 ===")
print("==============")
doPart2 = True
if doPart2 == True:
    spellSequences = []
    for s in ["Missile", "Poison", "Drain", "Shield", "Recharge"]:
        seq = SpellSeq()
        seq.addSpell(s)
        spellSequences.append(seq)
    
    spellSequences.sort(key=lambda x: x.cost, reverse=True)
    
    minMana = 10000
    while len(spellSequences) > 0:
        seq = spellSequences.pop()
        if dbgEn:
            print(minMana)
            seq.printSeq()

        if seq.cost > minMana:
            continue
    
        boss   = Boss(bossHP, bossDamage)
        player = Player(50, 500)
        rtnCode = simulate(boss, player, seq.spells, True)
    
        if rtnCode == "playerDied":
            continue
    
        if rtnCode == "bossDied":
            if minMana > player.manaspent:
                minMana = player.manaspent
            continue
    
        if rtnCode == "outOfSpells":
            #  Generate new spell sequences
            for spl in ["Missile", "Poison", "Drain", "Shield", "Recharge"]:
                if canCastSpell(spl, seq.spells):
                    newSeq = copy.deepcopy(seq)
                    newSeq.addSpell(spl)
                    spellSequences.append(newSeq)
    
            #spellSequences.sort(key=lambda x: x.cost, reverse=True)
            spellSequences.sort(key=lambda x: x.cost, reverse=False)
            continue
    
        assert False, "invalid return code"
    
    print("Min Mana = {}".format(minMana))
    
