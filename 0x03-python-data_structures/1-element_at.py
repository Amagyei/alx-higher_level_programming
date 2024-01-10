#!/usr/bin/python3
<<<<<<< HEAD
# 1-element_at.py


def element_at(my_list, idx):
    """Retrive an element from a list."""
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return (my_list[idx])
=======

def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
>>>>>>> refs/remotes/origin/main
