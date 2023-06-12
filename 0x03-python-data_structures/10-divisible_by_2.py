#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_new = [not i % 2 for i in my_list]
    return list_new
