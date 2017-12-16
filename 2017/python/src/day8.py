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
    registers = {}
    max_max = 0
    for line in lines:
        register = line.split(' ')[0]
        amount = int(line.split(' ')[2])
        if register not in registers:
            registers[register] = 0
        equation = line.split(' if ')
        left, cond, right = equation[1].split(' ')
        if left not in registers:
            registers[left] = 0
        left, right = registers[left], int(right)
        execute = {
            '==': left == right,
            '!=': left != right,
            '>': left > right,
            '<': left < right,
            '>=': left >= right,
            '<=': left <= right
        }
        if execute[cond]:
            if 'inc' in line:
                registers[register] += amount
            elif 'dec' in line:
                registers[register] -= amount
            if registers[register] > max_max:
                max_max = registers[register]
    return [max([x for x in registers.values()]), max_max]

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
