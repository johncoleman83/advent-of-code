#!/usr/bin/env python3
"""
Advent of Code 2017: Day #
"""
import os
from readdayinput import readdayinput


def first_half():
    """
    first half solver:
    """
    # Generator A starts with 591 ; generator A uses 16807
    # Generator B starts with 393 ; ; generator B uses 48271
    # 2147483647
    A, B = 591, 393
    count = 0
    for x in range (40000000):
        A = (A * 16807) % 2147483647
        B = (B * 48271) % 2147483647
        if A & 65535 == B & 65535:
            count += 1
    return count

def second_half():
    """
    second half solver:
    """
    # Generator A starts with 591 ; generator A uses 16807
    # Generator B starts with 393 ; ; generator B uses 48271
    # 2147483647
    A, B = 591, 393
    count = 0
    for x in range (5000000):
        while A % 4 != 0:
            A = (A * 16807) % 2147483647
        while B % 8 != 0:
            B = (B * 48271) % 2147483647
        if A & 65535 == B & 65535:
            count += 1
        A = (A * 16807) % 2147483647
        B = (B * 48271) % 2147483647
    return count

def app():
    """
    runs day application
    """
    #dayinput = readdayinput()
    #half_one = first_half()
    half_two = second_half()
    print(half_two)
    #print(half_one, half_two)

if __name__ == "__main__":
    """
    MAIN APP
    """
    app()
