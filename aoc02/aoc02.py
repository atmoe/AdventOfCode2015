#!/usr/bin/python

import sys
import re

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

totalPaperArea = 0
totalRibbon = 0
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    m = re.match("^(\d+)x(\d+)x(\d+)$", line)
    assert m, "invalid line = {}".format(line)

    w = int(m.group(1))
    h = int(m.group(2))
    d = int(m.group(3))

    totalPaperArea += 2*w*h + 2*w*d + 2*d*h + min(w*h,w*d,d*h)
    totalRibbon += w*h*d + min(2*w+2*h, 2*w+2*d, 2*d+2*h)

inputFile.close()

print "Total Paper Area = {}".format(totalPaperArea)
print "Total Ribbon     = {}".format(totalRibbon)
