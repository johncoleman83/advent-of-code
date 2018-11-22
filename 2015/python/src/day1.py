#!/usr/bin/env python3
"""
Advent of Code 2018: Day #
An opening parenthesis, (, means he should go up one floor
and a closing parenthesis, ), means he should go down one floor.

"""
import os
from shared.readdayinput import readdayinput

def first_half(dayinput):
    """
    first half solver:
    """
    result = dayinput.count('(') - dayinput.count(')')

    return result

def second_half(dayinput):
    """
    second half solver:
    """
    i = 0
    floor = 0
    while i < len(dayinput):
        if dayinput[i] == '(':
            floor += 1
        elif dayinput[i] == ')':
            floor -=1
        if floor == -1:
            return i + 1
        i += 1
    return -1

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
