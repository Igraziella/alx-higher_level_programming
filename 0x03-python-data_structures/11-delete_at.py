#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > 0:
        return my_list

    length = len(my_list)
    new_list = delete_at(my_lis, idx)
    del my_list, idx
    return new_list
