#!/usr/bin/env python3
"""
Advent of Code 2017: Day #
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
    programs = {}
    for line in lines:
        key, val = line.split(' <-> ')
        val = [int(x) for x in val.split(', ')]
        programs[int(key)] = val
    connections = [0]
    index = 0
    while index < len(connections):
        to_check = connections[index]
        for p in programs[to_check]:
            if p not in connections:
                connections.append(p)
        index += 1
    return len(connections)


def second_half(dayinput):
    """
    second half solver:
    """
    lines = dayinput.split('\n')
    programs = {}
    for line in lines:
        key, val = line.split(' <-> ')
        val = [int(x) for x in val.split(', ')]
        programs[int(key)] = val
    connections = [0]
    max_p = max([programs.keys()])
    total = set()
    for prog in programs.keys():
        connections = [prog]
        index = 0
        while index < len(connections):
            to_check = connections[index]
            for p in programs[to_check]:
                if p not in connections:
                    connections.append(p)
            index += 1
        total.add(''.join([str(x) for x in sorted(set(connections))]))

    return len(total)

def app():
    """
    runs day application
    """
    dayinput = readdayinput()
    half_one = first_half(dayinput)
    half_two = second_half(dayinput)
    print(half_one, half_two)

if __name__ == "__main__":
    """
    MAIN APP
    """
    app()
