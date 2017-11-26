#!/usr/bin/env python3
"""
Advent of Code 2016: Day 6
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

def sort_by_frequencies(alphas):
    """
    sorts string by frequencies
    """
    items = []
    temp = [alphas[0]]
    for x in range(1, len(alphas)):
        if alphas[x] == alphas[x - 1]:
            temp.append(alphas[x])
        else:
            items.append(''.join(temp))
            temp = [alphas[x]]
    items.append(''.join(temp))
    newa = ''.join([k[0] for k in sorted(items, key=lambda x: -len(x))])
    return newa

def find_repititions(dayinput):
    """
    first half solver:
    get message from repititions
    """
    lines = dayinput.split('\n')
    rotated = []
    rotated[:] = zip(*lines[::-1])
    rotated = [''.join(sorted(list(x))) for x in rotated]
    message = []
    message2 = []
    for line in rotated:
        newalpha = sort_by_frequencies(line)
        message.append(newalpha[0])
        message2.append(newalpha[-1])
    return "1: {} -- 2: {}".format(''.join(message), ''.join(message2))

def app():
    """
    runs day application
    """
    dayinput = readdayinput()
    repitition_message = find_repititions(dayinput)
    print(repitition_message)


if __name__ == "__main__":
    """
    MAIN APP
    """
    app()
