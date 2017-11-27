#!/usr/bin/env python3
"""
Advent of Code 2016: Day 9
"""
import os
import re
testinput = "(27x12)(20x12)(13x14)(7x10)(1x12)A"


def readdayinput():
    """
    Reads day input to solve
    """
    return testinput
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


def first_half(compressedfile):
    """
    first half solver:
    """
    compressedfile = compressedfile.replace('\n', '')
    compressedfile = compressedfile.replace(' ', '')
    compressedfile = compressedfile.replace('\t', '')
    pattern = r"\(\d+x\d+\)"
    allmatches = re.findall(pattern, compressedfile)
    storage = {
        0:None
    }
    for match in allmatches:
        updated = match[1:-1].split('x')
        start = max(storage.keys())
        index = compressedfile[start:].index(match) + start
        storage[index] = {
            "instruction": match,
            "length": len(match),
            "chars": int(updated[0]),
            "times": int(updated[1])
        }
    allstarts = sorted([i for i in storage.keys()])
    next_start = 0
    for i in allstarts:
        if i < next_start:
            #print("deleted index: {}, next start: {}, instruction: {}".format(i, next_start, storage[i].get("instruction")))
            del(storage[i])
        else:
            chars = storage[i].get("chars")
            L = storage[i].get("length")
            next_start = i + chars + L
    totalchars = len(compressedfile)
    for meta in storage.values():
        totalchars -= meta.get("length")
        totalchars += (meta.get("chars") * (meta.get("times") - 1))
        #print("index: {}, metadata: {}".format(k, v))
    return totalchars

def modify_vals(index, indexes, storage):
    """
    modifies compression instructions
    """
    meta = storage[index]
    times = meta.get("times")
    end = index + meta.get("length") + meta.get("chars")
    i = 0
    while i < len(indexes) and indexes[i] < end:
        storage[index]["chars"] -= storage[indexes[i]]["length"]
        storage[indexes[i]]["times"] = storage[indexes[i]]["times"] * (times - 1)
        i += 1

def second_half(compressedfile):
    """
    first half solver:
    """
    compressedfile = compressedfile.replace('\n', '')
    compressedfile = compressedfile.replace(' ', '')
    compressedfile = compressedfile.replace('\t', '')
    pattern = r"\(\d+x\d+\)"
    allmatches = re.findall(pattern, compressedfile)
    storage = {
        0:None
    }
    for match in allmatches:
        updated = match[1:-1].split('x')
        start = max(storage.keys())
        index = compressedfile[start:].index(match) + start
        storage[index] = {
            "instruction": match,
            "length": len(match),
            "chars": int(updated[0]),
            "times": int(updated[1])
        }
    all_indexes = sorted([i for i in storage.keys()])
    decompressed
    i = 0
    while i < len(all_indexes):
        modify_vals(all_indexes[i], all_indexes[i + 1:], storage)
        i += 1
    totalchars = len(compressedfile)
    for index, meta in storage.items():
        totalchars -= meta.get("length")
        totalchars += (meta.get("chars") * (meta.get("times") - 1))
        print("index: {}, metadata: {}".format(index, meta))
    return totalchars

def app():
    """
    runs day application
    """
    dayinput = readdayinput()
    #result = first_half(dayinput)
    result2 = second_half(dayinput)
    print(result2)

if __name__ == "__main__":
    """
    MAIN APP
    """
    app()
