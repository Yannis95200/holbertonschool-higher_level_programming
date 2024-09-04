#!/usr/bin/python3

def uppercase(str):
    for uppercase1 in str:
        if (ord(uppercase1) <= ord('z') and ord(uppercase1) >= ord('a')):
            uppercase2 = chr(ord(uppercase1) - 32)
        else:
            uppercase2 = uppercase1
        print("{}".format(uppercase2), end='')
    print()
