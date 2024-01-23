#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in my_list:
            print("{:d}".format(i)
            count++
            if count >= x:
                break
        print()
    except Exception as e:
        print('an error occured')
    
    return count
