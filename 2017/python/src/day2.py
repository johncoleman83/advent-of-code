#!/usr/bin/env python3
"""
Advent of Code 2017: Day #
"""
import os

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
    total = 0
    lines = dayinput.split('\n')
    for line in lines:
        nums = [int(n) for n in line.split('\t')]
        dif = max(nums) - min(nums)
        total += dif
    return total

def second_half(dayinput):
    """
    second half solver:
    """
    total = 0
    lines = dayinput.split('\n')
    for line in lines:
        nums = [int(n) for n in line.split('\t')]
        x = 0
        while x < len(nums):
            y = 0
            while y < len(nums):
                if y == x:
                    y += 1
                    continue
                diff = nums[x] / nums[y]
                if diff == int(diff):
                    y = x = len(nums)
                y += 1
            x += 1
        total += diff
    return total

def app():
    """
    runs day application
    """
    dayinput = readdayinput()
    result = first_half(dayinput)
    result2 = second_half(dayinput)
    print(result, result2)

if __name__ == "__main__":
    """
    MAIN APP
    """
    app()
