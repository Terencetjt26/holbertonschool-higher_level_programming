#!/usr/bin/env python3
"""Duck Typing Example with Abstract Base Class"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract Base Class for shapes"""

    @abstractmethod
    def area(self):
        """Returns the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Returns the perimeter of the shape"""
        pass


class Circle(Shape):
    """Class representing a circle."""

    def __init__(self, radius):
        """Initializes the circle with a given radius"""
        self.radius = radius

    def area(self):
        """Returns the area of the circle"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Returns the perimeter of the circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Class representing a rectangle"""

    def __init__(self, width, height):
        """Initializes the rectangle with a given width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter of a given shape"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
