#!/usr/bin/python3
""" this module is based on the base class"""

from models.base import Base
import inspect

class Rectangle(Base):
    """ this module is based on the base class """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}'
    

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(inspect.currentframe().f_code.co_name))
        if value <= 0:
            raise ValueError('{} must be > 0'.format(inspect.currentframe().f_code.co_name))
        else:
            self.__width = value
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(inspect.currentframe().f_code.co_name))
        if value <= 0:
            raise ValueError('{} must be > 0'.format(inspect.currentframe().f_code.co_name))
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            self.__x = None
            raise TypeError('{} must be an integer'.format(inspect.currentframe().f_code.co_name))
        if value < 0:
            self.__x = None
            raise ValueError('{} must be >= 0'.format(inspect.currentframe().f_code.co_name))
        else:    
            self.__x = value
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            self.__y = None
            raise TypeError('y must be an integer')
        if value < 0:
            self.__y = None
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        return self.__height * self.__width
    
    
    def display(self):
        # Print y offset
        for _ in range(self.__y):
            print()

        # Print rectangle with x offset
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    
    def update(self, *args, **kwargs):
        # update the rectangle
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        for attr, value in kwargs.items():
            setattr(self, attr, value)


    
