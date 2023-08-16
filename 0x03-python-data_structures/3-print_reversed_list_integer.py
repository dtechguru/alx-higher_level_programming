#!/usr/bin/python3
# |-3-print_reversed_list_integer.py-|
# this program is to print the reversed list style

# Dtechgu codes
# a define function is as def
# this function helps us create my func
def print_reversed_list_integer(my_list=[]):
    # all integers of the list will be printed reversed style
    # we will make use of an if statement
    if isinstance(my_list, list):
        my_list.reverse()
        # now our for loop
        for i in my_list:
            print("{:d}".format(i))
            # dtechgur style
