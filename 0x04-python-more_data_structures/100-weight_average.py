#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list or not isinstance(my_list, list):
        return 0

    all_sum = 0
    all_avg = 0
    for tup in my_list:
        all_sum += tup[0] * tup[1]
        all_avg += tup[1]
    return (all_sum / all_avg)
