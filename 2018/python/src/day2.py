#!/usr/bin/env python3
"""
Advent of Code 2018: Day #
"""
import os
import difflib
from shared.readdayinput import readdayinput

def first_half(dayinput):
    """
    first half solver:
    To make sure you didn't miss any, you scan the likely
    candidate boxes again, counting the number that have an
    ID containing exactly two of any letter and then separately
    counting those with exactly three of any letter. You can
    multiply those two counts together to get a rudimentary
    checksum and compare it to what your device predicts.
    """
    lines = dayinput.split('\n')
    result = None
    twos = 0
    threes = 0
    for line in lines:
        l_list = [l for l in line]
        found_twos = False
        found_threes = False
        for l in line:
            if l_list.count(l) == 2 and not found_twos:
                twos += 1
                found_twos = True
            if l_list.count(l) == 3 and not found_threes:
                threes += 1
                found_threes = True    
    return twos * threes

def second_half(dayinput):
    """
    second half solver:
    What letters are common between the two correct box IDs?
    (In the example above, this is found by removing the differing
    character from either ID, producing fgij.)
    """
    lines = dayinput.split('\n')
    result = None
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            line_1 = lines[i]
            line_2 = lines[j]
            output_list = [li for li in difflib.ndiff(line_1, line_2) if li[0] != ' ']
            if len(output_list) == 2:
                print(line_1, line_2, output_list)
    return None

def app():
    """
    runs day application
    """
    dayinput = readdayinput()
    half_one = first_half(dayinput)
    print(half_one)
    half_two = second_half(dayinput)
    print(half_two)

if __name__ == "__main__":
    """
    MAIN APP
    """
    app()
