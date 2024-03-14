#!/usr/bin/python3
""" 
    this is based on the rectangle class from this same module
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """ this is a square class from the TRctangle module"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ the size getter for the class"""
        return self.size
    
    @size.setter
    def size(self, value):
        """ the size getter for the class"""
        self.size = value


