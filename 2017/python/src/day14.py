#!/usr/bin/env python3
"""
Advent of Code 2017: Day #
"""
import os
from readdayinput import readdayinput
#from gridday14 import GRID

def knot_hash(dayinput):
    """
    second half solver day 10:
    """
    suffix = [17, 31, 73, 47, 23]
    knot = [i for i in range(256)]
    sub_lengths = []
    for x in dayinput:
        sub_lengths.append(ord(x))
    sub_lengths += suffix
    current = skip = 0
    for x in range(64):
        for length in sub_lengths:
            skip_base, index, counter = length, current, 0
            sub = []
            while counter < length:
                if index == len(knot):
                    index = 0
                sub.append(knot[index])
                index += 1
                counter += 1
            sub = list(reversed(sub))
            index, counter = current, 0
            while counter < length:
                if index == len(knot):
                    index = 0
                knot[index] = sub[counter]
                index += 1
                counter += 1
            current += skip_base + skip
            while current >= len(knot):
                current = current - len(knot)
            skip += 1
    dense_hash = []
    index = 0
    while index < len(knot):
        value = knot[index]
        index += 1
        count = 0
        while count < 15:
            value ^= knot[index]
            index += 1
            count += 1
        dense_hash.append(value)
    knot_hash = []
    for val in dense_hash:
        hex_val = hex(val).split('x')[-1]
        if len(hex_val) == 1:
            hex_val = '0' + hex_val
        knot_hash.append(hex_val)
    return ''.join(knot_hash)


def hex_to_bin(h):
    b = bin(int(h, 16))[2:]
    while len(b) < 4:
        b = '0' + b
    return b

def first_half(dayinput):
    """
    first half solver:
    """
    squares_used = 0
    for x in range(128):
        k_hash = knot_hash("{}{}{}".format(dayinput, '-', str(x)))
        #row = []
        for h in k_hash:
            b = hex_to_bin(h)
            #row.append(b)
            squares_used += b.count('1')
        #row = ''.join(row)
        #squares_used += row.count('1')
    return squares_used

def second_half(dayinput):
    """
    second half solver:
    """
    squares_used = 0
    grid = []
    for x in range(128):
        k_hash = knot_hash("{}{}{}".format(dayinput, '-', str(x)))
        row = []
        for h in k_hash:
            b = hex_to_bin(h)
            for b_digit in b:
                row.append(int(b_digit))
        grid.append(row)
    return grid


def count_total_sections(grid):
    def mutate_section(row, col):
        if 0 <= row < len(grid) and 0 <= col < len(grid[row]) and grid[row][col] == 1:
            grid[row][col] = 0
            mutate_section(row + 1, col)
            mutate_section(row - 1, col)
            mutate_section(row, col + 1)
            mutate_section(row, col - 1)
            return 1
        return 0
    total_sections = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            total_sections += mutate_section(row, col)
    return total_sections


def app():
    """
    runs day application
    """
    dayinput = 'ffayrhll' # readdayinput()
    half_one = first_half(dayinput)
    GRID = second_half(dayinput)
    half_two = count_total_sections(GRID)
    print(half_one, half_two)

if __name__ == "__main__":
    """
    MAIN APP
    """
    app()
