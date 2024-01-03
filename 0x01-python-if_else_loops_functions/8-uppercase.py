#!/usr/bin/python3
def uppercase(str):
    for i in str:
        c = ord(i)
        if c >= 97 and c <= 122:
            pc = chr(c - 32)
        else:
            pc = i
        print("{}".format(pc), end='')
    print()
