#!/usr/bin/python3
def islower(c):
    return isinstance(c, str) and len(c) == 1 and 97 <= ord(c) <= 122
