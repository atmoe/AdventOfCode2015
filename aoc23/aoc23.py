#!/usr/bin/python

import sys
import re
import copy
import random 

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

dbgEn = True
def dbgPrint(text):
    if dbgEn:
        print(text)

class ExecState:
    def __init__(self, pc, a, b):
        self.pc = pc
        self.a  = a
        self.b  = b

    def printState(self):
        dbgPrint(f'PC: {self.pc}  A: {self.a}  B: {self.b}')


class Instruction:
    def __init__(self, op, args):
        self.op   = op
        self.args = args

    def printInstr(self):
        dbgPrint(f'{self.op} {self.args}')

    def execute(self, exSt):
        if self.op == 'hlf':
            if self.args[0] == "a":
                exSt.a = exSt.a / 2
            elif self.args[0] == "b":
                exSt.b = exSt.b / 2
            exSt.pc+=1

        elif self.op == 'tpl':
            if self.args[0] == "a":
                exSt.a = exSt.a * 3
            elif self.args[0] == "b":
                exSt.b = exSt.b * 3
            exSt.pc+=1

        elif self.op == 'inc':
            if self.args[0] == "a":
                exSt.a = exSt.a + 1
            elif self.args[0] == "b":
                exSt.b = exSt.b + 1
            exSt.pc+=1

        elif self.op == 'jmp':
            exSt.pc += int(self.args[0])

        elif self.op == 'jie':
            if self.args[0] == "a" and exSt.a % 2 == 0:
                exSt.pc += int(self.args[1])
                
            elif self.args[0] == "b" and exSt.b % 2 == 0:
                exSt.pc += int(self.args[1])

            else:
                exSt.pc += 1
           
        elif self.op == 'jio':
            if self.args[0] == "a" and exSt.a == 1:
                exSt.pc += int(self.args[1])
                
            elif self.args[0] == "b" and exSt.b == 1:
                exSt.pc += int(self.args[1])

            else:
                exSt.pc += 1


inputFile = open(sys.argv[1], "r")
program = []
for line in inputFile.readlines():
    instrRe = re.match("(\w*) *(.*)", line)
    instr = instrRe.group(1)
    args  = instrRe.group(2).split(", ")
    program.append(Instruction(instr, args))
inputFile.close()


for i in program:
    i.printInstr()

print("==============")
print("=== Part 1 ===")
print("==============")
doPart1 = True
if doPart1:
    execState = ExecState(0,0,0)

    execState.printState()
    dbgPrint("------------------------------")
    while execState.pc < len(program):
        program[execState.pc].printInstr()
        program[execState.pc].execute(execState)
        execState.printState()
        dbgPrint("------------------------------")
        
    
print("==============")
print("=== Part 2 ===")
print("==============")
doPart2 = True
if doPart2:
    execState = ExecState(0,1,0)

    execState.printState()
    dbgPrint("------------------------------")
    while execState.pc < len(program):
        program[execState.pc].printInstr()
        program[execState.pc].execute(execState)
        execState.printState()
        dbgPrint("------------------------------")
 
