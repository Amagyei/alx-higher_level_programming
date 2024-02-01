#!/usr/bin/python3
<<<<<<< HEAD
# 0-add_integer.py
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
=======

def add_integer(a, b=98):
    for item in (a, b):
        if type(item) not in (int, float):
            raise TypeError('{} must be an integer'.format(item))

    result = a + b
    return result

>>>>>>> refs/remotes/origin/main
