#!/usr/bin/python3
# Dtechguru
"""Lets create our own special func"""
def search_replace(my_list, search, replace):
    """Am Dtechguru"""
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return (new_list)
# Auth: Dtechguru
