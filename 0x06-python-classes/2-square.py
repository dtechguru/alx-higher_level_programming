#!/usr/bin/python3
# Dtechguru
# Class Square is defined here

 # Author: Dtechguru
class Square:
    # this should represent a square

    def __init__(self, size=0):
    # Dtechguru
        if not isinstance(size, int):
            raise TypeError("size must be an integer")  # Dtechguru
        elif size < 0:
            raise ValueError("size must be >= 0")  # Dtechguru
        self.__size = size
# Author: Dtechguru
