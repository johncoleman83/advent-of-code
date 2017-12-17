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
    correct = 0
    for line in lines:
        if len(line.split(' ')) == len(set(line.split(' '))):
            correct += 1

    return correct

def second_half(dayinput):
    """
    second half solver:
    """
    lines = dayinput.split('\n')
    correct = 0
    for line in lines:
        word_set = set()
        line = line.split(' ')
        for word in line:
            word_set.add(''.join(sorted(list(word))))
        if len(line) == len(set(word_set)):
            correct += 1

    return correct

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
