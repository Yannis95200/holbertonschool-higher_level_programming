#!/usr/bin/python3
def fizzbuzz():
    for f in range(1, 101):
        if f % 3 == 0 and f % 5 == 0:
            print("FizzBuzz")
        elif f % 3 == 0:
            print("Fizz")
        elif f % 5 == 0:
            print("Buzz")
        else:
            print(f)
