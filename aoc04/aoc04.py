#!/usr/bin/python

import sys
import re
import hashlib

def getMD5(string):
    m = hashlib.md5()
    m.update(string)
    return m.hexdigest()

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

secretKey = sys.argv[1]



valFound = False
currVal = 1
while not valFound:
    inputStr = secretKey+str(currVal)

    md5 = getMD5(inputStr)

    if md5[0:5] == "00000":
        valFound = True
        break

    currVal += 1


print "hash suffix for 5 zeroes = {}".format(currVal)


valFound = False
currVal = 1
while not valFound:
    inputStr = secretKey+str(currVal)

    md5 = getMD5(inputStr)

    if md5[0:6] == "000000":
        valFound = True
        break

    currVal += 1


print "hash suffix for 6 zeroes = {}".format(currVal)

