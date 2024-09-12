#!/usr/bin/python3
"""10-square.py
"""

Rectangle = __import_('9-rectangle').Rectangle

class Square(Rectangle):
    """ inherits the rectagnle class """

    def __init__(self, size):
        """ init func for the obj"""
        self.integer_validator = size
        self.__size = size

    def area(self):
        """ Returns the area"""
        return size * size
