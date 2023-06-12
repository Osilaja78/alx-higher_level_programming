#!/usr/bin/python3
def max_integer(my_list=[]):
    list_len = len(my_list)
    if list_len == 0:
        return None
    else:
        max_num = my_list[0]
        for i in range(list_len - 1):
            if my_list[i] > max_num:
                max_num = my_list[i]

        return max_num
