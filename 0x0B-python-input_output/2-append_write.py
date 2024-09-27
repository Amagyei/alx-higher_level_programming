#!/usr/bin/python3
""" Defines a function that reads a file"""

def write_file(filename="",text=""):
    """ pprints the contedts of a UTF8 text file to stdout """
    with open(filename,'a', encoding="utf-8") as f:
        return f.write(text)
