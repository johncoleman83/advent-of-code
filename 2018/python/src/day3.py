#!/usr/bin/env python3
"""
Advent of Code 2018: Day #
"""
import os
from shared.readdayinput import readdayinput

def parse_line(line):
    """
    parse the integers from:
    #1196 @ 349,741: 17x17
    """
    coords, dimensions = line.split(' @ ')[1].split(': ')
    coords = coords.split(',')
    x, y = int(coords[0]) + 1, 0 - (int(coords[1]) + 1)
    dimensions = dimensions.split('x')
    x_length, y_length = int(dimensions[0]), int(dimensions[1])
    return [x, y, x_length, y_length]

def loop_and_return_fabric(lines):
    """
    loops lines like:
    #1196 @ 349,741: 17x17
    """
    fabric = {}
    for line in lines:
        [x, y, x_length, y_length] = parse_line(line)
        i_x, i_y = 0, 0
        while i_y < y_length:
            i_x = 0
            while i_x < x_length:
                this_coords = (x + i_x, y - i_y)
                if fabric.get(this_coords, None) != None:
                    fabric[this_coords] += 1
                else:
                    fabric[this_coords] = 1
                i_x += 1
            i_y += 1
    return fabric

def first_half(dayinput):
    """
    first half solver:
    A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies
    a rectangle 3 inches from the left edge, 2 inches from the top
    edge, 5 inches wide, and 4 inches tall. How many square inches
    of fabric are within two or more claims?
    """
    lines = dayinput.split('\n')
    fabric = loop_and_return_fabric(lines)
    dupe_squares = 0
    for k, v in fabric.items():
        if v > 1:
            #print(k, v)
            dupe_squares += 1
    return dupe_squares

def second_half(dayinput):
    """
    second half solver:
    What is the ID of the only claim that doesn't overlap?
    """
    lines = dayinput.split('\n')
    fabric = loop_and_return_fabric(lines)

    for line in lines:
        [x, y, x_length, y_length] = parse_line(line)
        i_x, i_y = 0, 0
        all_squares_have_only_one_elf = True
        while i_y < y_length:
            i_x = 0
            while i_x < x_length:
                this_coords = (x + i_x, y - i_y)
                if fabric.get(this_coords) != 1:
                    all_squares_have_only_one_elf = False
                i_x += 1
            i_y += 1
        if all_squares_have_only_one_elf == True:
            return line
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
