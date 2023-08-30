#!/usr/bin/python3
"""Define one class Square."""


class Square:
    """Represent one square."""

    def __init__(self, size=0):
        """Initialize one new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size  # Author: Dtechguru

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size  # Author: Dtechguru

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")  # Author: Dtechguru
        elif value < 0:
            raise ValueError("size must be >= 0")  # Author: Dtechguru
        self.__size = value  # Author: Dtechguru

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size  # Author: Dtechguru

    def __eq__(self, other):
        """Define the == comparison to a Square."""
        return self.area() == other.area()  # Author: Dtechguru

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()  # Author: Dtechguru

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()  # Author: Dtechguru

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()  # Author: Dtechguru

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()  # Author: Dtechguru

    def __ge__(self, other):
        """Define the >= comparison to a Square."""
        return self.area() >= other.area()  # Author: Dtechguru
