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

    number_of_instances = 0
    print_symbol = '#'
    square = 0

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
        Rectangle.number_of_instances += 1
        self.instance_attribute = (width == height)

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

    def __str__(self):
        """
        print the print_symbol with the character #
        """
        if self.width == 0 or self.height == 0:
            return ""
        result = ""
        for index in range(self.height):
            result += str(self.print_symbol) * self.width + "\n"
        return result.strip()

    def __repr__(self):
        """""
        Returns the formal string representation of the rectangle.


        Returns:
            str: A string that can be used to recreate the object.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Deletes a rectangle instance and prints a message.

        Prints:
            "Bye rectangle..." upon deletion of an instance.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
    Returns the rectangle with the larger or equal area.

    Args:
        rect_1 (Rectangle): First rectangle.
        rect_2 (Rectangle): Second rectangle.

    Returns:
        Rectangle: The rectangle with the larger or equal area.

    Raises:
        TypeError: If either argument is not a Rectangle.
    """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
    Returns a new square-shaped Rectangle.

    Args:
        size (int): Size of the square's sides (default is 0).

    Returns:
        Rectangle: A new Rectangle instance with equal width and height.
    """
        return cls(size, size)
