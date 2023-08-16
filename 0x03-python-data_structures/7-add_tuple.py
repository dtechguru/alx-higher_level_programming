#!/usr/bin/python3
# "Dtechguru"


def add_tuple(tuple_a=(), tuple_b=()):
    # dont know what tuples does yet let's find out
    # Dtechguru
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            # tuple here (Dtechguru)
            tuple_a = 0, 0
            # lets make an else call
        else:
            tuple_a = tuple_a[0], 0
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
            # lets call another else
        else:
            tuple_b = tuple_b[0], 0
# our code shoud return a statement and an interger Dtechguru
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
# and there we have it our coe's all set
