#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in my_list:
            if isinstance(i, int):
                print(i, end="")
                count += 1
                if count >= x:
                    break
        print()
    except Exception as e:
        print('an error occured')
    
    return count
