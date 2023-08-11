#!/usr/bin/python3
# Dtechguru

# We will call an if statement
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

# count is new to me but it is actually related to int
    count = len(sys.argv) - 1  # actually found out in this code that
    # python uses inline comment
    if count == 0:  # Nice
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))  # Dtechguru
