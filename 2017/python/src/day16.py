#!/usr/bin/env python3
"""
Advent of Code 2017: Day #
"""
import os
from readdayinput import readdayinput


def first_half(dayinput):
    """
    first half solver:
    """
    positions = [x for x in 'abcdefghijklmnop']
    lines = dayinput.split(',')
    for move in lines:
        if move[0] == 'x':
            a, b = move[1:].split('/')
            a, b = int(a), int(b)
            positions[a], positions[b] = positions[b], positions[a]
        elif move[0] == 'p':
            a, b = move[1:].split('/')
            ai, bi = positions.index(a), positions.index(b)
            positions[ai], positions[bi] = positions[bi], positions[ai]
        elif move[0] == 's':
            spins = int(move[1:])
            while spins > 0:
                positions.insert(0, positions.pop())
                spins -= 1
    return ''.join(positions)

def second_half(dayinput):
    """
    'abcdefghijklmnop'
    'lbdiomkhgcjanefp'
    second half solver:
    """
    positions = [x for x in 'abcdefghijklmnop']
    lines = dayinput.split(',')
    all_positions = {'abcdefghijklmnop'}
    for x in range(48):
        for move in lines:
            if move[0] == 'x':
                a, b = move[1:].split('/')
                a, b = int(a), int(b)
                positions[a], positions[b] = positions[b], positions[a]
            elif move[0] == 'p':
                a, b = move[1:].split('/')
                ai, bi = positions.index(a), positions.index(b)
                positions[ai], positions[bi] = positions[bi], positions[ai]
            elif move[0] == 's':
                spins = int(move[1:])
                while spins > 0:
                    positions.insert(0, positions.pop())
                    spins -= 1
        this_pos = ''.join(positions)
        if this_pos in all_positions:
            print(x, ''.join(positions))
            return x
        else:
            all_positions.add(''.join(positions))
    return ''.join(positions)

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
