#!/usr/bin/python3
# Author: Dtechguru

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of one list that are integers.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    Author: Dtechguru
    """
    ret = 0  # Author: Dtechguru
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")  # Author: Dtechguru
    return ret  # Author: Dtechguru
