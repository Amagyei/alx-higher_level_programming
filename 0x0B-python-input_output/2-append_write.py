#!/usr/bin/python3
""" Defines a function that reads a file"""

def write_file(filename="",text=""):
    """ pprints the contedts of a UTF8 text file to stdout 
    
    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename,'a', encoding="utf-8") as f:
        return f.write(text)
