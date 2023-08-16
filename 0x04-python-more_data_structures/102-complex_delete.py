#!/usr/bin/python3
# our own func is to be defined here [(Dtechguru)]
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

# our for statement ghere up (Dtechguru)
# got you covered
    for value_dic in list_keys:
        if value == a_dictionary.get(value_dic):
            del a_dictionary[value_dic]  # delete func here

# final return statement
    return (a_dictionary)
