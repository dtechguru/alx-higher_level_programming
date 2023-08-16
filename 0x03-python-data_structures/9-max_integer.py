#!/usr/bin/python3
# |max_integer|
# Dtechguru on the line

# We'll lets define a new func
def max_integer(my_list=[]):
    """the greatest int is to be found in the list"""
    if len(my_list) == 0:
        """Dtechguru"""
        """our return statement should return nothing here"""
        return (None)
# a new variable name is declared here
    big = my_list[0]
    """
    a for loop now to create a for loop
    in the range of the num stored in my_list
    """
    for i in range(len(my_list)):
        if my_list[i] > big:
            big = my_list[i]
# our return statement is returning big here
    return (big)
