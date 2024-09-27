#!/usr/bin/python3
""" Defines a function that reads a file"""

def write_file(filename=""):
    """ pprints the contedts of a UTF8 text file to stdout """
    with open(filename,'w', encoding="utf-8") as f:
        f.write(text)
