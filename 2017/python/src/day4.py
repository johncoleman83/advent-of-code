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
    lines = dayinput.split('\n')
    correct = 0
    for line in lines:
        if len(line.split(' ')) == len(set(line.split(' '))):
            correct += 1

    return correct

def second_half(dayinput):
    """
    second half solver:
    """
    lines = dayinput.split('\n')
    correct = 0
    for line in lines:
        word_set = set()
        line = line.split(' ')
        for word in line:
            word_set.add(''.join(sorted(list(word))))
        if len(line) == len(set(word_set)):
            correct += 1

    return correct

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
