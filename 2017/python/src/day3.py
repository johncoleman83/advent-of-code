#!/usr/bin/env python3
"""
Advent of Code 2017: Day #
"""
import os
from readdayinput import readdayinput
test = [
    [17,  16,  15,  14,  13],
    [18,   5,   4,   3,  12],
    [19,   6,   1,   2,  11],
    [20,   7,   8,   9,  10],
    [21,  22,  23,  24,  25]
]


def first_half(dayinput):
    """
    first half solver:
    """
    loop = []
    n = 1
    while n < dayinput:
        loop.append([n])
        n += 1
        # right
        end = len(loop) + 1
        while len(loop[-1]) < end:
            loop[-1].append(n)
            n += 1
        # up
        i = len(loop) - 2
        while i >= 0:
            loop[i].append(n)
            n += 1
            i -= 1
        loop.insert(0, [n])
        n += 1
        # left
        while len(loop[0]) < len(loop) + 1:
            loop[0].insert(0, n)
            n += 1
        # down
        i = 1
        while i < len(loop[0]) - 1:
            loop[i].insert(0, n)
            n += 1
            i += 1
    i = 0
    while i < len(loop):
        if dayinput in loop[i]:
            row, col = i, loop[i].index(dayinput)
            total_r, total_c = len(loop), len(loop[i])
            break
        i += 1
    half = total_r // 2
    steps = abs(half - row)
    half = total_c // 2
    steps += abs(half - col)
    return steps

def check_num(n):
    return n >= 361527

def second_half(dayinput):
    """
    second half solver:
    """
    loop = []
    n = 1
    while n < dayinput:
        loop.append([n])
        # right
        end = len(loop) + 1
        while len(loop[-1]) < end:
            try:
                n += loop[-2][len(loop[-1]) + 1]
            except:
                pass
            try:
                n += loop[-2][len(loop[-1])]
            except:
                pass
            try:
                n += loop[-2][len(loop[-1]) - 1]
            except:
                pass
            loop[-1].append(n)

        # up
        i = len(loop) - 2
        while i >= 0:
            n += loop[i + 1][-2]
            n += loop[i][-1]
            if i - 1 != -1:
                n += loop[i - 1][-1]
            loop[i].append(n)
            i -= 1
        n += loop[0][-2]
        loop.insert(0, [n])
        # left
        while len(loop[0]) < len(loop) + 1:
            n += loop[1][-len(loop[0])]
            try:
                n += loop[1][-len(loop[0]) - 1]
            except:
                pass
            try:
                n += loop[1][-len(loop[0]) - 2]
            except:
                pass
            loop[0].insert(0, n)
        # down
        i = 1
        while i < len(loop[0]):
            n += loop[i - 1][1]
            try:
                n += loop[i][0]
            except:
                pass
            try:
                n += loop[i + 1][0]
            except:
                pass
            if i == len(loop[0]) - 1:
                break
            loop[i].insert(0, n)
            i += 1
    result = []
    for row in loop:
        for col in row:
            if check_num(col):
                result.append(col)
    return min(result)


def app():
    """
    runs day application
    """
    dayinput = 361527 # readdayinput()
    half_one = first_half(dayinput)
    half_two = second_half(dayinput)
    print(half_one, half_two)



if __name__ == "__main__":
    """
    MAIN APP
    """
    app()
