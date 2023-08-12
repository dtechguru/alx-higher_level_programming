#!/usr/bin/python3
# we will be dealing with file name

# Dtechguru
if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
# Import func is been called dope
    import hidden_4

# declare a variable "name"
    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            # calling the one and final print statement
            print(name)
