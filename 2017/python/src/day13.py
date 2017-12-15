#!/usr/bin/env python3
"""
Advent of Code 2017: Day #
"""
import os

TEST = """0: 3
1: 2
4: 4
6: 4"""

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


def reset_firewall(firewall):
    for key in firewall.keys():
        if firewall[key] is None:
            continue
        index = firewall[key].index(1)
        firewall[key][index] = 0
        firewall[key][1] = 1

def copy_firewall(firewall):
    copy = {}
    for key, val in firewall.items():
        if val is None:
            copy[key] = val
        else:
            copy[key] = [x for x in val]
    return copy

def shift_firewall(firewall):
    for key in firewall.keys():
        if firewall[key] is None:
            continue
        if len(firewall[key]) <= 2:
            continue
        direction = firewall[key][0]
        index = firewall[key].index(1)
        firewall[key][index] = 0
        if direction == 'F':
            index += 1
        else:
            index -= 1
        if index == len(firewall[key]):
            index = len(firewall[key]) - 2
            firewall[key][0] = 'B'
        elif index == 0:
            index = 2
            firewall[key][0] = 'F'
        firewall[key][index] = 1

def run_firewall_is_success(max_layer, firewall):
    i = 0
    while i < max_layer + 1:
        if firewall[i] is None:
            pass
        elif firewall[i][1] == 1:
            return False
        shift_firewall(firewall)
        i += 1
    return True

def run_firewall(max_layer, firewall):
    i = 0
    total_severity = 0
    while i < max_layer + 1:
        if firewall[i] is None:
            pass
        elif firewall[i][1] == 1:
            total_severity += i * (len(firewall[i]) - 1)
        shift_firewall(firewall)
        i += 1
    return total_severity

def first_half(dayinput):
    """
    first half solver:
    """
    lines = dayinput.split('\n')
    firewall = {}
    for line in lines:
        layer, depth = line.split(': ')
        firewall[int(layer)] = [0 for x in range(int(depth) + 1)]
        firewall[int(layer)][0] = 'F'
        firewall[int(layer)][1] = 1
    last_layer = max(list(firewall.keys()))
    for i in range(last_layer):
        if i not in firewall:
            firewall[i] = None
    result = run_firewall(last_layer, firewall)
    return result

def second_half(dayinput):
    """
    second half solver:
    """
    lines = dayinput.split('\n')
    firewall = {}
    for line in lines:
        layer, depth = line.split(': ')
        firewall[int(layer)] = [0 for x in range(int(depth) + 1)]
        firewall[int(layer)][0] = 'F'
        firewall[int(layer)][1] = 1
    last_layer = max(list(firewall.keys()))
    for i in range(last_layer):
        if i not in firewall:
            firewall[i] = None
    test = 0
    while True:
        copy_fire = copy_firewall(firewall)
        result = run_firewall_is_success(last_layer, copy_fire)
        if result is True:
            return test
        shift_firewall(firewall)
        test += 1

def app():
    """
    runs day application
    """
    dayinput = readdayinput()
    half_one = first_half(dayinput)
    half_two = second_half(dayinput)
    #half_two = second_half(TEST)
    print(half_one, half_two)

if __name__ == "__main__":
    """
    MAIN APP
    """
    app()
