#!/usr/bin/python3
"""
Module that defines Fish, Bird, and FlyingFish classes.
"""


class Fish:
    """
    A class representing a fish.

    Methods:
        swim(): Prints a message indicating the fish is swimming.
        habitat(): Prints the habitat of the fish.
    """

    def swim(self):
        """Prints a message indicating the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Prints the habitat of the fish."""
        print("The fish lives in water")


class Bird:
    """
    A class representing a bird.

    Methods:
        fly(): Prints a message indicating the bird is flying.
        habitat(): Prints the habitat of the bird.
    """

    def fly(self):
        """Prints a message indicating the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Prints the habitat of the bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A class representing a flying fish, inheriting from both Fish and Bird.

    Methods:
        fly(): Prints a message indicating the flying fish is soaring.
        swim(): Prints a message indicating the flying fish is swimming.
        habitat(): Prints the habitat of the flying fish.
    """

    def fly(self):
        """Prints a message indicating the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Prints a message indicating the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Prints the habitat of the flying fish."""
        print("The flying fish lives both in water and the sky!")
