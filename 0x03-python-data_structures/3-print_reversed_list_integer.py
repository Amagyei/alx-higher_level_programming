#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
<<<<<<< HEAD
    """Print all integers of a list in reverse order."""
    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
=======
    i = len(my_list) - 1
    for item in my_list:
        print("{:d}".format(my_list[i]))
        i-=1

>>>>>>> refs/remotes/origin/main
