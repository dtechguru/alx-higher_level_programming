#!/usr/bin/python3
# Author: Dtechguru
"""Define one class Square."""


class Square:
    """Represent one square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize one new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        Author: Dtechguru
        """
        self.size = size  # Author: Dtechguru
        self.position = position  # Author: Dtechguru

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

    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.__position  # Author: Dtechguru

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")  # Author: Dtechguru
        self.__position = value  # Author: Dtechguru

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size  # Author: Dtechguru

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")  # Author: Dtechguru
            return

        [print("") for i in range(self.__position[1])]  # Author: Dtechguru
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]  # Author: Dtechguru
            [print("#", end="") for k in range(self.__size)]  # Author: Dtechguru
            print("")  # Author: Dtechguru

