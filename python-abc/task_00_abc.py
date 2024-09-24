#!/usr/bin/env python3
"""
Defines an abstract Animal class and its subclasses.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract class for animals.
    """
    @abstractmethod
    def sound(self):
        """Returns the sound an animal makes."""
        pass

class Dog(Animal):
    """
    Dog class that returns 'Bark' as sound.
    """
    def sound(self):
        return "Bark"

class Cat(Animal):
    """
    Cat class that returns 'Meow' as sound.
    """
    def sound(self):
        return "Meow"