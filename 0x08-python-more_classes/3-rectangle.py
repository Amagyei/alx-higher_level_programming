#!/usr/bin/python3
"""Define a class Square."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    def __str__(self):
        if self.width  == 0 or self.height == 0:
            return ""
        else:
            result = ""
            for h in range(self.height):
                for w in range(self.width):
                    result+='#'
                result+='\n'
            return result

    @property
    def width(self):
        """getter"""
        return self.__width
    @width.setter
    def width(self, value):
        """ setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter"""
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height muse be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if (self.height == 0) or (self.width == 0):
            return 0
        else:
            return 2 * self.height + 2 * self.width
    
