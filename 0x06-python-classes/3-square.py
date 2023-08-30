#!/usr/bin/python3
# Author: Dtechguru
"""This is the defination of a class square ."""


class Square:
    # dis takes de shape of a square
    def __init__(self, size=0):

        # a new square is now den initialized
        if not isinstance(size, int):
            raise TypeError("size must be an integer")   # dtechguru

        elif size < 0:
            raise ValueError("size must be >= 0")  # dtechguru
        self.__size = size

    def area(self):
        # dhe area of dhe square is returned
        return (self.__size * self.__size)
# dtechguru
