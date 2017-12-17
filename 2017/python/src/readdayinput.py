#!/usr/bin/env python3
"""
Advent of Code 2017: Reads Day Input
"""
import os
import sys

def readdayinput():
    """
    Reads day input to solve
    """
    THISFILE = sys.argv[0][2:-3]
    print("{}\n{}".format("-" * len(THISFILE), THISFILE))
    inputtxt = "{}input.txt".format(THISFILE)
    if os.path.exists("../resources/{}".format(inputtxt)):
        dayinputfile = "../resources/{}".format(inputtxt)
    elif os.path.exists("./resources/{}".format(inputtxt)):
        dayinputfile = "./resources/{}".format(inputtxt)
    else:
        print('error, no input text file', file=sys.stderr)
        sys.exit(1)
    with open(dayinputfile, mode='r', encoding='utf-8') as fileio:
        dayinput = fileio.read()
    dayinput = dayinput.strip('\n')
    return dayinput

if __name__ == "__main__":
    """
    MAIN APP
    """
    print('Usage: import readdayinput')
