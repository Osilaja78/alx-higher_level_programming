#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg_len = len(sys.argv)

    if arg_len == 1:
        print("0 arguments.")
    else:
        if arg_len == 2:
            print("1 argument:")
        else:
            print("{} arguments:".format(arg_len - 1))

        for i in range(arg_len - 1):
            i += 1
            print("{}: {}".format(i, sys.argv[i]))
