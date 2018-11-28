#!/usr/bin/env python3
"""
Advent of Code 2015: Day #
"""
import os
from shared.readdayinput import readdayinput
VOWELS = { 'a', 'e', 'i', 'o', 'u' }
INVALID = [ 'ab', 'cd', 'pq', 'xy' ]

def has_double(s):
    p = None
    for c in s:
        if p and p == c: return True
        p = c
    return False

def vowel_count(s):
    c = 0
    for l in s:
        if l in VOWELS: c += 1
    return c

def has_invalid(s):
    for i in INVALID:
        if i in s: return True
    return False

def nice_string(s):
    return has_double(s) and vowel_count(s) >= 3 and not has_invalid(s)

def repeat_with_middle(s):
    for i in range(1, len(s) - 1):
        if s[i - 1] == s[i + 1]:
            return True
    return False

def repeat_same_two(s):
    for i in range(1, len(s) - 1):
        if "{}{}".format(s[i - 1], s[i]) in s[i + 1:]: return True
    return False

def nice_string_v2(s):
    return repeat_with_middle(s) and repeat_same_two(s)

def first_half(dayinput):
    """
    first half solver:
    - It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    - It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    - It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
    """
    lines = dayinput.split('\n')
    nice_strings_count = 0
    for s in lines:
        if nice_string(s): nice_strings_count += 1
    return nice_strings_count

def second_half(dayinput):
    """
    second half solver:
    - It contains a pair of any two letters that appears at least twice in the string without overlapping,
    like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    - It contains at least one letter which repeats with exactly one letter between them,
    like xyx, abcdefeghi (efe), or even aaa.
    """
    lines = dayinput.split('\n')
    nice_strings_count = 0
    for s in lines:
        if nice_string_v2(s): nice_strings_count += 1
    return nice_strings_count

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
