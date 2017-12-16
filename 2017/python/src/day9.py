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


def first_half(stream):
    """
    first half solver:
    """
    stream = [x for x in stream]
    i = 0
    garbage = 0
    while i < len(stream):
        if stream[i] == '!':
            del stream[i]
            del stream[i]
            continue
        if stream[i] == '<':
            start = i
            temp = i
            while temp < len(stream):
                if stream[temp] == '!':
                    del stream[temp]
                    del stream[temp]
                    continue
                if stream[temp] == '>':
                    end = temp
                    break
                temp += 1
            garbage += (end - start - 1)
            stream = stream[:start] + stream[end + 1:]
        i += 1
    stream = ''.join(stream)
    stream = stream.replace(',', '')
    #print(stream)
    stream = [x for x in stream]
    q = []
    i = 0
    count = 0
    while i < len(stream):
        if stream[i] == '{':
            q.append('{')
        if stream[i] == '}':
            count += len(q)
            q.pop()
        i += 1
    return [count, garbage]

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
