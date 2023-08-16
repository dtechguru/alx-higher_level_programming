#!/usr/bin/python3
# |-4-new_in_list.py-|
# Am "Dtechguru"

# def func toc to make our own func
def new_in_list(my_list, idx, element):

    # an element is subtituted in a list

    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
# now we will call copy it means copy also
    copy = [x for x in my_list]
    copy[idx] = element
    return (copy)
# and we still returned copy of what was copied rom the list
