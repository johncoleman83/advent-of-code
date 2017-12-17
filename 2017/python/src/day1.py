#!/usr/bin/env python3
"""
Advent of Code 2017: Day #
"""
import os
from readdayinput import readdayinput
testcase = "11221"


def first_half(dayinput):
    """
    first half solver:
    """
    half = len(dayinput) // 2
    end = len(dayinput)
    dayinput = dayinput * 2
    i = 0
    total = 0
    while i < end:
        next_i = i + half
        if dayinput[i] == dayinput[next_i]:
            total += int(dayinput[i])
        i += 1
    print(total)

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
