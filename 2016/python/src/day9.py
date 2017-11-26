#!/usr/bin/env python3
"""
Advent of Code 2016: Day #
"""
import os

def readdayinput():
    """
    Reads day input to solve
    """
    thisfile = os.path.basename(__file__)
    thisfile = thisfile[:len(thisfile) - 3]
    print("{}\n{}".format("-" * len(thisfile), thisfile))
    if __name__ == "__main__":
        resource = "../resources"
    else:
        resource = "./resources"
    dayinputfile = "{}/{}input.txt".format(resource, thisfile)
    with open(dayinputfile, mode='r', encoding='utf-8') as fileio:
        dayinput = fileio.read()
    dayinput = dayinput.strip('\n')
    return dayinput


def first_half(dayinput):
    """
    first half solver:
    """
    lines = dayinput.split('\n')

def app():
    """
    runs day application
    """
    dayinput = readdayinput()
    result = first_half(dayinput)
    print(result)

if __name__ == "__main__":
    """
    MAIN APP
    """
    app()
