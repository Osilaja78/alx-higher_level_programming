#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_keys = []
    for k, v in a_dictionary.items():
        if v == value:
            del_keys.append(k)

    for i in del_keys:
        del(a_dictionary[i])
    return a_dictionary
