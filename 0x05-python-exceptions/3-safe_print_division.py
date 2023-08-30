#!/usr/bin/python3
# Author: Dtechguru

def safe_print_division(a, b):
    # Author: Dtechguru
    """Return the division of a by b."""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))  # Author: Dtechguru
    return div  # Author: Dtechguru
