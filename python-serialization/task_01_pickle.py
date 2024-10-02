#!/usr/bin/python3
"""
Module for a CustomObject class with serialization and deserialization methods.
"""

import pickle


class CustomObject:
    """
    Represents a custom object with name, age, and student status.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes a CustomObject instance.

        Args:
            name (str): Name of the object.
            age (int): Age of the object.
            is_student (bool): Student status.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Displays the object's attributes."""
        print("Name : {}".format(self.name))
        print("Age : {}".format(self.age))
        print("Is Student : {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serializes the object to a file.

        Args:
            filename (str): Filename to save the object.
        """
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
            Deserializes an object from a file.

            Args:
                filename (str): Filename to load the object from.

            Returns:
                CustomObject: The deserialized object.
            """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return None
