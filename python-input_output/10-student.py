#!/usr/bin/python3
"""
Module that defines a Student class.
"""


class Student:
    """
    Represents a student with a first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        If attrs is provided, only the attributes specified in attrs
        are included in the returned dictionary.

        Args:
            attrs (list, optional): A list of attribute names to include
            in the dictionary representation. Defaults to None.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for index in attrs:
            if index in self.__dict__:
                new_dict[index] = self.__dict__[index]
        return new_dict
