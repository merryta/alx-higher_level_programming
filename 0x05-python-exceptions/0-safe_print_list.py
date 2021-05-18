#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        j = 0
        for i, v in enumerate(my_list):
            if x > i:
                print(v, end="")
                j = j + 1
        print()
        return j
    except IndexError:
        return j
