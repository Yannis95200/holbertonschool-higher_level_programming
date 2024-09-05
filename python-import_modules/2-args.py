#!/usr/bin/env python3
from sys import argv

if __name__ == "__main__":
    arguments = argv[1:]
    nombre_argu = len(arguments)
    print(f"{nombre_argu} argument{'s' if nombre_argu != 1 else ''}", end="")


    if nombre_argu == 0:
        print(".")
    elif nombre_argu == 1:
        print(":")
    else:
        print(":")


    for i, arg in enumerate(arguments, start=1):
        print(f"{i} : {arg}")
