#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if ord('a') <= ord(a) <= ord('z'):
            a = chr(ord(a) - 32)
        print("{}".format(a), end='')
    print()
