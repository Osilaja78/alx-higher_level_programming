#!/usr/bin/python3
def uppercase(str):
    for char in str:
        ascii_value = ord(char)
        if 97 <= ascii_value <= 122:
            upper_char = chr(ascii_value - 32)
        else:
            upper_char = chr(ascii_value)
        print("{}".format(upper_char), end='')
    print()
