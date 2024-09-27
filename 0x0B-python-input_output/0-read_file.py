#!/usr/bin/python3
""" Defines a function that reads a file"""

def read_file(filename=""):
    """ pprints the contedts of a UTF8 text file to stdout """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
