#!/usr/bin/python3
"""Defines a Rectangle class based on 8-rectangle with area and string representation."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return string representation: [Rectangle] <width>/<height>"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
