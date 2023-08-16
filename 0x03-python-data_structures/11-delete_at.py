#!/usr/bin/python3
# |-11-delete_at.py-|

# of course you gused it we'll create our new func
def delete_at(my_list=[], idx=0):
    """
    Our new func is to delete nums in a specific list.
    """
    if idx >= 0 and idx < len(my_list):
        # we'll call in the delete func known as del
        del my_list[idx]

        # a return statement with the address of (my_list) in it
    return (my_list)
