#!/usr/bin/env python3
"""
Advent of Code 2015: Day #
"""
import os
from shared.readdayinput import readdayinput

def change_coords(h, coords):
    """
    updates coords of home based on directions from elf
    """
    if h == '^':
        coords[1] += 1
    elif h == '>':
        coords[0] += 1
    elif h == 'v':
        coords[1] -= 1
    elif h == '<':
        coords[0] -= 1
    return coords

def first_half(dayinput):
    """
    first half solver:
    """
    houses = { (0,0): 1 }
    coords = [0, 0]
    for h in dayinput:
        coords = change_coords(h, coords)
        home = (coords[0], coords[1])
        if houses.get(home, None):
            houses[home] += 1
        else:
            houses[home] = 1
    return len(houses)

def second_half(dayinput):
    """
    second half solver:
    """
    houses = { (0,0): 1 }
    santa_coords = [0, 0]
    robo_coords = [0, 0]
    santa = True
    for h in dayinput:
        if santa:
            santa_coords = change_coords(h, santa_coords)
            coords = santa_coords
        else:
            robo_coords = change_coords(h, robo_coords)
            coords = robo_coords
        home = (coords[0], coords[1])
        if houses.get(home, None) is not None:
            houses[home] += 1
        else:
            houses[home] = 1
        santa = not santa
    return len(houses)

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
