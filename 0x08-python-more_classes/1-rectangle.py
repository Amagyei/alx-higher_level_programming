#!/usr/bin/python3
"""Define a class Square."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height


    def width(self):
        """getter"""
        return self.__width

    def width(self, value):
        """ setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value


    def height(self):
        """getter"""
        return self.__height
    
    def heigth(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height muse be >= 0")
        else:
            self.__height = value

