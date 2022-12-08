#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    uniq_list(new_list)
    for item in my_list:
        print(item)
