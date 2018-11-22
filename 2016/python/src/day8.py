#!/usr/bin/env python3
"""
Advent of Code 2016: Day 8
"""
import os
from shared.readdayinput import readdayinput

def build_base():
    """
    builds base image full of off switches
    """
    return [[' ' for x in range(50)] for y in range(6)]

def handle_rect(instruction, image):
    """
    handles instructions to turn on switches
    rect AxB
    """
    dimensions = instruction.split(' ')[1].split('x')
    width = int(dimensions[0])
    height = int(dimensions[1])
    for row in range(height):
        for col in range(width):
            image[row][col] = '#'

def handle_rotate_row(instruction, image):
    """
    handles instruction to rotate row
    rotate row y=A by B
    """
    row = int(instruction.split('=')[1].split(' by ')[0])
    shift = int(instruction.split('=')[1].split(' by ')[1]) % 50
    rotated = [0 for x in range(50)]
    for index in range(50):
        new_index = index + shift
        if new_index > 49:
            new_index = new_index - 50
        rotated[new_index] = image[row][index]
    image[row] = rotated

def handle_rotate_col(instruction, image):
    """
    handles instruction to rotate the column
    rotate column x=A by B
    """
    col = int(instruction.split('=')[1].split(' by ')[0])
    shift = int(instruction.split('=')[1].split(' by ')[1]) % 50
    for step in range(shift):
        row = 0
        prev_i = image[5][col]
        while row < 6:
            this_i = image[row][col]
            image[row][col] = prev_i
            prev_i = this_i
            row += 1

def build_image(dayinput, image):
    """
    first half solver:
    """
    lines = dayinput.split('\n')
    for instruction in lines:
        if "rect" in instruction:
            handle_rect(instruction, image)
        if "row" in instruction:
            handle_rotate_row(instruction, image)
        if "column" in instruction:
            handle_rotate_col(instruction, image)

def app():
    """
    runs day application
    """
    dayinput = readdayinput()
    image = build_base()
    build_image(dayinput, image)
    switches_on = 0
    for row in image:
        switches_on += row.count('#')
        print(''.join(row))
    print("ON SWITCHES = {}".format(switches_on))

if __name__ == "__main__":
    """
    MAIN APP
    """
    app()
