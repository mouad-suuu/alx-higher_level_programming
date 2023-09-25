#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0  # Initialize the index

    try:
        while count < x:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
            i += 1  # Increment the index
        print()
        return count
    except (IndexError, ValueError, TypeError):
        print()
        return count
