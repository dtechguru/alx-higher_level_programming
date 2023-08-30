#!/usr/bin/python3:
"""Author: Dtechguru"""
"""Define one class Square."""


class Square:
    """Author: Dtechguru"""
    """Represent one square."""
    def __init__(self, size):
        """Initialize one new square."""
# Author: Dtechguru
    self.size = size

    @property

    def size(self):
    # Get/set the current size of the square.
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    # Author: Dtechguru
    def area(self):
        # Return the current area of the square.
        return (self.__size * self.__size)
        # Author: Dtechguru
    def my_print(self):

        """Print the square with the  # symb style here"""

        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")  """Author: Dtechguru"""
        if self.__size == 0:
            print("")
"""Author: Dtechguru"""
