#!/usr/bin/python

import sys
import re

class Net:
    def __init__(self, name):
        self.name = name
        self.val  = -1
        self.resolved = False

    def update(self,val):
        assert not self.resolved, "Net already updated!"
        self.val = val
        self.resolved = True

class Gate:
    def __init__(self, gType, aNet, bNet, outNet):
        self.gType = gType
        self.a     = aNet
        self.b     = bNet
        self.out   = outNet
        self.outResolved = False
    
    def inputReady(self):
        return self.a.resolved and self.b.resolved

    def update(self):
        assert self.a.resolved and self.b.resolved, "input nets not resolved!"

        outVal = 0
        if   self.gType == "AND":    outVal = self.a.val & self.b.val
        elif self.gType == "OR":     outVal = self.a.val | self.b.val
        elif self.gType == "LSHIFT": outVal = self.a.val << self.b.val
        elif self.gType == "RSHIFT": outVal = self.a.val >> self.b.val
        elif self.gType == "NOT":    outVal = ~self.a.val
        elif self.gType == "BUF":    outVal = self.a.val
        else: assert 0, "invalid gate type"

        outVal = outVal & 0xffff
        self.out.update(outVal)
        self.outResolved = True

        #print "updated {} with {} by doing {} {} {}".format(self.out.name, outVal, self.a.val, self.gType, self.b.val)

    def getStr(self):
        if self.gType != "NOT": return "{} {} {} -> {}".format(self.a.name, self.gType, self.b.name, self.out.name)
        else:                   return "{} {} -> {}".format(self.gType, self.a.name, self.out.name)

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

nets  = {}
gates = []
inputFile = open(sys.argv[1], "r")

for line in inputFile.readlines():
    m = re.search("^((\w+) )?(AND|OR|LSHIFT|RSHIFT|NOT)?( (\w+) )?-> (\w+)", line)
    assert m, "invalid line = {}".format(line)

    aNet   = m.group(2)
    bNet   = m.group(5)
    outNet = m.group(6)
    gType  = m.group(3)

    if aNet:
        if re.search("^(\d+)$",aNet): # a is constant
            aConstNet = "CONST{}".format(aNet)
            if not aConstNet in nets.keys():
                nets[aConstNet] = Net(aConstNet)
                nets[aConstNet].update(int(aNet))
            aNet = aConstNet
        elif not aNet in nets.keys():
            nets[aNet] = Net(aNet)

    if bNet:
        if re.search("^(\d+)$",bNet): # b is constant
            bConstNet = "CONST{}".format(bNet)
            if not bConstNet in nets.keys():
                nets[bConstNet] = Net(bConstNet)
                nets[bConstNet].update(int(bNet))
            bNet = bConstNet
        elif not bNet in nets.keys():
            nets[bNet] = Net(bNet)

    if not outNet in nets.keys():
        nets[outNet] = Net(outNet)

    if   gType is None:     gates.append(Gate("BUF",    nets[aNet], nets[aNet], nets[outNet]))
    elif gType == "AND":    gates.append(Gate("AND",    nets[aNet], nets[bNet], nets[outNet]))
    elif gType == "OR":     gates.append(Gate("OR",     nets[aNet], nets[bNet], nets[outNet]))
    elif gType == "LSHIFT": gates.append(Gate("LSHIFT", nets[aNet], nets[bNet], nets[outNet]))
    elif gType == "RSHIFT": gates.append(Gate("RSHIFT", nets[aNet], nets[bNet], nets[outNet]))
    elif gType == "NOT":    gates.append(Gate("NOT",    nets[bNet], nets[bNet], nets[outNet]))

inputFile.close()

#for g in gates:
#    print g.getStr()

pendingGates = True
while pendingGates:
    pendingGates = False

    notReadyGates = 0
    for g in gates:
        if g.inputReady() and not g.outResolved:
            g.update()
        elif not g.outResolved:
            notReadyGates += 1
            pendingGates = True

    #print "pending gates = {}".format(notReadyGates)

#for n in nets.values():
#    print "{}: {}".format(n.name, n.val)

print "================"
print "--- Part 1"
print "a = {}".format(nets["a"].val)

########## PART 2 ##########

newNet = "CONST{}".format(nets["a"].val)
if not newNet in nets.keys():
    nets[newNet] = Net(newNet)
    nets[newNet].update(nets["a"].val)

for g in gates:
    g.outResolved=False
    if g.out.name == "b":
        g.a = nets[newNet]
        g.b = nets[newNet]

for n in nets.keys():
    if not re.search("CONST", nets[n].name):
        nets[n].resolved=False

pendingGates = True
while pendingGates:
    pendingGates = False

    notReadyGates = 0
    for g in gates:
        if g.inputReady() and not g.outResolved:
            g.update()
        elif not g.outResolved:
            notReadyGates += 1
            pendingGates = True

#    print "pending gates = {}".format(notReadyGates)

print "================"
print "--- Part 2"
print "a = {}".format(nets["a"].val)




