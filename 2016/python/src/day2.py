#!/usr/bin/env python3
"""
Advent of Code 2016: Day 2
"""
import os
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
    return dayinput

def solvebathroom(dayinput):
    """
    first half solver:
    push buttons on keypad
    """
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
        print(positions[index], end="")
    print()

if __name__ == "__main__":
    """
    MAIN APP
    """
    dayinput = readdayinput()
    solvebathroom(dayinput)
