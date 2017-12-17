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
    # 344
    circlebuffer = [0]
    current_pos = 0
    steps = 344
    index = 0
    count = 1
    size = 1
    all_zeros = []
    while count < 50000001:
        index += steps + 1
        index = index % size
        # ciclebuffer.insert(index, count)
        if index == 0:
            all_zeros.append(count)
        size += 1
        count += 1
    return all_zeros[-1]

def second_half(dayinput):
    """
    second half solver:
    """
    lines = dayinput.split('\n')
    result = None

    return result

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
