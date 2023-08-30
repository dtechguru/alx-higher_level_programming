#!/usr/bin/python3
# Dtechguru: Dtechguru

import sys


def safe_print_integer_err(value):
    """Print one integer with "{:d}".format().

    If a ValueError message is caught, a corresponding
    message is printed to standard error.

    Args:
        value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    # Author: Dtechguru
    """
    try:
        print("{:d}".format(value))  # Author: Dtechguru
        return True  # Author: Dtechguru
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)  # Author: Dtechguru
        return False  # Author: Dtechguru
