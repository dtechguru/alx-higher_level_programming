#!/usr/bin/python3
# 1-element_at.py
"""It's Dtechguru"""
# we'll call a func name def to create our own function
def element_at(my_list, idx):
    #  Retrive an element from a list for Dtechguru program

    if idx < 0 or idx > (len(my_list) - 1):

        return None
    return (my_list[idx])
# in this program i got to know what return does
