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
    lines = [int(i) for i in lines]
    i = 0
    steps = 0
    while i < len(lines) and i >= 0:
        jump = lines[i]
        lines[i] += 1
        i += jump
        steps += 1
    return steps


def second_half(dayinput):
    """
    second half solver:
    """
    lines = dayinput.split('\n')
    lines = [int(i) for i in lines]
    i = 0
    steps = 0
    while i < len(lines) and i >= 0:
        jump = lines[i]
        if jump >= 3:
            lines[i] -= 1
        else:
            lines[i] += 1
        i += jump
        steps += 1
    return steps


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
