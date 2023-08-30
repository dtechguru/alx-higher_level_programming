#!/usr/bin/python3
# Author: Dtechguru

def safe_print_integer(value):
    """Print one integer with "{:d}".format().

    Args:
        value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    Author: Dtechguru
    """
    try:
        print("{:d}".format(value))  # Author: Dtechguru
        return True  # Author: Dtechguru
    except (TypeError, ValueError):
        return False  # Author: Dtechguru
