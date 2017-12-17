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
    lines = dayinput.split('	')
    lines = [int(i) for i in lines]
    states = set()
    count = 0
    while ''.join([str(i) for i in lines]) not in states:
        max_n = max(lines)
        index_max = lines.index(max_n)
        index = index_max + 1
        states.add(''.join([str(i) for i in lines]))
        lines[index_max] = 0
        count += 1
        while max_n > 0:
            if index == len(lines):
                index = 0
            lines[index] += 1
            max_n -= 1
            index += 1
    return count

def second_half(dayinput):
    """
    second half solver:
    """
    lines = dayinput.split('	')
    lines = [int(i) for i in lines]
    states = dict()
    count = 0
    while ''.join([str(i) for i in lines]) not in states:
        max_n = max(lines)
        index_max = lines.index(max_n)
        index = index_max + 1
        states[''.join([str(i) for i in lines])] = count
        lines[index_max] = 0
        count += 1
        while max_n > 0:
            if index == len(lines):
                index = 0
            lines[index] += 1
            max_n -= 1
            index += 1
    return count - states[''.join([str(i) for i in lines])]

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
