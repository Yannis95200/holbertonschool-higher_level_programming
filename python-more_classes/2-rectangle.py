#!/usr/bin/python3
"""
This is a module that defines the Rectangle class.
"""


class Rectangle:
    """
    A class used to represent a Rectangle.

    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).

    Methods:
        __init__(self, width=0, height=0):
            Initializes the rectangle with a given width and height.
        width(self):
            Retrieves the width of the rectangle.
        width(self, value):
            Sets the width of the rectangle with validation.
        height(self):
            Retrieves the height of the rectangle.
        height(self, value):
            Sets the height of the rectangle with validation.
        area(self):
            Returns the area of the rectangle.
        perimeter(self):
            Returns the perimeter of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with a given width and height.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).

        Raises:
            TypeError: If `width` or `height` is not an integer.
            ValueError: If `width` or `height` is negative.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle with validation.

        Args:
            value (int): The width to set for the rectangle.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle with validation.

        Args:
            value (int): The height to set for the rectangle.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Computes and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Computes and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if either the width
            or the height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
