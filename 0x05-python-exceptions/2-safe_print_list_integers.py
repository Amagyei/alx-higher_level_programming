#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    length = 0
    try:
        for i in my_list:
            length+=1
            if isinstance(i, int):
                print("{:d}".format(i), end="")
                count += 1
                if count >= x:
                    break
        print()
    except Exception as e:
        print('an error occured')
    try:
        if x > length:
            raise IndexError
    except IndexError as ie:
        print(f"IndexError: {ie}")
    return count
