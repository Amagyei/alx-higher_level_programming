#!/usr/bin/python3
def safe_print_integer(value):
    count = 0
    try:
        print("{:d}".format(value))
        print()
        return True
    except Exception as e:
        print('an error occured')
        return False
