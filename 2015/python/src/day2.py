#!/usr/bin/env python3
"""
Advent of Code 2015: Day #
"""
import os
from shared.readdayinput import readdayinput

def first_half(dayinput):
    """
    first half solver:
    length l, width w, and height h
    find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l plus area of smallest side
    """
    lines = dayinput.split('\n')
    total_sq_feet = 0
    for line in lines:
        dimensions = map(lambda x: int(x), line.split('x'))
        [l, w, h] = sorted(dimensions)
        sq_feet = (2 * l * w) + (2 * w * h) + (2 * h * l) + (l * w)
        total_sq_feet += sq_feet
    return total_sq_feet

def second_half(dayinput):
    """
    second half solver:
    ribbon required to wrap a present is the shortest distance around its sides
    the perfect bow is equal to the cubic feet of volume of the present
    """
    lines = dayinput.split('\n')
    total_ribbon_feet = 0
    for line in lines:
        dimensions = map(lambda x: int(x), line.split('x'))
        [l, w, h] = sorted(dimensions)
        side_ribbon = 2 * (l + w)
        bow = l * w * h
        total_ribbon_feet += (side_ribbon + bow)
    return total_ribbon_feet

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
