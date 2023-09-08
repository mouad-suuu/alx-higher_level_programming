#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    # Get the total number of arguments (excluding the script name)
    num_args = len(argv) - 1

    if num_args == 0:
        print("0 arguments.")
    else:
        print("{} {}:".format(num_args, "argument" if num_args == 1 else "arguments"))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
