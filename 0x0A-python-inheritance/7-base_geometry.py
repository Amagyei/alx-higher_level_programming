#!/usr/bin/python3

""" empty class"""


class BaseGeometry():
    """ empty class """

    def area(self):
        """Not implemented."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
	""" validates the value variable"""
	if !isinstance(int, value):
	    raise TypeError(name + " must be an integer")
	if value <= 0:
            raise ValueError(name + " must be greater than 0")
