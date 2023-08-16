#!/usr/bin/python3
# Auth: Dtechguru

# we'll be defining a new func ()
def print_sorted_dictionary(a_dictionary):
    list_ord = list(a_dictionary.keys())
    list_ord.sort()
    # A for loop for i and a _dictionary.get(i) will be declared
    for i in list_ord:
        print("{}: {}".format(i, a_dictionary.get(i)))
