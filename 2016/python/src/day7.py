#!/usr/bin/env python3
"""
Advent of Code 2016: Day 7
"""
import os
testcase = """abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn"""

def readdayinput():
    """
    Reads day input to solve
    """
    #return testcase
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

def isvalid_tls(sub, brackets):
    """
    checks if substring is valid TLS IP7
    """
    ip7 = False
    if '[' in sub or ']' in sub:
        return "unknown"
    if sub[:2] == ''.join(list(reversed(sub[2:]))):
        if sub.count(sub[0]) == 4:
            ip7 = False
        else:
            ip7 = True
    if ip7 is False:
        return "unknown"
    if brackets is True and ip7 is True:
        return "invalid"
    if brackets is False and ip7 is True:
        return "valid"

def count_tls_ips(dayinput):
    """
    first half solver:
    """
    total = 0
    lines = dayinput.split('\n')
    for ip in lines:
        brackets = False
        isvalid_ip = False
        start = 0
        end = 4
        while end <= len(ip):
            sub = ip[start:end]
            if '[' in sub:
                brackets = True
            if ']' in sub:
                brackets = False
            validity = isvalid_tls(sub, brackets)
            if validity == "invalid":
                isvalid_ip = False
                break
            if validity == "valid":
                isvalid_ip = True
            start += 1
            end += 1
        if isvalid_ip is True:
            #print("valid: {}".format(ip))
            total += 1
        else:
            pass
            #print("invalid: {}".format(ip))
    return total

def isvalid_ssl(sub, brackets):
    """
    checks if substring is valid SSL IP7
    """
    valid = False
    if '[' in sub or ']' in sub:
        return "invalid"
    if sub[0] == sub[2] and sub[1] != sub[0]:
        if brackets == False:
            return "validaba"
        else:
            return "validbab"
    return "invalid"

def check_ssl(aba, bab):
    """
    checks if any matches of valid aba & bab are found
    """
    for a in aba:
        for b in bab:
            if a[0] == b[1] and b[0] == a[1]:
                return True
    return False

def count_ssl_ips(dayinput):
    """
    second half solver:
    """
    total = 0
    lines = dayinput.split('\n')
    for ip in lines:
        brackets = False
        start = 0
        end = 3
        aba = []
        bab = []
        while end <= len(ip):
            sub = ip[start:end]
            if '[' in sub:
                brackets = True
            if ']' in sub:
                brackets = False
            validity = isvalid_ssl(sub, brackets)
            if validity == "validaba":
                aba.append(sub)
            if validity == "validbab":
                bab.append(sub)
            start += 1
            end += 1
        isvalid_ip = check_ssl(aba, bab)
        if isvalid_ip is True:
            #print("valid: {} - {}:{}".format(ip, aba, bab))
            total += 1
        else:
            pass
            #print("invalid: {}".format(ip))
    return total

def app():
    """
    runs day application
    """
    print("Day #7:")
    dayinput = readdayinput()
    tls_ips = count_tls_ips(dayinput)
    ssl_ips = count_ssl_ips(dayinput)
    print(tls_ips)
    print(ssl_ips)


if __name__ == "__main__":
    """
    MAIN APP
    """
    app()
