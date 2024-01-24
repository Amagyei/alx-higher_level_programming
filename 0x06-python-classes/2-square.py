#!/usr/bin/python3

def Square:
    def __init__(self, size=0):
        # Validate that size is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        # Validate that size is not less than 0
        if size < 0:
            raise ValueError("size must be >= 0")

        # Set the private instance attribute
        self.__size = size
