#!/usr/bin/env python3
"""
Advent of Code 2015: Day #
"""
import os
import hashlib

SECRET_KEY = 'iwrupvqb'

def make_byte_string(n):
    return "{}{}".format(SECRET_KEY, n).encode()

def first_half():
    """
    first half solver:
    find MD5 hashes which, in hexadecimal, start with at least five zeroes.
    iwrupvqb followed by a number in decimal.
    To mine AdventCoins, you must find Santa the lowest positive number that produces such a hash.
    """
    n = 1
    while n:
        new_bytes = make_byte_string(n)
        hash_to_check = hashlib.md5(new_bytes).hexdigest()
        if hash_to_check[:5] == '00000':
            return n
        n += 1

def second_half():
    """
    second half solver:
    """
    n = 346386
    while n:
        new_bytes = make_byte_string(n)
        hash_to_check = hashlib.md5(new_bytes).hexdigest()
        if hash_to_check[:6] == '000000':
            return n
        n += 1

def app():
    """
    runs day application
    """
    half_one = first_half()
    half_two = second_half()
    print(half_one, half_two)

if __name__ == "__main__":
    """
    MAIN APP
    """
    app()
