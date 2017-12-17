#!/usr/bin/env python3
"""
Advent of Code 2017: Day #
"""
import os
from readdayinput import readdayinput


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
