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
    knot = [i for i in range(256)]
    #knot = [0, 1, 2, 3, 4]
    sub_lengths = [int(i) for i in dayinput.split(',')]
    #sub_lengths = [3, 4, 1, 5]
    current = skip = 0
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

    return knot[0] * knot[1]


def second_half(dayinput):
    """
    second half solver:
    """
    suffix = [17, 31, 73, 47, 23]
    knot = [i for i in range(256)]
    sub_lengths = []
    for x in dayinput:
        sub_lengths.append(ord(x))
    print(sub_lengths)
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
    print(knot)
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
    print(dense_hash)
    knot_hash = []
    for val in dense_hash:
        hex_val = hex(val).split('x')[-1]
        if len(hex_val) == 1:
            hex_val = '0' + hex_val
        knot_hash.append(hex_val)

    return ''.join(knot_hash)


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
