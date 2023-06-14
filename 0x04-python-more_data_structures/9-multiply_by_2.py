#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for k, v in a_dictionary.items():
        value = v * 2
        new_dict[k] = value
    return new_dict
