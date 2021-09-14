#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx == range(len(my_list)):
        return None
    else:
        for i, v in enumerate(my_list):
            if i == idx:
                return v
