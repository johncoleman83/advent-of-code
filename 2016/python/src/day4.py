#!/usr/bin/env python3
"""
Advent of Code 2016: Day 4
"""
import os
testinstructions = """aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]"""
# sum of test instructions: `1514`

def readdayinput():
    """
    Reads day input to solve
    """
    #return testinstructions
    thisfile = os.path.basename(__file__)
    thisfile = thisfile[:len(thisfile) - 3]
    if __name__ == "__main__":
        resource = "../resources"
    else:
        resource = "./resources"
    dayinputfile = "{}/{}input.txt".format(resource, thisfile)
    with open(dayinputfile, mode='r', encoding='utf-8') as fileio:
        dayinput = fileio.read()
    dayinput = dayinput.strip('\n')
    return dayinput

def sort_by_frequencies(alphas):
    """
    returns dict of frequencies of the alphas
    """
    items = []
    temp = alphas[0]
    for x in range(1, len(alphas)):
        if alphas[x] == alphas[x - 1]:
            temp += alphas[x]
        else:
            items.append(temp)
            temp = alphas[x]
    items.append(temp)
    newa = ''.join([k[0] for k in sorted(items, key=lambda x: -len(x))[:5]])
    return newa

def encryptrooms(dayinput):
    """
    first half solver:
    encrypt real rooms and add the sum of rooms
    """
    realrooms = []
    cases = dayinput.split('\n')
    for encrypted in cases:
        #print("-------------------------------")
        #print(encrypted)
        #print("-------------------------------")
        e = encrypted.split('[')
        checksum = e[1][:-1]
        sector = int(e[0].split('-')[-1])
        alphas = ''.join(sorted(''.join(e[0].split('-')[:-1])))
        sortedalphas = sort_by_frequencies(alphas)
        if sortedalphas == checksum:
            #print(sortedalphas, sector)
            realrooms.append(sector)
        else:
            #print("DECOY", sortedalphas)
            pass
    print(sum(realrooms))

def app():
    """
    runs day application
    """
    print("Day #4:")
    dayinput = readdayinput()
    encryptrooms(dayinput)


if __name__ == "__main__":
    """
    MAIN APP
    """
    app()
