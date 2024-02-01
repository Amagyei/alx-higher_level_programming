#!/usr/bin/python3

def add_integer(a, b=98):
    for item in (a, b):
        if type(item) not in (int, float):
            raise TypeError('{} must be an integer'.format(item))

    result = a + b
    return result

