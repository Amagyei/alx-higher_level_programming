#!/usr/bin/python3
"""REctangle"""

class Rectangle(BaseGeometry):
"""Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
	"""Initialize a new Rectangle instance."""
	self.integer_validator("width", width)
	self.integer_validator("height", height)
	self.__width = width
	self.__height = height
