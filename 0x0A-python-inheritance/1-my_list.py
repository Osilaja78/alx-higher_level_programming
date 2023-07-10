#!/usr/bin/python3
"""
A class MyList.
"""


class MyList(list):
    """
    A MyList class that inherits form
    list.
    """

    def print_sorted(self):
        "Prints the list in ascending sort"

        sorted_list = sorted(self)
        print(sorted_list)
