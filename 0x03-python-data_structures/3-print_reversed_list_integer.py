#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))

