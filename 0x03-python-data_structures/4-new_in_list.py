#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)

    leng = len(my_list)

    if idx > leng - 1:
        return (my_list)

    new_element = my_list.copy()

    new_element[idx] = element

    return (new_element)
