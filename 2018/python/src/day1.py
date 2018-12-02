#!/usr/bin/env python3
"""
Advent of Code 2018: Day #
"""
import os
from shared.readdayinput import readdayinput

def first_half(dayinput):
    """
    first half solver:
    Starting with a frequency of zero, what is the resulting
    frequency after all of the changes in frequency have been applied?
    """
    lines = dayinput.split('\n')
    result = 0
    for freq in lines:
        result += int(freq)
    return result

def second_half(dayinput):
    """
    second half solver:
    What is the first frequency your device reaches twice?
    """
    lines = dayinput.split('\n')
    freq_set = {0}
    total_freq = 0
    while True:
        for freq in lines:
            total_freq += int(freq)
            if total_freq in freq_set:
                return total_freq
            freq_set.add(total_freq)
    return None

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
