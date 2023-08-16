#!/usr/bin/python3
# |divisible_by_2|
# |-Dtechguru-|

# lets make our own beautiful func now
def divisible_by_2(my_list=[]):
    """our new func is to find all multiple of 2 here."""
    multiples = []
    for i in range(len(my_list)):
        # i finally got to understand the meaning of %
        # it just calculate the remender not the percent
        if my_list[i] % 2 == 0:
            multiples.append(True)  # A true statement
            # lets use an else statement here
        else:
            multiples.append(False)
# return (nultiples) "Dtechguru"
    return (multiples)
