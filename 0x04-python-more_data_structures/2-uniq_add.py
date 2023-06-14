#!usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = []

    for x in my_list:
        if x not in unique_set:
            unique_set.append(x)

    result = 0
    for i in unique_set:
        result += i
    return result
