#!/usr/bin/env python3
"""
Advent of Code 2017: Day #
"""
import os

test = [
    [17,  16,  15,  14,  13],
    [18,   5,   4,   3,  12],
    [19,   6,   1,   2,  11],
    [20,   7,   8,   9,  10],
    [21,  22,  23,  24,  25]
]

def readdayinput():
    """
    Reads day input to solve
    """
    thisfile = os.path.basename(__file__)
    thisfile = thisfile[:len(thisfile) - 3]
    print("{}\n{}".format("-" * len(thisfile), thisfile))
    if __name__ == "__main__":
        resource = "../resources"
    else:
        resource = "./resources"
    dayinputfile = "{}/{}input.txt".format(resource, thisfile)
    with open(dayinputfile, mode='r', encoding='utf-8') as fileio:
        dayinput = fileio.read()
    dayinput = dayinput.strip('\n')
    return dayinput

def first_half(dayinput):
    """
    first half solver:
    """
    loop = [[1]]
    n = 2
    while n < dayinput:
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
        loop.append([n])
        n += 1
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

def second_half(dayinput):
    """
    second half solver:
    """
    result = None

    return result

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
