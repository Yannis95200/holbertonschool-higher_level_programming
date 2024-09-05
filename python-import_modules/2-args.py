#!/usr/bin/env python3
from sys import argv

if __name__ == "__main__":
    argv = sys.argv[1:]
    nombre_arguments = len(argv)


    if nombre_arguments == 0:
        print("0 argument.")
    elif nombre_arguments == 1:
        print("1 argument :")
    else:
        print(f"{nombre_arguments} arguments :")

    
    for i, arg in enumerate(argv, start=1):
        print(f"{i} : {arg}")
