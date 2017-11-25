#!/usr/bin/env python3
"""
Advent of Code 2016: Day 2
"""
import os
debugging = "RRDDD"
testinstructions = """ULL
RRDDD
LURDL
UUUUD"""

def readdayinput():
    """
    Reads day input to solve
    """
    thisfile = os.path.basename(__file__)
    thisfile = thisfile[:len(thisfile) - 3]
    dayinputfile = "../resources/{}input.txt".format(thisfile)
    with open(dayinputfile, mode='r', encoding='utf-8') as fileio:
        dayinput = fileio.read()
    dayinput = dayinput.strip('\n')
    #dayinput = debugging
    #dayinput = testinstructions
    return dayinput

def solvebathroom(dayinput):
    """
    first half solver:
    push buttons on keypad
    """
    code = []
    cases = dayinput.split('\n')
    positions = [x for x in range(1, 10)]
    index = 4
    print()
    for case in cases:
        for d in case:
            if d == "U" and index > 2:
                index -= 3
            elif d == "D" and index < 6:
                index += 3
            elif d == "R" and index % 3 != 2:
                index += 1
            elif d == "L" and index % 3 != 0:
                index -= 1
        code.append(str(positions[index]))
    print(''.join(code))


def solvediamond(dayinput):
    """
    second half solver:
    push buttons on diamond keypad
    """
    code = []
    cases = dayinput.split('\n')
    positions = [x for x in range(1, 10)] + ['A', 'B', 'C', 'D']
    index = 4
    restrictions = {
        "U": [0, 1, 3, 4, 8],
        "D": [4, 8, 9, 11, 12],
        "R": [0, 3, 8, 11, 12],
        "L": [0, 1, 4, 9, 12]
    }
    print()
    for case in cases:
        for d in case:
            if d == "U" and index not in restrictions[d]:
                if index in [2, 12]:
                    index -= 2
                else:
                    index -= 4
            elif d == "D" and index not in restrictions[d]:
                if index in [0, 10]:
                    index += 2
                else:
                    index += 4
            elif d == "R" and index not in restrictions[d]:
                index += 1
            elif d == "L" and index not in restrictions[d]:
                index -= 1
        code.append(str(positions[index]))
    print(''.join(code))


if __name__ == "__main__":
    """
    MAIN APP
    """
    dayinput = readdayinput()
    solvebathroom(dayinput)
    solvediamond(dayinput)
