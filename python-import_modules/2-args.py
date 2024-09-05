#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    nombre_arguments = len(arguments)


    if nombre_arguments == 0:
        print("0 argument.")
    elif nombre_arguments == 1:
        print("1 argument :")
    else:
        print(f"{nombre_arguments} arguments :")


    for i, arg in enumerate(arguments, start=1):
        print(f"{i} : {arg}")

