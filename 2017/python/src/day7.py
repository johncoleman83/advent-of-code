#!/usr/bin/env python3
"""
Advent of Code 2017: Day #
"""
import os
from shared.readdayinput import readdayinput


class Program():
    def __init__(self, n, w, c=[]):
        self.n = n
        self.w = w
        self.c = c

def first_half(dayinput):
    """
    first half solver:
    """
    lines = dayinput.split('\n')
    all_progs = {}
    has_connections = []
    for line in lines:
        prog, weight_connect = line.split(' (')
        if '->' in weight_connect:
            has_connections.append(prog)
            weight, connections = weight_connect.split(') -> ')
            weight = int(weight)
            connections = connections.split(', ')
        else:
            weight = int(weight_connect[:-1])
            connections = []
        all_progs[prog] = [weight, connections]
    for prog in has_connections:
        is_leaf = False
        for k, v in all_progs.items():
            if prog in v[1]:
                is_leaf = True
                break
        if is_leaf == False:
            return prog

def parse_tree(root):
    if len(root.c) == 0:
        root.con_weight = 0
        return root.w
    weights = []
    '''
    print(root.n)
    for con in root.c:
        print(con.n, end=", ")
    print()
    '''
    for con in root.c:
        weights.append(parse_tree(con))
    if root.n == 'mfzpvpj':
        print(root.n, root.w, weights, [con.n for con in root.c])
    if len(set(weights)) > 1:
        print(root.n, [con.n for con in root.c], weights)
    root.con_weight = sum(weights)
    return root.con_weight + root.w


def second_half(dayinput):
    """
    second half solver:
    """
    lines = dayinput.split('\n')
    all_progs = {}
    #has_connections = []
    for line in lines:
        prog, weight_connect = line.split(' (')
        if '->' in weight_connect:
            #has_connections.append(prog)
            weight, connections = weight_connect.split(') -> ')
            weight = int(weight)
            connections = connections.split(', ')
        else:
            weight = int(weight_connect[:-1])
            connections = []
        new_prog = Program(prog, weight, connections)
        all_progs[prog] = new_prog
    for name, prog in all_progs.items():
        new_cons = []
        for con in prog.c:
            new_cons.append(all_progs[con])
        prog.c = new_cons
    root = all_progs['uownj']
    total_weight = parse_tree(root)
    return total_weight


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
