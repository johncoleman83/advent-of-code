#!/usr/bin/env python3
"""
Advent of Code 2017: Day #
"""
import os
from shared.readdayinput import readdayinput

TEST = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""


def first_half(dayinput):
    """
    first half solver:
    """
    #dayinput = TEST
    lines = dayinput.split('\n')
    assembly = []
    registers = {}
    sounds_played = []
    for line in lines:
        line = line.split(' ')
        if len(line) == 3:
            if (line[2].replace('-', '')).isdigit():
                line[2] = int(line[2])
        assembly.append(line)
        if line[1] not in registers:
            registers[line[1]] = 0
    recovered_sounds = []
    i = 0
    while i < len(assembly):
        code = assembly[i]
        if len(code) == 3:
            Y = code[2]
            if type(Y).__name__ == 'str':
                Y = registers[Y]
        if code[0] == 'snd':
            sounds_played.append(registers[code[1]])
        elif code[0] == 'set':
            registers[code[1]] = Y
        elif code[0] == 'add':
            registers[code[1]] += Y
        elif code[0] == 'mul':
            registers[code[1]] = registers[code[1]] * Y
        elif code[0] == 'mod':
            registers[code[1]] = registers[code[1]] % Y
        elif code[0] == 'rcv':
            if registers[code[1]] != 0:
                recovered_sounds.append(sounds_played[-1])
                print('recovered')
                print(sounds_played[-1])
                return None
        elif code[0] == 'jgz':
            if registers[code[1]] > 0:
                i = i + Y
                continue
        i += 1


assemblyA, assemblyB = [], []
registersA, registersB = {}, {}
sentA, sentB = [], []
total_one_sent = 0
iA, iB = 0, 0


def handleA(action):
    global iA
    global iB
    global assemblyA
    global assemblyB
    global registerB
    global registersA
    global sentB
    global sentA
    global total_one_sent
    while iA < len(assemblyA):
        #print(iA, assemblyA[iA])
        code = assemblyA[iA]
        if len(code) == 3:
            Y = code[2]
            if type(Y).__name__ == 'str':
                Y = registersA[Y]
        if code[0] == 'snd':
            if action == 'rcv':
                return True
            sentA.append(registersA[code[1]])
        elif code[0] == 'set':
            registersA[code[1]] = Y
        elif code[0] == 'add':
            registersA[code[1]] += Y
        elif code[0] == 'mul':
            registersA[code[1]] = registersA[code[1]] * Y
        elif code[0] == 'mod':
            registersA[code[1]] = registersA[code[1]] % Y
        elif code[0] == 'rcv':
            #print('A', action)
            if action == 'snd':
                return True
            if len(sentB) == 0:
                return False
            code[1] = sentB[0]
            del sentB[0]
        elif code[0] == 'jgz':
            if registersA[code[1]] > 0:
                iA = iA + Y
                continue
        iA += 1
    return False


def handleB(action):
    global iA
    global iB
    global assemblyA
    global assemblyB
    global registerB
    global registersA
    global sentB
    global sentA
    global total_one_sent
    while iB < len(assemblyB):
        code = assemblyB[iB]
        if len(code) == 3:
            Y = code[2]
            if type(Y).__name__ == 'str':
                Y = registersB[Y]
        if code[0] == 'snd':
            if action == 'rcv':
                return True
            sentB.append(registersB[code[1]])
            total_one_sent += 1
        elif code[0] == 'set':
            registersB[code[1]] = Y
        elif code[0] == 'add':
            registersB[code[1]] += Y
        elif code[0] == 'mul':
            registersB[code[1]] = registersB[code[1]] * Y
        elif code[0] == 'mod':
            registersB[code[1]] = registersB[code[1]] % Y
        elif code[0] == 'rcv':
            #print('B', action)
            if action == 'snd':
                return True
            if len(sentA) == 0:
                return False
            code[1] = sentA[0]
            del sentA[0]
        elif code[0] == 'jgz':
            if registersB[code[1]] > 0:
                iB = iB + Y
                continue
        iB += 1
    return False


def second_half(dayinput):
    """
    second half solver:
    """
    global iA
    global iB
    global assemblyA
    global assemblyB
    global registerB
    global registersA
    global sentB
    global sentA
    global total_one_sent
    lines = dayinput.split('\n')
    for line in lines:
        line = line.split(' ')
        if len(line) == 3:
            if (line[2].replace('-', '')).isdigit():
                line[2] = int(line[2])
        assemblyA.append(line)
        assemblyB.append(line)
        if line[1] not in registersA:
            registersA[line[1]] = 0
            registersB[line[1]] = 0
    registersB['p'] = 1


    while True:
        #print('rotation')
        res1 = handleA('snd')
        res3 = handleB('rcv')
        res2 = handleB('snd')
        res4 = handleA('rcv')
        if not res3 and not res4:
            break
    print('total: ', total_one_sent)


def app():
    """
    runs day application
    """
    dayinput = readdayinput()
    #half_one = first_half(dayinput)
    half_two = second_half(dayinput)
    print(half_two)
    #print(half_one, half_two)

if __name__ == "__main__":
    """
    MAIN APP
    """
    app()
