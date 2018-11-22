#!/usr/bin/env python3
"""
Advent of Code 2017: Day #
"""
import os
from shared.readdayinput import readdayinput


def first_half(d):
    """
    first half solver:
    """
    d = d.split(',')
    away = 0
    vert = 0
    horzl = 0
    horzr = 0
    for step in d:
        if step == 'n':
            vert += 1
        elif step == 's':
            vert -= 1
        elif step == 'ne':
            horzr += 1
        elif step == 'sw':
            horzr -= 1
        elif step == 'nw':
            horzl += 1
        elif step == 'se':
            horzl -= 1
        temp = vert + horzr
        if temp > away:
            away = temp
            print(away)
            print("vert, horzr, horzl", vert, horzr, horzl)
    '''
    ne = d.count('ne')
    n = d.count('n')
    s = d.count('s')
    nw = d.count('nw')
    se = d.count('se')
    sw = d.count('sw')
    vert = n - s
    horzr = ne - sw
    horzl = nw - se
    '''
    print("vert, horzr, horzl", vert, horzr, horzl)
    result = None
    return result

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
