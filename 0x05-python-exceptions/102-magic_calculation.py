#!/usr/bin/python3
# Author: dtechguru

import sys


def safe_function(fct, *args):
    """Execute one function safely.

    Args:
        fct: The function to execute.
        args: Arguments for fct.

    Returns:
        If an error occurs - None.
        Otherwise - the result of the call to fct.
    Author: Dtechguru
    """
    try:
        result = fct(*args)  # Author: Dtechguru
        return result  # Author: Dtechguru
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)  # Author: Dtechguru
        return None  # Author: Dtechguru
