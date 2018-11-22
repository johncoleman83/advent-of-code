#!/usr/bin/env python3
"""
Advent of Code 2016: Day 5
"""
import hashlib

decrypted = [
    "00000fe1e92080b9951b053e70e31fcb",
    "000007c827126c81fa664211693f2540",
    "000007880153f1b804481a39a6d2e86a",
    "00000a6e225253b6aaa8f20efbaad8b5",
    "00000096164643e2e0fbf5a91bfd7f06",
    "00000e77a8b223b2d149990fb634bd74",
    "000006ec13bc03b597beee4fa9352176",
    "00000ee477915a03c15f93ac53769648"
]
cols = ['f', '7', '7', 'a', '0', 'e', '6', 'e']
thepassword = 'f77a0e6e'

def readdayinput():
    """
    Reads day input to solve
    """
    print("{}\n{}".format("-" * len("day5"), "day5"))
    encryption = "cxdnnyjw"
    return encryption

def doorpassword1(dayinput):
    """
    first half solver:
    get password from room encryption
    """
    m = hashlib.md5()
    i = 0
    password = []
    while len(password) < 8:
        check = str(hashlib.md5("{}{}".format(dayinput, i).encode()).hexdigest())
        if check[:5] == '00000':
            print(check)
            password.append(check)
        i += 1
    newpass = []
    for encrypted in password:
        newpass.append(encrypted[5])
    return ''.join(newpass)

def doorpassword2(dayinput):
    """
    second half solver:
    get password from room encryption
    """
    m = hashlib.md5()
    i = 0
    passwords = 0
    positions = [None] * 8
    while passwords < 8:
        check = str(hashlib.md5("{}{}".format(dayinput, i).encode()).hexdigest())
        if check[:5] == '00000':
            index = check[5]
            if index.isdigit():
                index = int(check[5])
                print(check)
                if index < 8 and positions[index] is None:
                    positions[index] = check[6]
                    passwords += 1
        i += 1
    return ''.join(positions)

def app():
    """
    runs day application
    """
    dayinput = readdayinput()
    password1 = doorpassword1(dayinput)
    print(password1)
    password2 = doorpassword2(dayinput)
    print(password2)


if __name__ == "__main__":
    """
    MAIN APP
    """
    app()
