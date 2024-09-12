#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
"""9-rectangle.py
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a new Rectangle instance."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Sets the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ Returns the string rep opf the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
